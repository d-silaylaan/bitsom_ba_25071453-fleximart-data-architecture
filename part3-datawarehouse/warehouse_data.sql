use fleximart_dw;
INSERT INTO dim_date VALUES
(20240101,'2024-01-01','Monday',1,1,'January','Q1',2024,false),
(20240102,'2024-01-02','Tuesday',2,1,'January','Q1',2024,false),
(20240103,'2024-01-03','Wednesday',3,1,'January','Q1',2024,false),
(20240104,'2024-01-04','Thursday',4,1,'January','Q1',2024,false),
(20240105,'2024-01-05','Friday',5,1,'January','Q1',2024,false),
(20240106,'2024-01-06','Saturday',6,1,'January','Q1',2024,true),
(20240107,'2024-01-07','Sunday',7,1,'January','Q1',2024,true),
(20240108,'2024-01-08','Monday',8,1,'January','Q1',2024,false),
(20240109,'2024-01-09','Tuesday',9,1,'January','Q1',2024,false),
(20240110,'2024-01-10','Wednesday',10,1,'January','Q1',2024,false),
(20240111,'2024-01-11','Thursday',11,1,'January','Q1',2024,false),
(20240112,'2024-01-12','Friday',12,1,'January','Q1',2024,false),
(20240113,'2024-01-13','Saturday',13,1,'January','Q1',2024,true),
(20240114,'2024-01-14','Sunday',14,1,'January','Q1',2024,true),
(20240115,'2024-01-15','Monday',15,1,'January','Q1',2024,false),
(20240116,'2024-01-16','Tuesday',16,1,'January','Q1',2024,false),
(20240117,'2024-01-17','Wednesday',17,1,'January','Q1',2024,false),
(20240118,'2024-01-18','Thursday',18,1,'January','Q1',2024,false),
(20240119,'2024-01-19','Friday',19,1,'January','Q1',2024,false),
(20240120,'2024-01-20','Saturday',20,1,'January','Q1',2024,true),
(20240121,'2024-01-21','Sunday',21,1,'January','Q1',2024,true),
(20240122,'2024-01-22','Monday',22,1,'January','Q1',2024,false),
(20240123,'2024-01-23','Tuesday',23,1,'January','Q1',2024,false),
(20240124,'2024-01-24','Wednesday',24,1,'January','Q1',2024,false),
(20240125,'2024-01-25','Thursday',25,1,'January','Q1',2024,false),
(20240126,'2024-01-26','Friday',26,1,'January','Q1',2024,false),
(20240127,'2024-01-27','Saturday',27,1,'January','Q1',2024,true),
(20240128,'2024-01-28','Sunday',28,1,'January','Q1',2024,true),
(20240129,'2024-01-29','Monday',29,1,'January','Q1',2024,false),
(20240130,'2024-01-30','Tuesday',30,1,'January','Q1',2024,false);


INSERT INTO dim_product(product_id,product_name,category,subcategory,unit_price) VALUES
('P001','Laptop','Electronics','Computers',60000),
('P002','Headphones','Electronics','Audio',2000),
('P003','Smartphone','Electronics','Mobiles',30000),
('P004','Tablet','Electronics','Computers',25000),
('P005','Keyboard','Electronics','Accessories',1500),
('P006','Shoes','Fashion','Footwear',2500),
('P007','T-Shirt','Fashion','Clothing',800),
('P008','Jeans','Fashion','Clothing',2000),
('P009','Washing Machine','Appliances','Home',45000),
('P010','Microwave','Appliances','Kitchen',12000),
('P011','Refrigerator','Appliances','Home',70000),
('P012','Mixer Grinder','Appliances','Kitchen',6000),
('P013','Book','Stationery','Books',500),
('P014','Notebook','Stationery','Paper',200),
('P015','Pen','Stationery','Writing',50);


INSERT INTO dim_customer(customer_id,customer_name,city,state,customer_segment) VALUES
('C001','Amit Sharma','Mumbai','Maharashtra','Retail'),
('C002','Priya Verma','Delhi','Delhi','Retail'),
('C003','Rahul Mehta','Bengaluru','Karnataka','Corporate'),
('C004','Sneha Nair','Chennai','Tamil Nadu','Retail'),
('C005','Vikas Singh','Pune','Maharashtra','SMB'),
('C006','Ritu Kapoor','Jaipur','Rajasthan','Retail'),
('C007','Arjun Patel','Ahmedabad','Gujarat','Corporate'),
('C008','Neha Gupta','Kolkata','West Bengal','Retail'),
('C009','Rohan Das','Hyderabad','Telangana','SMB'),
('C010','Simran Kaur','Chandigarh','Punjab','Retail'),
('C011','Manoj Yadav','Noida','Uttar Pradesh','Corporate'),
('C012','Divya Rao','Mumbai','Maharashtra','Retail');


INSERT INTO fact_sales(date_key,product_key,customer_key,quantity_sold,unit_price,discount_amount,total_amount) VALUES
(20240101,1,3,1,60000,0,60000),
(20240101,2,5,2,2000,0,4000),
(20240102,3,2,1,30000,1000,29000),
(20240102,7,4,3,800,0,2400),
(20240103,6,1,1,2500,0,2500),
(20240103,10,8,1,12000,500,11500),
(20240104,5,6,2,1500,0,3000),
(20240104,13,7,4,500,0,2000),
(20240105,1,9,1,60000,2000,58000),
(20240105,3,10,1,30000,0,30000),

(20240106,6,2,3,2500,0,7500),
(20240106,9,1,1,45000,1000,44000),
(20240106,11,5,1,70000,5000,65000),

(20240107,2,4,4,2000,0,8000),
(20240107,8,3,2,2000,0,4000),
(20240107,12,6,1,6000,0,6000),

(20240108,4,12,1,25000,0,25000),
(20240108,14,9,5,200,0,1000),

(20240109,5,11,2,1500,0,3000),
(20240109,3,8,1,30000,0,30000),

(20240110,7,1,2,800,0,1600),
(20240110,9,2,1,45000,0,45000),

(20240111,10,12,1,12000,200,11800),

(20240112,1,6,1,60000,1000,59000),

(20240113,6,5,4,2500,0,10000),
(20240113,8,7,3,2000,0,6000),

(20240114,3,3,2,30000,2000,58000),
(20240114,2,10,5,2000,0,10000),

(20240115,1,4,1,60000,0,60000),

(20240116,15,2,10,50,0,500),
(20240117,13,8,3,500,0,1500),

(20240118,12,9,1,6000,0,6000),

(20240119,4,6,1,25000,1000,24000),

(20240120,11,1,1,70000,2000,68000),
(20240120,6,3,3,2500,0,7500),

(20240121,2,12,6,2000,0,12000),
(20240121,7,5,4,800,0,3200);

