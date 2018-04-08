import tornado.ioloop
from handler.base import MainHandler
from handler.city import CityHandler
from handler.station import StationHandler
from handler.aqi import CityAqiHandler, StationAqiHandler
from db.city import create_table_city
from db.station import create_table_station
from db.aqi import create_table_city_aqi, create_table_station_aqi


def make_app():
    return tornado.web.Application([
        (r'/', MainHandler),
        (r'/city', CityHandler),
        (r'/station', StationHandler),
        (r'/aqi/city', CityAqiHandler),
        (r'/aqi/station', StationAqiHandler),
    ])


if __name__ == '__main__':
    create_table_city()
    create_table_station()
    create_table_city_aqi()
    create_table_station_aqi()
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
