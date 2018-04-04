from .base import *


CREATE_TABLE_STATION = '''
CREATE TABLE IF NOT EXISTS station (
  id INT PRIMARY KEY auto_increment,
  station_name VARCHAR(50) not NULL,
  station_code VARCHAR(10) not NULL,
  city_id INT not NULL,
  KEY city_id (city_id),
  CONSTRAINT station_ibfk_1 FOREIGN KEY (city_id) REFERENCES city(id),
  CONSTRAINT UNIQUE (city_id, station_name, station_code)
) DEFAULT CHARACTER SET utf8mb4;
'''

DROP_TABLE_STATION = '''
DROP TABLE station;
'''

INSERT_INTO_TABLE_STATION = '''
INSERT INTO station (
  station_name,
  station_code,
  city_id
) VALUES (
  %s, %s, (SELECT id from city WHERE name=%s)
);
'''

SELECT_FROM_STATION = '''
SELECT s.id, s.station_name, s.station_code, c.name FROM station s LEFT JOIN city c on s.city_id=c.id;
'''

SELECT_FROM_STATION_WHERE_NAME = '''
SELECT s.id, s.station_name, s.station_code, c.name FROM station s LEFT JOIN city c on s.city_id=c.id WHERE station_name='{}';
'''

SELECT_FROM_STATION_WHERE_CODE = '''
SELECT s.id, s.station_name, s.station_code, c.name FROM station s LEFT JOIN city c on s.city_id=c.id WHERE station_code='{}';
'''

SELECT_FROM_STATION_WHERE_CITY = '''
SELECT id, station_name, station_code FROM station WHERE city_id=(SELECT id FROM city WHERE name='{}');
'''


def create_table_station(conn):
    execute_create_or_drop(conn, CREATE_TABLE_STATION)


def drop_table_station(conn):
    execute_create_or_drop(conn, DROP_TABLE_STATION)


def select_from_station(conn, station_name=None, station_code=None, city=None):
    if station_name:
        return execute_select_all(conn, SELECT_FROM_STATION_WHERE_NAME.format(station_name))
    elif station_code:
        return execute_select_all(conn, SELECT_FROM_STATION_WHERE_CODE.format(station_code))
    elif city:
        return execute_select_all(conn, SELECT_FROM_STATION_WHERE_CITY.format(city))


def select_all_from_station(conn):
    return execute_select_all(conn, SELECT_FROM_STATION)


def insert_into_station(conn, param):
    execute_insert(conn, INSERT_INTO_TABLE_STATION, param)


def insert_many_into_station(conn, params):
    return executemany_insert(conn, INSERT_INTO_TABLE_STATION, params)
