1. Entity–Relationship Description (Text Format)
ENTITY: customers

Purpose: Stores customer information required to manage orders and communication.

Attributes:

customer_id: Unique identifier for each customer (Primary Key)

first_name: Customer’s first name

last_name: Customer’s last name

email: Customer’s email address (Unique)

phone: Customer’s phone number

city: City where the customer resides

registration_date: Date when the customer registered

Relationships:

One customer can place many orders (1:M relationship with orders table)


2. ENTITY: products

Purpose: Stores information about products available for sale.

Attributes:

product_id: Unique identifier for each product (Primary Key)

product_name: Name of the product

category: Product category

price: Price per unit

stock_quantity: Available stock

Relationships:

One product can appear in many order items (1:M relationship with order_items table)

3. ENTITY: orders

Purpose: Stores order-level information for each customer purchase.

Attributes:

order_id: Unique identifier for each order (Primary Key)

customer_id: Identifier of the customer who placed the order (Foreign Key)

order_date: Date when the order was placed

status: Order status (e.g., Completed, Pending)

total_amount: Total monetary value of the order

Relationships:

One order belongs to one customer (M:1 with customers)

One order can contain many order items (1:M with order_items)

3. ENTITY: order_items

Purpose: Stores individual product details within an order.

Attributes:

order_item_id: Unique identifier for each order item (Primary Key)

order_id: Identifier of the associated order (Foreign Key)

product_id: Identifier of the product (Foreign Key)

quantity: Quantity of the product ordered

unit_price: Price per unit at the time of order

total_price: Total price for the item (quantity × unit_price)

Relationships:

Many order items belong to one order

Many order items reference one product


Normalization Explanation (3NF)

The FlexiMart database design follows Third Normal Form (3NF) principles to ensure data integrity and minimize redundancy.

In this schema, all tables contain attributes that are fully functionally dependent on their respective primary keys. For example, in the customers table, attributes such as first name, last name, email, and city depend only on customer_id. There are no partial dependencies, as each table has a single-column primary key.

Transitive dependencies are eliminated by separating data into appropriate tables. Product-related information is stored exclusively in the products table, while order-level details are maintained in the orders table. The order_items table resolves the many-to-many relationship between orders and products by storing item-level details.

Functional dependencies include:

customer_id → customer attributes

product_id → product attributes

order_id → order attributes
This design prevents update anomalies (e.g., changing product price in one place), insert anomalies (e.g., inserting an order without customer data), and delete anomalies (e.g., deleting an order does not remove product records). Therefore, the schema satisfies all conditions of 3NF.


Sample Data Representation

Customers
customer_id	first_name	last_name	email	phone	city	registration_date
1	Rahul	Sharma	rahul.sharma@gmail.com	919876543210	Bangalore	2023-01-15
2	Priya	Patel	priya.patel@yahoo.com	919988776655	Mumbai	2023-02-20
3	Amit	Kumar	9765432109@noemail.com	919765432109	Delhi	2023-03-10

products

product_id	product_name	    category	price	stock_quantity
1	        Samsung Galaxy S21	Electronics	45999.00	150
2	        Nike Running Shoes	Fashion	    3499.00	    80
3	        Apple MacBook Pro	Electronics	52999.00	45

orders

order_id	customer_id	order_date	total_amount	status
1	         1	       2024-01-15	45999.00	Completed
2	         2	       2024-01-16	5998.00	    Completed
3	         3	       2024-01-15	52999.00	Completed
