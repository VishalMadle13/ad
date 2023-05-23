CREATE DATABASE site1;

USE site1;

CREATE TABLE Books(ISBN int,Author varchar(30),Topic varchar(100),TotalStock int, Price int);

INSERT INTO site1.Books values ('1001','A.P.J. Abdul Kalam','Wings Of Fire',20,500);
INSERT INTO site1.Books values ('1002','Shivaji Sawant','Mrutyunjay',30,200);
INSERT INTO site1.Books values ('1003','Shivaji Sawant','Chhava',50,400);
INSERT INTO site1.Books values ('1004','Pu. L. Deshpande','Pulakit',10,350);
INSERT INTO site1.Books values ('1005','Pu. L. Deshpande','Purachundi',25,500);
INSERT INTO site1.Books values ('1006','Sane Guruji','Shyamchi Aai',30,400);

SELECT * FROM Books;

CREATE TABLE BookStore(Storeno int,City varchar(30),State varchar(100),ZipCode int, InventoryValue int);

INSERT INTO site1.BookStore values (1,'Sangli','Maharashtra',416416,3214);
INSERT INTO site1.BookStore values (2,'Satara','Maharashtra',415415,4512);
INSERT INTO site1.BookStore values (3,'Solapur','Maharashtra',414414,4253);
INSERT INTO site1.BookStore values (4,'Bengaluru','Karnataka',700456,8294);
INSERT INTO site1.BookStore values (5,'Pune','Maharashtra',418916,6544);

SELECT * FROM site1.BookStore;

CREATE TABLE Stock(Storeno int,ISBN varchar(30),Qty int);

INSERT INTO site1.Stock values (1,'1001',85);
INSERT INTO site1.Stock values (2,'1004',40);
INSERT INTO site1.Stock values (3,'1006',25);
INSERT INTO site1.Stock values (4,'1003',88);

SELECT * FROM site1.Stock;

CREATE DATABASE site2;

USE site2;

CREATE TABLE Books(ISBN int,Author varchar(30),Topic varchar(100),TotalStock int, Price int);

INSERT INTO site2.Books values ('1021','Shivaji Sawant','Yugandhar',40,200);
INSERT INTO site2.Books values ('1022','Ranjeet Desai','Swami',38,600);
INSERT INTO site2.Books values ('1023','Vishwas Patil','Mahanayak',75,450);
INSERT INTO site2.Books values ('1024','Daya Pawar','Baluta',15,490);
INSERT INTO site2.Books values ('1025','Laxman Mane','Upara',65,350);
INSERT INTO site2.Books values ('1026','Sudha Murty','Aayushyache Dhade Giravtana',30,480);

SELECT * FROM site2.Books;

CREATE TABLE BookStore(Storeno int,City varchar(30),State varchar(100),ZipCode int, InventoryValue int);

INSERT INTO site2.BookStore values (11,'Chittor','Andhra Pradesh',586416,1441);
INSERT INTO site2.BookStore values (12,'Deogarh','Odisha',284415,1221);
INSERT INTO site2.BookStore values (13,'Amritsar','Panjab',600414,5335);
INSERT INTO site2.BookStore values (14,'Gomati','Tripura',711456,9449);
INSERT INTO site2.BookStore values (15,'Chamoli','Uttarakhand',418586,4444);	

SELECT * FROM site2.BookStore;

CREATE TABLE Stock(Storeno int,ISBN varchar(30),Qty int);

INSERT INTO site2.Stock values (11,'1023',15);
INSERT INTO site2.Stock values (12,'1024',45);
INSERT INTO site2.Stock values (13,'1022',65);
INSERT INTO site2.Stock values (14,'1026',78);

SELECT * FROM site2.Stock;

CREATE DATABASE site3;

USE site3;

CREATE TABLE Books(ISBN int,Author varchar(30),Topic varchar(100),TotalStock int, Price int);

INSERT INTO site3.Books values ('1031','Vishnu Khandekar','Yayati',20,400);
INSERT INTO site3.Books values ('1032','Bhalchandra Nemade','Kosala',56,550);
INSERT INTO site3.Books values ('1033','Vishwas Patil','Panipat',58,350);
INSERT INTO site3.Books values ('1034','Pu. L. Deshpande','Batatyachi Chaal',86,490);
INSERT INTO site3.Books values ('1035','Achyut Godbole','Musafir',52,580);
INSERT INTO site3.Books values ('1036','Ranjit Desai','Shreeman Yogi',18,970);

SELECT * FROM site3.Books;

CREATE TABLE BookStore(Storeno int,City varchar(30),State varchar(100),ZipCode int, InventoryValue int);

INSERT INTO site3.BookStore values (21,'Balod','Chhattisgarh',416614,5751);
INSERT INTO site3.BookStore values (22,'Arwal','Bihar',415514,9821);
INSERT INTO site3.BookStore values (23,'Bokaro','Jharkhand',600006,5585);
INSERT INTO site3.BookStore values (24,'Idukki','Kerala',654456,9547);
INSERT INTO site3.BookStore values (25,'Rajkot','Gujarat',586586,9844);	

SELECT * FROM site3.BookStore;

CREATE TABLE Stock(Storeno int,ISBN varchar(30),Qty int);

INSERT INTO site3.Stock values (21,'1031',25);
INSERT INTO site3.Stock values (22,'1032',45);
INSERT INTO site3.Stock values (23,'1033',66);
INSERT INTO site3.Stock values (24,'1034',71);

SELECT * FROM site3.Stock;

USE site3;

SELECT sum(Qty) from site3.Stock;

SELECT SUM(Qty) from site2.Stock;

SELECT SUM(Qty) from site1.Stock;

USE site1;

SELECT * from site3.Books;

UPDATE site3.Books SET Price=530 where ISBN='1032';

SELECT * from site3.Books;

USE site2;

SELECT Storeno, Qty from site3.Stock where ISBN='1033';

USE site2;

SELECT * FROM site1.Books
UNION
SELECT * FROM site2.Books
UNION
SELECT * FROM site3.Books;

USE site3;

SELECT * FROM site1.BookStore
UNION
SELECT * FROM site2.BookStore
UNION
SELECT * FROM site3.BookStore;




