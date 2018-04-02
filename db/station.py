from .base import execute_create_or_drop


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


def create_table_station(conn):
    execute_create_or_drop(conn, CREATE_TABLE_STATION)


def drop_table_station(conn):
    execute_create_or_drop(conn, DROP_TABLE_STATION)
