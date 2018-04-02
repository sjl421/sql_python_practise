from .base import *


CREATE_TABLE_STATION = '''
CREATE TABLE IF NOT EXISTS station (
  id INT PRIMARY KEY auto_increment,
  station_name VARCHAR(50) not NULL,
  station_code VARCHAR(10) not NULL,
  city_id INT not NULL,
  KEY city_id (city_id),
  CONSTRAINT station_ibfk_1 FOREIGN KEY (city_id) REFERENCES city(id)
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
  %s, %s, %s
);
'''

SELECT_FROM_STATION = '''
SELECT * FROM station;
'''

SELECT_FROM_STATION_WHERE_NAME = '''
SELECT * FROM station WHERE station_name='{}';
'''


def create_table_station(conn):
    execute_create_or_drop(conn, CREATE_TABLE_STATION)


def drop_table_station(conn):
    execute_create_or_drop(conn, DROP_TABLE_STATION)


def select_from_station(conn, station):
    return execute_select_all(conn, SELECT_FROM_STATION_WHERE_NAME.format(station))


def select_all_from_station(conn):
    return execute_select_all(conn, SELECT_FROM_STATION)


def insert_into_station(conn, param):
    execute_insert(conn, INSERT_INTO_TABLE_STATION)


def insert_many_into_station(conn, params):
    return executemany_insert(conn, INSERT_INTO_TABLE_STATION, params)
