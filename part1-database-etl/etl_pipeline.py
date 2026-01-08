import pandas as pd
import datetime
import re
from datetime import datetime
import mysql.connector



#------------READING CSV FILES----------------------------
customer = pd.read_csv('customers_raw.csv')
product = pd.read_csv('products_raw.csv')
sale = pd.read_csv('sales_raw.csv')

#---------------REPORT------------------------------------

report = {
    "customers" : {"processed" : 0, "Duplicates" : 0, "Missing" : 0, "Records": 0},
    "products" : {"processed" : 0, "Duplicates" : 0, "Missing" : 0, "Records": 0},
    "sales" : {"processed" : 0, "Duplicates" : 0, "Missing" : [0,0], "Records": 0}
}

#-----DEFINING FUNCTIONS-----------------------------------
def format_phone(phone):
    if pd.isna(phone):
        return None
    digits = re.sub(r"\D", "", str(phone))   #removes anything that is not a digit
    if len(digits) == 12 and digits.startswith("91"):
        return digits
    elif len(digits) == 10:
        return "91" + digits
    return None


def format_date(date):
    dt = pd.to_datetime(date).date()
    fdt = dt.strftime("%Y-%m-%d")
    return fdt




#-------------TRANSFORM CUSTOMERS_RAW.CSV---------------------
report["customers"]["processed"] = len(customer)
dup = customer.duplicated().sum()
report["customers"]["Duplicates"] = int(dup)
customer.drop_duplicates(inplace=True)
missing_email = customer["email"].isna().sum()
report["customers"]["Missing"]= int(missing_email)
customer["email"] = customer["email"].fillna(customer["phone"]+ "@noemail.com")
customer["phone"] = customer["phone"].apply(format_phone)
customer["registration_date"] = customer["registration_date"].apply(format_date)

#print(customer)
#print(report)

#-------------TRANSFORM PRODUCTS_RAW.CSV-----------------------

report["products"]["processed"] = len(product)

dup = product.duplicated().sum()
report["products"]["Duplicates"] = int(dup)
product.drop_duplicates(inplace=True)

product["category"] = product["category"].str.title()

missing_price = product["price"].isna().sum()
report["products"]["Missing"] = int(missing_price)
sale_price = sale.groupby("product_id")["unit_price"].first()
product["price"] = product["price"].fillna(product["product_id"].map(sale_price))

product["stock_quantity"].fillna(0, inplace=True)
#print(product)
#print(report)



#-------------TRANSFORM SALES_RAW.CSV---------------------------

report["sales"]["processed"] = len(sale)

dup = sale.duplicated().sum()
report["sales"]["Duplicates"] = int(dup)
sale.drop_duplicates(inplace=True)

sale["transaction_date"] = sale["transaction_date"].apply(format_date)

missing_custid = sale["customer_id"].isna().sum()
missing_prodid = sale["product_id"].isna().sum()
report["sales"]["Missing"][0] = int(missing_custid)
report["sales"]["Missing"][1] = int(missing_prodid)
sale.dropna(subset=["customer_id", "product_id"], inplace=True)

sale["subtotal"] = sale["quantity"] * sale["unit_price"]
sale["subtotal"] = sale["subtotal"].apply(lambda x: round(float(x), 2))

#print(sale)
#print(report)


#-------------LOAD FILES TO MYSQL-------------------------------
# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Divya#3007",
    database="fleximart"
)
cursor = conn.cursor()


for _, row in product.iterrows():
    cursor.execute(
        """
        INSERT INTO products (product_name, category, price, stock_quantity)
        VALUES (%s, %s, %s, %s)
        """,
        tuple(row[1:])
    )
    report["products"]["Records"] += 1

conn.commit()
cursor.close()


cursor = conn.cursor()

