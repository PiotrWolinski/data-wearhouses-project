USE agencyDW
GO

INSERT INTO dbo.Junk
values(1, 'Less than 5 minutes')
INSERT INTO dbo.Junk
values(2, '5-10 minutes')
INSERT INTO dbo.Junk
values(3, '10-20 minutes')
INSERT INTO dbo.Junk
values(4, '20-30 minutes')
INSERT INTO dbo.Junk
values(5, 'More than 30 minutes')

INSERT INTO dbo.Client
values(1,'Andrzej', 'Winiary')
INSERT INTO dbo.Client
values(2,'Tymoteusz', 'Pudliszki')
INSERT INTO dbo.Client
values(3,'Walery', 'Witold')
INSERT INTO dbo.Client
values(4,'Monika', 'Blaszka')
INSERT INTO dbo.Client
values(5,'Alojzy', 'Mirek')
INSERT INTO dbo.Client
values(6,'Andrzej', 'Waleczny')
INSERT INTO dbo.Client
values(7,'Martin', 'Kuczyñski')
INSERT INTO dbo.Client
values(8,'Piotr', 'Woliñski')
INSERT INTO dbo.Client
values(9,'Michal', 'Flakowski')

INSERT INTO	dbo.Date
values(1,'2020-11-12', 2020, 'November', 11, 'Thursday', 4)
INSERT INTO	dbo.Date
values(2,'2021-11-12', 2021, 'November', 11, 'Friday', 5)
INSERT INTO	dbo.Date
values(3,'2021-06-07', 2021, 'June', 6, 'Monday', 1)

INSERT INTO dbo.Time
values(1, 8, 20, 30)
INSERT INTO dbo.Time
values(2, 8, 40, 12)
INSERT INTO dbo.Time
values(3, 9, 30, 1)
INSERT INTO dbo.Time
values(4, 10, 13, 14)
INSERT INTO dbo.Time
values(5, 11, 16, 19)
INSERT INTO dbo.Time
values(6, 15, 14, 0)
INSERT INTO dbo.Time
values(7, 14, 12, 10)
INSERT INTO dbo.Time
values(8, 13, 14, 14)
INSERT INTO dbo.Time
values(9, 10, 0, 0)
INSERT INTO dbo.Time
values(10, 8, 45, 5)

INSERT INTO Department (ID_Department, CallCenter, Street, Building_number, City, PostalCode)
VALUES (1, 1, 'Ogrodowa', 42, 'Gdañsk', '83-143');
INSERT INTO Department (ID_Department, CallCenter, Street, Building_number, City, PostalCode)
VALUES (2, 1, 'Grunwaldzka', 123, 'Gdañsk', '83-041');

INSERT INTO Consultant (ID_Consultant, BK_Consultant, FK_DEPARTMENT, Name, Surname, Education, Experience, DateCreation, DateDelete, BenefitsAmount, EmployeeCost)
VALUES (1, 1, 1, 'Johny', 'Bravo', 'Bachelor', 'More than 3 years', '2018-07-12', Null, '0', 'Less than 4000');
INSERT INTO Consultant (ID_Consultant, BK_Consultant, FK_DEPARTMENT, Name, Surname, Education, Experience, DateCreation, DateDelete, BenefitsAmount, EmployeeCost)
VALUES (2, 2, 1, 'Michael', 'Smith', 'Bachelor', 'Less than 3 years', '2019-11-21', Null, '1-2', 'Less than 4000');
INSERT INTO Consultant (ID_Consultant, BK_Consultant, FK_DEPARTMENT, Name, Surname, Education, Experience, DateCreation, DateDelete, BenefitsAmount, EmployeeCost)
VALUES (3, 3, 1, 'Victoria', 'Anderson', 'Secondary', 'Less than half a year', '2021-07-12', Null, '0', 'Less than 4000');
INSERT INTO Consultant (ID_Consultant, BK_Consultant, FK_DEPARTMENT, Name, Surname, Education, Experience, DateCreation, DateDelete, BenefitsAmount, EmployeeCost)
VALUES (4, 4, 2, 'Vincent', 'Cage', 'Master', 'More than 3 years', '2011-03-02', Null, '1-2', 'Less than 7500');
INSERT INTO Consultant (ID_Consultant, BK_Consultant, FK_DEPARTMENT, Name, Surname, Education, Experience, DateCreation, DateDelete, BenefitsAmount, EmployeeCost)
VALUES (5, 5, 2, 'Laura', 'Spiegel', 'None', 'Less than a year', '2020-12-03', Null, '0', 'Less than 5000');
INSERT INTO Consultant (ID_Consultant, BK_Consultant, FK_DEPARTMENT, Name, Surname, Education, Experience, DateCreation, DateDelete, BenefitsAmount, EmployeeCost)
VALUES (6, 6, 2, 'Peter', 'Decker', 'Bachelor', 'Less than half a year', '2020-11-02', '2021-07-12', '0', 'Less than 4000');
INSERT INTO Consultant (ID_Consultant, BK_Consultant, FK_DEPARTMENT, Name, Surname, Education, Experience, DateCreation, DateDelete, BenefitsAmount, EmployeeCost)
VALUES (7, 7, 2, 'Albert', 'Wick', 'Primary', 'Less than a year', '2021-01-07', Null, '0', 'Less than 4000');


