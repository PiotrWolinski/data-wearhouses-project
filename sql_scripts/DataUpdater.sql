USE Talk2Us

INSERT INTO dbo.Client values('Martin', 'Kuczynski');
INSERT INTO dbo.Client values('Piotr', 'Wolinski');

INSERT INTO dbo.Consultation values(1, 100001, '20211025 10:21:22 AM', '20211025 10:31:29 AM', 'feedback');
INSERT INTO dbo.Consultation values(1, 100002, '20211025 10:32:22 AM', '20211025 10:57:11 AM', 'offer question');

INSERT INTO dbo.Survey values(0, 1000001, 5);
INSERT INTO dbo.Survey values(0, 1000002, 5);

INSERT INTO dbo.Rating values(600001, 'consultant rating', 5);

INSERT INTO dbo.Rating values(600002, 'consultant rating', 5);
INSERT INTO dbo.Rating values(600002, 'solution rating', 5);

UPDATE dbo.Consultant
SET Consultant_surname = 'Kuczynski'
WHERE ID_Consultant = 1;

UPDATE dbo.Benefit
SET Employer_cost = 400, Employee_cost = 10
WHERE Benefit_name = 'Macbook Air';