for _, row in customer.iterrows():
    cursor.execute(
        """
        INSERT INTO customers (first_name, last_name, email, phone, city, registration_date)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            first_name = VALUES(first_name),
            last_name = VALUES(last_name),
            phone = VALUES(phone),
            city = VALUES(city)
        """,
        tuple(row[1:])
    )
    report["customers"]["Records"] += 1

conn.commit()
cursor.close()

cursor = conn.cursor()


# fetch customer_id

merged = sale.merge(
    customer,
    on="customer_id",
    how="left"
)

merged2 = merged.merge(
    product,
    on="product_id",
    how="left"
)



for _, row in merged.iterrows():

    cursor.execute(
        "SELECT customer_id FROM customers WHERE email = %s",
        (row["email"],)
    )

    result = cursor.fetchone()

    if result is None:
        print(f"Customer not found for email: {row['email']}")
        continue

    customer_id = result[0]

    # now insert into orders
    cursor.execute(
        """
        INSERT INTO orders (customer_id, order_date, total_amount, status)
        VALUES (%s, %s, %s, %s)
        """,
        (customer_id, row["transaction_date"], row["subtotal"], row["status"])
    )
    report["sales"]["Records"] += 1

conn.commit()


cursor.close()

cursor = conn.cursor()

for index, row in merged2.iterrows():

    cursor.execute(
        "SELECT product_id FROM products WHERE product_name = %s",
        (row["product_name"],)
    )
    result = cursor.fetchone()
    merged2.loc[index, "product_id"]= result[0]

    cursor.execute(
        "SELECT customer_id FROM customers WHERE email = %s",
        (row["email"],)
    )
    result2 = cursor.fetchone()
    merged2.loc[index, "customer_id"] = result2[0]


conn.commit()


cursor.close()


cursor = conn.cursor()
for index, row in merged2.iterrows():

    # find the order_id
    cursor.execute(
        """
        SELECT order_id 
        FROM orders
        WHERE customer_id = %s
          AND order_date = %s
        """,
        (row["customer_id"], row["transaction_date"])
    )

    order = cursor.fetchone()

    order_id = order[0]   # assume order already exists


    # insert order item
    cursor.execute(
        """
        INSERT INTO order_items (
            order_id,
            product_id,
            quantity,
            unit_price,
            subtotal
        )
        VALUES (%s, %s, %s, %s,%s)
        """,
        (
            order_id,
            row["product_id"],
            row["quantity"],
            row["unit_price"],
            row["subtotal"]
        )
    )

conn.commit()
cursor.close()

conn.close()







#-------------DATA QUALITY REPORT---------------------------------

with open("data_quality_report.txt", "w") as f:
    f.write("DATA QUALITY REPORT\n")
    f.write("---------------------------------------------\n")
    f.write("customers_raw.csv\n")
    f.write(f"Number of records processed: {report["customers"]["processed"]}\n")
    f.write(f"Number of duplicates removed: {report["customers"]["Duplicates"]}\n")
    f.write(f"Number of missing emails handled: {report["customers"]["Missing"]}\n")
    f.write(f"Number of records loaded successfully: {report["customers"]["Records"]}\n")
    f.write("---------------------------------------------\n")

    f.write("products_raw.csv\n")
    f.write(f"Number of records processed: {report["products"]["processed"]}\n")
    f.write(f"Number of duplicates removed: {report["products"]["Duplicates"]}\n")
    f.write(f"Number of missing prices handled: {report["products"]["Missing"]}\n")
    f.write(f"Number of records loaded successfully: {report["products"]["Records"]}\n")

    f.write("----------------------------------------------\n")
    f.write("sales_raw.csv\n")
    f.write(f"Number of records processed: {report["sales"]["processed"]}\n")
    f.write(f"Number of duplicates removed: {report["sales"]["Duplicates"]}\n")
    f.write(f"Number of missing customer ID handled: {report["sales"]["Missing"][0]}\n")
    f.write(f"Number of missing product ID handled: {report["sales"]["Missing"][1]}\n")
    f.write(f"Number of records loaded successfully: {report["sales"]["Records"]}\n")


