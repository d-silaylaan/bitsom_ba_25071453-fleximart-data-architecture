Section A: Limitations of RDBMS 

Relational databases use a fixed schema, which makes them unsuitable for product catalogs where products have different attributes. For example, laptops require fields like RAM and processor, while shoes need size and color. In an RDBMS, this either leads to many nullable columns or multiple tables with complex joins, increasing design and maintenance effort.
Additionally, whenever a new product type is introduced, schema changes such as altering tables or adding new tables are required. These changes can be risky, time-consuming, and may cause downtime in production systems.
Storing customer reviews is also challenging in relational databases because reviews are naturally nested within products. This requires separate tables and joins to retrieve product details along with reviews, which impacts performance and increases query complexity. Overall, RDBMS struggles with flexibility, scalability, and efficient handling of semi-structured and nested data in such scenarios.


Section B: NoSQL Benefits 

MongoDB solves these problems by using a flexible, document-based schema. Each product can store only the attributes relevant to it, allowing laptops and shoes to exist in the same collection without schema changes. This flexibility makes it easy to add new product types without altering existing data structures.
MongoDB also supports embedded documents, enabling customer reviews to be stored directly inside product documents. This reduces the need for joins and allows faster retrieval of product data along with its reviews.
Furthermore, MongoDB provides horizontal scalability through sharding, which allows data to be distributed across multiple servers. This makes it suitable for handling large volumes of product and review data while maintaining performance. As a result, MongoDB is well-suited for dynamic and growing product catalogs.


Section C: Trade-offs 

One disadvantage of MongoDB compared to MySQL is weaker support for complex transactions and joins, which can be important for applications requiring strict relational consistency.
Another drawback is the lack of enforced schema at the database level, which can lead to inconsistent data if proper validation is not implemented at the application layer. This places additional responsibility on developers to maintain data integrity.