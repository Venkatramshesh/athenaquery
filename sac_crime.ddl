 CREATE EXTERNAL TABLE IF NOT EXISTS sacremento.sac_crime (
               ts VARCHAR(255),
               address VARCHAR(255),
               district INT,
               beat VARCHAR(255),
               grid INT,
               crimedescr VARCHAR(255),
               ucr_ncic_code INT,
               latitude FLOAT,
               longitude FLOAT
               )
               ROW FORMAT DELIMITED
               FIELDS TERMINATED BY ","
               LINES TERMINATED BY "\n"
               LOCATION 's3://awsathenademo134/crimedata/'
               TBLPROPERTIES (
               'skip.header.line.count' = '1'
               );