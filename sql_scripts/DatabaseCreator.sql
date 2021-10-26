CREATE DATABASE Talk2Us
GO

USE Talk2Us
GO

CREATE TABLE Rating_type
(
    Rating_type_name varchar(30) PRIMARY KEY,
)
GO

CREATE TABLE Client
(
    ID_Client INTEGER IDENTITY(1,1) PRIMARY KEY,
    Client_name varchar(30),
    Client_surname varchar(40),
)
GO

CREATE TABLE Department
(
    ID_Department INTEGER IDENTITY(1,1) PRIMARY KEY,
    Street varchar(100),
    Building_number INTEGER,
    City varchar(40),
    Postal_code varchar(6),
    Consultant_count INTEGER,
    Call_center BIT,
)
GO

CREATE TABLE Consultant
(
    ID_Consultant INTEGER IDENTITY(1,1) PRIMARY KEY,
    FK_Department INTEGER FOREIGN KEY REFERENCES Department,
    Consultant_name varchar(30),
    Consultant_surname varchar(40),
)
GO

CREATE TABLE Consultation
(
    ID_Consultation INTEGER IDENTITY(1,1) PRIMARY KEY,
    FK_Consultant INTEGER FOREIGN KEY REFERENCES Consultant,
    FK_Client INTEGER FOREIGN KEY REFERENCES Client,
    Start_time DATETIME,
    End_time DATETIME,
    Topic varchar(40),
)
GO

CREATE TABLE Survey
(
    ID_Survey INTEGER IDENTITY(1,1) PRIMARY KEY,
    Reward_available BIT,
    FK_Consultation INTEGER FOREIGN KEY REFERENCES Consultation,
    Overall_rating INTEGER,
)
GO

CREATE TABLE Rating
(
    ID_Rating INTEGER IDENTITY(1,1) PRIMARY KEY,
    FK_Survey INTEGER FOREIGN KEY REFERENCES Survey,
    FK_Rating_type varchar(30) FOREIGN KEY REFERENCES Rating_type,
    Rating_value INTEGER,
)
GO

CREATE TABLE Benefit
(
    ID_Benefit INTEGER IDENTITY(1,1) PRIMARY KEY,
    Benefit_name varchar(60),
    Benefit_type varchar(40),
    Start_time DATE,
    End_time DATE,
    Employer_cost FLOAT,
    Employee_cost FLOAT,
    FK_Consultant INTEGER FOREIGN KEY REFERENCES Consultant,
)
GO