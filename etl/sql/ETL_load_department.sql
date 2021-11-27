USE agencyDW
GO

IF (object_id('vETLDimDeparmentData') IS NOT NULL) DROP VIEW vETLDimDeparmentData
GO
CREATE VIEW vETLDimDeparmentData
AS
SELECT DISTINCT
    [ID_Department],
    [Call_center],
    [Street],
    [Building_number],
    [City],
    [Postal_code]
FROM [Talk2Us].dbo.[Department]
;
GO

MERGE INTO Department AS TT
    USING vETLDimDeparmentData AS ST
        ON TT.BK_Department = ST.[ID_Department]
        AND TT.CallCenter = ST.[Call_center]
        AND TT.Street = ST.[Street]
        AND TT.Building_number = ST.[Building_number]
        AND TT.City = ST.[City]
        AND TT.PostalCode = ST.[Postal_code]
            WHEN NOT Matched
                THEN
                    INSERT
                    Values (
                        ST.[ID_Department],
                        ST.[Call_center],
                        ST.[Street],
                        ST.[Building_number],
                        ST.[City],
                        ST.[Postal_code]
                    )
            WHEN NOT MATCHED BY Source
                THEN
                    DELETE
            ;

DROP VIEW vETLDimDeparmentData
