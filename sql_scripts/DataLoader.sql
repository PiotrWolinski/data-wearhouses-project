USE Talk2Us

BULK INSERT dbo.Client
FROM 'C:\Users\mkuczynski11\Desktop\studia\5_sem\Hurtownie Danych\data-wearhouses-project\bulks\clients.bulk'
WITH 
  (
    CODEPAGE = '65001',
    FIELDTERMINATOR = '|', 
    ROWTERMINATOR = '0x0a' 
  )

BULK INSERT dbo.Rating_type
FROM 'C:\Users\mkuczynski11\Desktop\studia\5_sem\Hurtownie Danych\data-wearhouses-project\bulks\rating_types.bulk'
WITH 
  (
    CODEPAGE = '65001',
    FIELDTERMINATOR = '|', 
    ROWTERMINATOR = '0x0a' 
  )

BULK INSERT dbo.Department
FROM 'C:\Users\mkuczynski11\Desktop\studia\5_sem\Hurtownie Danych\data-wearhouses-project\bulks\departments.bulk'
WITH 
  (
    CODEPAGE = '65001',
    FIELDTERMINATOR = '|', 
    ROWTERMINATOR = '0x0a' 
  )

BULK INSERT dbo.Consultant
FROM 'C:\Users\mkuczynski11\Desktop\studia\5_sem\Hurtownie Danych\data-wearhouses-project\bulks\consultants.bulk'
WITH 
  (
    CODEPAGE = '65001',
    FIELDTERMINATOR = '|', 
    ROWTERMINATOR = '0x0a' 
  )

BULK INSERT dbo.Consultation
FROM 'C:\Users\mkuczynski11\Desktop\studia\5_sem\Hurtownie Danych\data-wearhouses-project\bulks\consultations.bulk'
WITH 
  (
    CODEPAGE = '65001',
    FIELDTERMINATOR = '|', 
    ROWTERMINATOR = '0x0a' 
  )

BULK INSERT dbo.Survey
FROM 'C:\Users\mkuczynski11\Desktop\studia\5_sem\Hurtownie Danych\data-wearhouses-project\bulks\surveys.bulk'
WITH 
  (
    CODEPAGE = '65001',
    FIELDTERMINATOR = '|', 
    ROWTERMINATOR = '0x0a' 
  )

BULK INSERT dbo.Rating
FROM 'C:\Users\mkuczynski11\Desktop\studia\5_sem\Hurtownie Danych\data-wearhouses-project\bulks\ratings.bulk'
WITH 
  (
    CODEPAGE = '65001',
    FIELDTERMINATOR = '|', 
    ROWTERMINATOR = '0x0a' 
  )

BULK INSERT dbo.Benefit
FROM 'C:\Users\mkuczynski11\Desktop\studia\5_sem\Hurtownie Danych\data-wearhouses-project\bulks\benefits.bulk'
WITH 
  (
    CODEPAGE = '65001',
    FIELDTERMINATOR = '|', 
    ROWTERMINATOR = '0x0a' 
  )