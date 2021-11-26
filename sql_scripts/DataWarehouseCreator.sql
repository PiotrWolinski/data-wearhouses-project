CREATE DATABASE agencyDW

USE agencyDW
GO

CREATE TABLE Department
(
	ID_Department INTEGER PRIMARY KEY,
	CallCenter BIT,
	Street varchar(100),
	Building_number INTEGER,
	City varchar(40),
	PostalCode varchar(6),
)
GO

CREATE TABLE Consultant
(
	ID_Consultant INTEGER PRIMARY KEY,
	BK_Consultant INTEGER,
	FK_DEPARTMENT INTEGER FOREIGN KEY REFERENCES Department,
	Name varchar(30),
	Surname varchar(30),
	Education varchar(20) check(Education IN ('None','Primary','Secondary','Bachelor', 'Master')),
	Experience varchar(30) check(Experience IN ('Less than a month','Less than half a year','Less than a year','Less than 3 years','More than 3 years')),
	DateCreation date,
	DateDelete date,
	BenefitsAmount varchar(10) check(BenefitsAmount IN ('0','1-2','3-4','>4')),
	EmployeeCost varchar(20) check(EmployeeCost IN ('Less than 4000','Less than 5000','Less than 7500','Less than 9000','More than 9000')),
)
GO

CREATE TABLE Consultation
(
	FK_Consultant INTEGER FOREIGN KEY REFERENCES Consultant,
	FK_Client INTEGER FOREIGN KEY REFERENCES Client,
	FK_Data INTEGER FOREIGN KEY REFERENCES Date,
	FK_StartTime INTEGER FOREIGN KEY REFERENCES Time,
	FK_EndTime INTEGER FOREIGN KEY REFERENCES Time,
	FK_Junk INTEGER FOREIGN KEY REFERENCES Junk,
	ConsultantRating INTEGER check(ConsultantRating >= 1 AND ConsultantRating <= 5),
	GeneralRating INTEGER check(GeneralRating >= 1 AND GeneralRating <= 5),
	Duration INTEGER check(Duration > 0 AND Duration <= 60 * 60 * 8),
	ID_Survey INTEGER,
	PRIMARY KEY(FK_Consultant, FK_Client, FK_Data, FK_StartTime, FK_EndTime, FK_Junk)
)
GO

CREATE TABLE Junk
(
	ID_Junk INTEGER PRIMARY KEY,
	Duration varchar(50) check(Duration IN ('Less than 5 minutes','5-10 minutes','10-20 minutes','20-30 minutes','More than 30 minutes')),
)
GO

CREATE TABLE Client
(
	ID_Client INTEGER PRIMARY KEY,
	Name varchar(30),
	Surname varchar(40),
)
GO

CREATE TABLE Date
(
	ID_Date INTEGER PRIMARY KEY,
	Date date,
	Year INTEGER,
	Month varchar(20) check(Month in ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')),
	MonthNo INTEGER check(MonthNo >= 1 AND MonthNo <= 12),
	DayOfTheWeek varchar(30) check(DayOfTheWeek in ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')),
	DayOfTheWeekNo INTEGER check(DayOfTheWeekNo >= 1 AND DayOfTheWeekNo <= 7),
)
GO

CREATE TABLE Time
(
	ID_Time INTEGER PRIMARY KEY,
	Hour INTEGER check (Hour >= 0 AND Hour <= 23),
	Minute INTEGER check (Minute >= 0 AND Minute <= 60),
	Second INTEGER check (Second >= 0 AND Second <= 60),
)
GO