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
  primary_pollutant VARCHAR(100),
  quality VARCHAR(10) not NULL,
  level VARCHAR(10) not NULL,
  so2 INT not NULL,
  so2_24h INT not NULL,
  time_point DATETIME not NULL,
  CONSTRAINT UNIQUE (city_id, time_point)
) DEFAULT CHARACTER SET utf8mb4;
'''

CREATE_TABLE_STATION_AQI = '''
CREATE TABLE IF NOT EXISTS station_aqi (
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

DROP_TABLE_CITY_AQI = '''
DROP TABLE city_aqi;
'''

DROP_TABLE_STATION_AQI = '''
DROP TABLE station_aqi;
'''

INSERT_INTO_TABLE_CITY_AQI = '''
INSERT INTO city_aqi (
  aqi,
  city_id,
  co,
  co_24h,
  no2,
  no2_24h,
  o3,
  o3_24h,
  o3_8h,
  o3_8h_24h,
  pm10,
  pm10_24h,
  pm2_5,
  pm2_5_24h,
  primary_pollutant,
  quality,
  level,
  so2,
  so2_24h,
  time_point
) VALUES (
  %s, (SELECT id from city WHERE name=%s),
  %s, %s, %s, %s, %s, %s, %s, %s,
  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
);
'''

INSERT_INTO_TABLE_STATION_AQI = '''
INSERT INTO station_aqi (
  aqi,
  city_id,
  co,
  co_24h,
  no2,
  no2_24h,
  o3,
  o3_24h,
  o3_8h,
  o3_8h_24h,
  pm10,
  pm10_24h,
  pm2_5,
  pm2_5_24h,
  position_id,
  primary_pollutant,
  quality,
  level,
  so2,
  so2_24h,
  time_point
) VALUES (
  %s, (SELECT id from city WHERE name=%s),
  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
  %s, (SELECT id from station WHERE station_name=%s), %s, %s, %s, %s, %s, %s
);
'''


def create_table_city_aqi(conn):
    execute_create_or_drop(conn, CREATE_TABLE_CITY_AQI)


def drop_table_city_aqi(conn):
    execute_create_or_drop(conn, DROP_TABLE_CITY_AQI)


def insert_into_city_aqi(conn, param):
    execute_insert(conn, INSERT_INTO_TABLE_CITY_AQI)


def insert_many_into_city_aqi(conn, params):
    return executemany_insert(conn, INSERT_INTO_TABLE_CITY_AQI, params)