INSERT INTO Consultation (FK_Consultant, FK_Client, FK_Data, FK_StartTime, FK_EndTime, FK_Junk, ConsultantRating, GeneralRating, Duration, ID_Survey)
VALUES (1, 1, 1, 1, 2, 1, 5, 4, 247, Null);
INSERT INTO Consultation (FK_Consultant, FK_Client, FK_Data, FK_StartTime, FK_EndTime, FK_Junk, ConsultantRating, GeneralRating, Duration, ID_Survey)
VALUES (2, 2, 2, 2, 3, 2, 3, 2, 75, 1);
INSERT INTO Consultation (FK_Consultant, FK_Client, FK_Data, FK_StartTime, FK_EndTime, FK_Junk, ConsultantRating, GeneralRating, Duration, ID_Survey)
VALUES (2, 2, 3, 3, 4, 3, 5, 5, 804, Null);
INSERT INTO Consultation (FK_Consultant, FK_Client, FK_Data, FK_StartTime, FK_EndTime, FK_Junk, ConsultantRating, GeneralRating, Duration, ID_Survey)
VALUES (3, 2, 1, 4, 5, 4, 4, 3, 32, 2);
INSERT INTO Consultation (FK_Consultant, FK_Client, FK_Data, FK_StartTime, FK_EndTime, FK_Junk, ConsultantRating, GeneralRating, Duration, ID_Survey)
VALUES (4, 4, 2, 5, 6, 1, 5, 5, 1232, 3);
INSERT INTO Consultation (FK_Consultant, FK_Client, FK_Data, FK_StartTime, FK_EndTime, FK_Junk, ConsultantRating, GeneralRating, Duration, ID_Survey)
VALUES (4, 5, 3, 6, 7, 2, 3, 4, 912, Null);
INSERT INTO Consultation (FK_Consultant, FK_Client, FK_Data, FK_StartTime, FK_EndTime, FK_Junk, ConsultantRating, GeneralRating, Duration, ID_Survey)
VALUES (6, 6, 1, 7, 8, 3, 4, 4, 174, 4);
INSERT INTO Consultation (FK_Consultant, FK_Client, FK_Data, FK_StartTime, FK_EndTime, FK_Junk, ConsultantRating, GeneralRating, Duration, ID_Survey)
VALUES (6, 6, 2, 8, 9, 4, 5, 5, 342, Null);
INSERT INTO Consultation (FK_Consultant, FK_Client, FK_Data, FK_StartTime, FK_EndTime, FK_Junk, ConsultantRating, GeneralRating, Duration, ID_Survey)
VALUES (7, 7, 3, 9, 10, 1, 5, 4, 293, Null);
INSERT INTO Consultation (FK_Consultant, FK_Client, FK_Data, FK_StartTime, FK_EndTime, FK_Junk, ConsultantRating, GeneralRating, Duration, ID_Survey)
VALUES (7, 8, 1, 10, 1, 2, 2, 2, 127, Null);

SELECT * FROM Consultation