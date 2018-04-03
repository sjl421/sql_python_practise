from .base import *


CREATE_TABLE_CITY_AQI = '''
CREATE TABLE IF NOT EXISTS city_aqi (
  id INT PRIMARY KEY auto_increment,
  aqi INT not NULL,
  city_id INT not NULL,
  co FLOAT not NULL,
  co_24h FLOAT not NULL,
  no2 INT not NULL,
  no2_24h INT not NULL,
  o3 INT not NULL,
  o3_24h INT not NULL,
  o3_8h INT not NULL,
  o3_8h_24h INT not NULL,
  pm10 INT not NULL,
  pm10_24h INT not NULL,
  pm2_5 INT not NULL,
  pm2_5_24h INT not NULL,
  position_id INT not NULL,
  primary_pollutant VARCHAR(100),
  quality VARCHAR(10) not NULL,
  level VARCHAR(10) not NULL,
  so2 INT not NULL,
  so2_24h INT not NULL,
  time_point DATETIME not NULL
) DEFAULT CHARACTER SET utf8mb4;
'''

DROP_TABLE_CITY = '''
DROP TABLE city;
'''

INSERT_INTO_TABLE_CITY = '''
INSERT INTO city (
  name
) VALUES (
  %s
);
'''

SELECT_FROM_CITY = '''
SELECT * FROM city;
'''

SELECT_FROM_CITY_WHERE_NAME = '''
SELECT * FROM city WHERE name='{}';
'''