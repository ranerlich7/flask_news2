
INSERT INTO Cars ( 'CarID','Plate','PersonID') VALUES (11,'22-33-44',2),(22,'444-555',1);

INSERT INTO Cars ( 'CarID','Plate','PersonID') VALUES (11,'22-33-44',2),(22,'444-555',1);

SELECT Cars.CARID, Cars.PLATE, Persons.FirstName FROM [Cars]
INNER JOIN Persons ON Persons.ID = Cars.PersonID;

CREATE TABLE Persons (
    Personid int NOT NULL AUTO_INCREMENT,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    PRIMARY KEY (Personid)
);

תרגיל 1:
לצור טבלת מכוניות
CARS: CAR_ID, PLATE
ולהכניס 3 רשומות

תרגיל 2
לבנות 2 טבלאות 
service: T_ID, CAR_ID, service_TYPE
CARS: CAR_ID, PLATE
תשתמשו ב-PRIMARY KEY 
FOREIGN KEY

להכניס לכל אחת 3 נתונים
insert 3 cars, 3 service

לעשות שאילתא עם JOIN
שהתוצאה שלה היא
CAR_ID, service_TYPE, PLATE 

------------------------------

CREATE TABLE Cars (
    ID int  NOT NULL PRIMARY KEY,
    Plate varchar(255) NOT NULL
);