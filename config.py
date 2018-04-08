from platform import platform


DB_HOST = '127.0.0.1'
if 'fedora' in platform():
    DB_HOST = '120.92.80.41'
DB_PORT = 3306
DB_USERNAME = 'root'
DB_PASSWORD = 'Zhujia1991'
DB_NAME = 'aqi'
