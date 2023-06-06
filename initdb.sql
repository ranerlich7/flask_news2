CREATE TABLE Cars (
    ID int  NOT NULL PRIMARY KEY,
    Plate varchar(255) NOT NULL
);

INSERT INTO Cars (ID, Plate)
VALUES (1, '22-33-44'), 
(2, '44-553-664'),
(3, '99-33-49994');

CREATE TABLE Service (
    ID int NOT NULL PRIMARY KEY,
    service_type varchar(50) NOT NULL,
    CarID int,
    FOREIGN KEY (CarID) REFERENCES Cars(ID)
);



INSERT INTO Service (ID, service_type, CarID)
VALUES (11, '10,000',3), 
(22, 'oil change',3),
(33, 'breaks',3);


 INSERT INTO article (title, content, image,category) VALUES ('Manchester City gets Messi', 'bla bla MEssi ... bla', 'https://picsum.photos/401/300','Sports')