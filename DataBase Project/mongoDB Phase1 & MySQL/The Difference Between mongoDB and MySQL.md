After using both of the two database tools to save the data of the world airport, I found that these two tools are different
in these aspects:

1. We must connect the server before we can write, read, upload, delete data in the database by using mongoDB. In other words, we must connect the internet before using mongoDB. However, we can use MySQL off-line. We just need to install MySQL on computer, then we do not need to connect internet to use MySQL. We can write python code to create database on our own computer, instead of on the server side.

2. Since we can use MySQL off-line, it also means the databse may occupy more space on our own computer. The mongoDB only cost a little space on personal computer.

3. MySQL and mongoDB save date in different ways. When we use MySQL, we must state what format we want to input into the database. However, when we use mongoDB, we can input data in dictionary or hash table type.
