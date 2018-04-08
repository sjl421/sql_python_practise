from .base import DB


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
  quality VARCHAR(10),
  so2 INT not NULL,
  so2_24h INT not NULL,
  time_point DATETIME not NULL,
  CONSTRAINT UNIQUE (position_id, time_point)
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
  so2,
  so2_24h,
  time_point
) VALUES (
  %s, (SELECT id from city WHERE name=%s),
  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
  %s, (SELECT id from station WHERE station_name=%s and station_code=%s AND city_id=(SELECT id from city WHERE name=%s)), %s, %s, %s, %s, %s
);
'''

SELECT_FROM_CITY_AQI = '''
SELECT 
  aqi,
  (SELECT name from city WHERE id=city_id),
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
  (SELECT DATE_FORMAT(time_point, '%Y-%m-%d %H:%i:%S'))
FROM city_aqi WHERE city_id=(SELECT id from city WHERE name='{}');
'''

SELECT_ALL_FROM_CITY_AQI = '''
SELECT 
  aqi,
  (SELECT name from city WHERE id=city_id),
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
  (SELECT DATE_FORMAT(time_point, '%Y-%m-%d %H:%i:%S'))
FROM city_aqi;
'''

SELECT_FROM_STATION_AQI_WHEN_CITY = '''
SELECT 
  aqi,
  (SELECT name from city WHERE id=city_id),
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
  (SELECT station_name from station WHERE id=position_id),
  primary_pollutant,
  quality,
  so2,
  so2_24h,
  (SELECT DATE_FORMAT(time_point, '%Y-%m-%d %H:%i:%S'))
FROM station_aqi WHERE city_id=(SELECT id FROM city WHERE name='{}');
'''

SELECT_ALL_FROM_STATION_AQI = '''
SELECT 
  aqi,
  (SELECT name from city WHERE id=city_id),
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
  (SELECT station_name from station WHERE id=position_id),
  primary_pollutant,
  quality,
  so2,
  so2_24h,
  (SELECT DATE_FORMAT(time_point, '%Y-%m-%d %H:%i:%S'))
FROM station_aqi;
'''


def create_table_city_aqi():
    db = DB()
    db.execute_create_or_drop(CREATE_TABLE_CITY_AQI)


def drop_table_city_aqi():
    db = DB()
    db.execute_create_or_drop(DROP_TABLE_CITY_AQI)


def insert_into_city_aqi(param):
    db = DB()
    db.execute_insert(INSERT_INTO_TABLE_CITY_AQI)


def insert_many_into_city_aqi(params):
    db = DB()
    return db.executemany_insert(INSERT_INTO_TABLE_CITY_AQI, params)


def create_table_station_aqi():
    db = DB()
    db.execute_create_or_drop(CREATE_TABLE_STATION_AQI)


def drop_table_station_aqi():
    db = DB()
    db.execute_create_or_drop(DROP_TABLE_STATION_AQI)


def insert_many_into_station_aqi(params):
    db = DB()
    return db.executemany_insert(INSERT_INTO_TABLE_STATION_AQI, params)


def select_from_city_aqi(city):
    db = DB()
    return db.execute_select_all(SELECT_FROM_CITY_AQI.format(city))


def select_all_from_city_aqi():
    db = DB()
    return db.execute_select_all(SELECT_ALL_FROM_CITY_AQI)


def select_from_station_aqi(city=None):
    db = DB()
    if city:
        return db.execute_select_all(SELECT_FROM_STATION_AQI_WHEN_CITY.format(city))
    else:
        return db.execute_select_all(SELECT_FROM_CITY_AQI.format(city))


def select_all_from_city_aqi():
    db = DB()
    return db.execute_select_all(SELECT_ALL_FROM_STATION_AQI)
