USE agencyDW
GO

IF (object_id('dbo.ConsultantTemp') IS NOT NULL) DROP TABLE dbo.ConsultantTemp;
CREATE TABLE dbo.ConsultantTemp(ID INTEGER, Department INTEGER, Name VARCHAR(50), Surname VARCHAR(50), BirthDate DATE, Education VARCHAR(20), Position VARCHAR(50), Salary FLOAT, DateOfEmployment DATE, DateOfDismissal DATE);
GO

BULK INSERT dbo.ConsultantTemp
    FROM 'C:\Users\mkuczynski11\Desktop\studia\5_sem\Hurtownie Danych\data-wearhouses-project\ceo_excel.csv'
    WITH
    (
        FIRSTROW = 2,
        CODEPAGE = '65001',
        FIELDTERMINATOR = ',', 
        ROWTERMINATOR = '0x0a'
    )

IF (object_id('vETLDimConsultantData') IS NOT NULL) DROP VIEW vETLDimConsultantData;
GO
CREATE VIEW vETLDimConsultantData
AS
SELECT
    t1.[ID],
    t2.[ID_Department],
	t3.[Consultant_name],
    t3.[Consultant_surname],
    t1.[Education],
	CASE
		WHEN t1.[DateOfDismissal] > t1.[DateOfEmployment] THEN CASE	
			WHEN DATEDIFF(month, t1.[DateOfEmployment], t1.[DateOfDismissal]) < 1 THEN 'Less than a month'
			WHEN DATEDIFF(month, t1.[DateOfEmployment], t1.[DateOfDismissal]) < 6 THEN 'Less than half a year'
			WHEN DATEDIFF(year, t1.[DateOfEmployment], t1.[DateOfDismissal]) < 1 THEN 'Less than a year'
			WHEN DATEDIFF(year, t1.[DateOfEmployment], t1.[DateOfDismissal]) < 3 THEN 'Less than 3 years'
			ELSE 'More than 3 years'
			END
		ELSE CASE
			WHEN DATEDIFF(month, t1.[DateOfEmployment], CURRENT_TIMESTAMP) < 1 THEN 'Less than a month'
			WHEN DATEDIFF(month, t1.[DateOfEmployment], CURRENT_TIMESTAMP) < 6 THEN 'Less than half a year'
			WHEN DATEDIFF(year, t1.[DateOfEmployment], CURRENT_TIMESTAMP) < 1 THEN 'Less than a year'
			WHEN DATEDIFF(year, t1.[DateOfEmployment], CURRENT_TIMESTAMP) < 3 THEN 'Less than 3 years'
			ELSE 'More than 3 years'
			END
    END AS [Experience],
	CASE
		WHEN (SELECT COUNT(FK_Consultant) FROM Talk2Us.dbo.Benefit WHERE FK_Consultant = ID AND Start_time <= '2021-06-06' AND End_time >= '2021-06-06') = 0 THEN '0'	--podmienic date
		WHEN (SELECT COUNT(FK_Consultant) FROM Talk2Us.dbo.Benefit WHERE FK_Consultant = ID AND Start_time <= '2021-06-06' AND End_time >= '2021-06-06') < 3 THEN '1-2'	--podmienic date
		WHEN (SELECT COUNT(FK_Consultant) FROM Talk2Us.dbo.Benefit WHERE FK_Consultant = ID AND Start_time <= '2021-06-06' AND End_time >= '2021-06-06') < 5 THEN '3-4'	--podmienic date
		ELSE '>4'
	END AS [BenefitsAmount],
	CASE
		WHEN COALESCE((SELECT SUM(Employer_cost) FROM Talk2Us.dbo.Benefit WHERE FK_Consultant = ID AND Start_time <= '2021-06-06' AND End_time >= '2021-06-06'),0) + t1.[Salary] < 4000 THEN 'Less than 4000'		--podmienic date
		WHEN COALESCE((SELECT SUM(Employer_cost) FROM Talk2Us.dbo.Benefit WHERE FK_Consultant = ID AND Start_time <= '2021-06-06' AND End_time >= '2021-06-06'),0) + t1.[Salary] < 5000 THEN 'Less than 5000'		--podmienic date
		WHEN COALESCE((SELECT SUM(Employer_cost) FROM Talk2Us.dbo.Benefit WHERE FK_Consultant = ID AND Start_time <= '2021-06-06' AND End_time >= '2021-06-06'),0) + t1.[Salary] < 7500 THEN 'Less than 7500'		--podmienic date
		WHEN COALESCE((SELECT SUM(Employer_cost) FROM Talk2Us.dbo.Benefit WHERE FK_Consultant = ID AND Start_time <= '2021-06-06' AND End_time >= '2021-06-06'),0) + t1.[Salary] < 9000 THEN 'Less than 9000'		--podmienic date
		ELSE 'More than 9000'
	END AS [EmployerCost]
FROM dbo.ConsultantTemp AS t1
JOIN dbo.Department AS t2 ON t2.BK_Department = t1.Department
JOIN [Talk2Us].dbo.[Consultant] AS t3 ON t3.ID_Consultant = t1.ID
WHERE t1.[Position] = 'Consultant'
;
GO

MERGE INTO Consultant as TT
	USING vETLDimConsultantData as ST
		ON TT.BK_Consultant = ST.[ID]
			WHEN NOT MATCHED
				THEN
					INSERT
					VALUES (
					ST.[ID],
					ST.[ID_Department],
					ST.[Consultant_name],
					ST.[Consultant_surname],
					ST.[Education],
					ST.[Experience],
					CURRENT_TIMESTAMP,
					NULL,
					ST.[BenefitsAmount],
					ST.[EmployerCost]
					)
			WHEN MATCHED
				AND (ST.[ID_Department] <> TT.FK_DEPARTMENT
				OR ST.[Consultant_name] <> TT.Name
				OR ST.[Consultant_surname] <> TT.Surname
				OR ST.[Education] <> TT.Education
				OR ST.[Experience] <> TT.Experience
				OR ST.[BenefitsAmount] <> TT.BenefitsAmount
				OR ST.[EmployerCost] <> TT.EmployerCost)
				THEN
					UPDATE
					SET TT.DateDelete = CURRENT_TIMESTAMP
			WHEN NOT MATCHED BY Source
			AND TT.BK_Consultant != -1
			THEN
				UPDATE
				SET TT.DateDelete = CURRENT_TIMESTAMP
			;

-- INSERTING CHANGED ROWS TO THE DIMSELLER TABLE
INSERT INTO Consultant
SELECT ID, ID_Department, Consultant_name, Consultant_surname, Education, Experience, CURRENT_TIMESTAMP, NULL, BenefitsAmount, EmployerCost FROM vETLDimConsultantData
EXCEPT SELECT BK_Consultant, FK_DEPARTMENT, Name, Surname, Education, Experience, CURRENT_TIMESTAMP, NULL, BenefitsAmount, EmployerCost FROM Consultant


DROP TABLE dbo.ConsultantTemp;
DROP VIEW vETLDimConsultantData;
