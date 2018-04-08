from .base import DB


CREATE_TABLE_CITY = '''
CREATE TABLE IF NOT EXISTS city (
  id INT PRIMARY KEY auto_increment,
  name VARCHAR(30) not NULL UNIQUE
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


def create_table_city():
    db = DB()
    db.execute_create_or_drop(CREATE_TABLE_CITY)


def drop_table_city():
    db = DB()
    db.execute_create_or_drop(DROP_TABLE_CITY)


def select_from_city(city):
    db = DB()
    return db.execute_select_all(SELECT_FROM_CITY_WHERE_NAME.format(city))


def select_all_from_city():
    db = DB()
    return db.execute_select_all(SELECT_FROM_CITY)


def insert_into_city(param):
    db = DB()
    db.execute_insert(INSERT_INTO_TABLE_CITY)


def insert_many_into_city(params):
    db = DB()
    return db.executemany_insert(INSERT_INTO_TABLE_CITY, params)
