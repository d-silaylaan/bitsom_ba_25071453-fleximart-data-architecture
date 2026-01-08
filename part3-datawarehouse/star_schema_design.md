Section 1 – Schema Overview

This star schema is used to store sales data for FlexiMart.
The goal is to help understand sales trends, customers, and products.

▶ Fact Table: fact_sales

This table stores each sales transaction at the product line-item level.
So one row = one product sold in one order.

Numbers stored (measures):

quantity_sold → how many units sold

unit_price → price per unit

discount_amount → discount given

total_amount → final amount paid

Links to other tables (foreign keys):

date_key → links to date table

product_key → links to product table

customer_key → links to customer table


▶ Dimension Table: dim_date

Used for time-based analysis.

Columns include:

date_key (PK)

full_date

day_of_week

month

month_name

quarter

year

is_weekend

This helps answer questions like:

“How many sales on weekends?”

“Which month sells most?”

▶ Dimension Table: dim_product

Stores product information.

Columns:

product_key (PK)

product_id

product_name

category

subcategory

unit_price

Used for:

category-wise sales

most selling products


▶ Dimension Table: dim_customer

Stores customer information.

Columns:

customer_key (PK)

customer_id

customer_name

city

state

customer_segment

Used for:

city-wise sales

customer analysis


Section 2 – Design Decisions

The data is stored at the transaction line-item level because it keeps the most detail. Later, this data can be summed to see totals by day, month, product, or customer.

Surrogate keys are used instead of business IDs because business IDs may change or repeat. Surrogate keys are simple numbers that are stable and easy for joins.

Drill-down and roll-up are possible because the dimensions have hierarchies.
For example:

Day → Month → Quarter → Year

Product → Subcategory → Category

This makes reporting flexible and fast.

Section 3 – Sample Data Flow (Elaborated Explanation)

This section explains how one real-world sales transaction is stored inside the data warehouse using the star schema.

Step 1 — Source Transaction (Real-World Event)

Suppose a customer buys a laptop from FlexiMart.

Example Sale:

Order Number: 101

Date: 15 January 2024

Customer Name: John Doe

Product: Laptop

Quantity: 2

Unit Price: ₹50,000

So, the total sale amount = 2 × 50,000 = ₹1,00,000.

This is how the sale happens in the real world.

Step 2 — Convert Information into Dimensions

Instead of storing the full text again and again,
we store the details separately in dimension tables.

Date goes to dim_date
date_key: 20240115
full_date: 2024-01-15
day_of_week: Monday
month: 1
quarter: Q1
year: 2024
is_weekend: false

Product goes to dim_product
product_key: 5
product_name: Laptop
category: Electronics
subcategory: Computers
unit_price: 50000

Customer goes to dim_customer
customer_key: 12
customer_name: John Doe
city: Mumbai
state: Maharashtra
customer_segment: Retail

Step 3 — Store the Sale in fact_sales
fact_sales:
date_key: 20240115
product_key: 5
customer_key: 12
quantity_sold: 2
unit_price: 50000
discount_amount: 0
total_amount: 100000
