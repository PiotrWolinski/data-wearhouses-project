USE Talk2Us

INSERT INTO dbo.Client values('Martin', 'Kuczynski');
INSERT INTO dbo.Client values('Piotr', 'Wolinski');
INSERT INTO dbo.Client values('Adam', 'Kowalski');
INSERT INTO dbo.Client values('Wiktor', 'Krawczyk');
INSERT INTO dbo.Client values('Kacper', 'Kotlownia');
INSERT INTO dbo.Client values('Mateusz', 'Kacperski');
INSERT INTO dbo.Client values('Anna', 'Wilczynska');
INSERT INTO dbo.Client values('Wiktoria', 'Urbanik');
INSERT INTO dbo.Client values('Zuzanna', 'Nawrocka');
INSERT INTO dbo.Client values('Joanna', 'Kawczynska');

INSERT INTO dbo.Consultation values(1, 100001, '20211025 10:21:22 AM', '20211025 10:31:29 AM', 'feedback');
INSERT INTO dbo.Consultation values(1, 100002, '20211025 10:32:22 AM', '20211025 10:57:11 AM', 'offer question');
INSERT INTO dbo.Consultation values(1, 100003, '20211026 9:12:42 AM', '20211026 9:22:12 AM', 'feedback');
INSERT INTO dbo.Consultation values(1, 100004, '20211026 13:22:11 AM', '20211026 13:25:17 AM', 'offer question');
INSERT INTO dbo.Consultation values(1, 100005, '20211026 10:10:34 AM', '20211026 10:21:29 AM', 'feedback');
INSERT INTO dbo.Consultation values(1, 100006, '20211026 10:32:22 AM', '20211026 10:57:11 AM', 'offer question');
INSERT INTO dbo.Consultation values(1, 100007, '20211026 13:21:22 AM', '20211026 13:31:29 AM', 'feedback');
INSERT INTO dbo.Consultation values(1, 100008, '20211026 14:48:22 AM', '20211026 14:57:11 AM', 'offer question');

INSERT INTO dbo.Survey values(0, 1000001, 5);
INSERT INTO dbo.Survey values(0, 1000002, 4);
INSERT INTO dbo.Survey values(1, 1000003, 5);
INSERT INTO dbo.Survey values(0, 1000004, 3);
INSERT INTO dbo.Survey values(1, 1000005, 4);
INSERT INTO dbo.Survey values(0, 1000006, 2);

INSERT INTO dbo.Rating values(600001, 'consultant rating', 5);

INSERT INTO dbo.Rating values(600002, 'consultant rating', 5);
INSERT INTO dbo.Rating values(600002, 'solution rating', 5);
INSERT INTO dbo.Rating values(600003, 'consultant rating', 5);
INSERT INTO dbo.Rating values(600003, 'solution rating', 5);

UPDATE dbo.Consultant
SET Consultant_surname = 'Kuczynski'
WHERE ID_Consultant = 1;

UPDATE dbo.Benefit
SET Employer_cost = 400, Employee_cost = 10
WHERE Benefit_name = 'Macbook Air';

UPDATE dbo.Department
SET City = 'Hel', Street = 'Wielka', Building_number = 1
WHERE ID_Department = 1;

UPDATE dbo.Consultant
SET Consultant_name = 'Antoni'
WHERE ID_Consultant = 1;
