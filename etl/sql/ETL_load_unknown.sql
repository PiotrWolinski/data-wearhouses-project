USE agencyDW
GO

SET IDENTITY_INSERT dbo.Client ON;
GO 

INSERT INTO dbo.Client
VALUES(-1, -1, 'UNKNOWN', 'UNKNOWN');

INSERT INTO dbo.Department
VALUES(-1, -1, 0, 'UNKNOWN', -1, 'UNKNOWN', '00-000');

INSERT INTO dbo.Consultant
VALUES(-1, -1, -1, 'UNKNOWN', 'UNKNOWN', 'None', 'Less than a month', NULL, NULL, '0', 'Less than 4000');
GO
