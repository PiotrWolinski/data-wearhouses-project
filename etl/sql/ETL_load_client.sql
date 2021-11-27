USE agencyDW
GO

IF (object_id('vETLDimClientData') IS NOT NULL) DROP VIEW vETLDimClientData
GO
CREATE VIEW vETLDimClientData
AS
SELECT DISTINCT
	[ID_Client],
    [Client_name],
    [Client_surname]
FROM [Talk2Us].dbo.[Client]
;
GO

MERGE INTO Client AS TT
    USING vETLDimClientData AS ST
	ON TT.BK_Client = ST.[ID_Client]
    AND TT.Name = ST.[Client_name]
    AND TT.Surname = ST.[Client_surname]
        WHEN NOT Matched
            THEN
                INSERT
                VALUES (
					ST.[ID_Client],
                    ST.[Client_name],
                    ST.[Client_surname]
                )
        WHEN NOT MATCHED BY Source
            THEN
                DELETE
        ;

DROP VIEW vETLDimClientData
