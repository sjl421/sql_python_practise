import os
import json
from .base import BaseHandler
from db.station import insert_many_into_station, select_from_station, select_all_from_station


class StationHandler(BaseHandler):

    def get(self, *args, **kwargs):
        name = self.get_argument('name', None)
        code = self.get_argument('code', None)
        city = self.get_argument('city', None)
        if name:
            data = select_from_station(conn=self.conn, station_name=name)
        elif code:
            data = select_from_station(conn=self.conn, station_code=code)
        elif city:
            data = select_from_station(conn=self.conn, city=city)
        else:
            data = select_all_from_station(conn=self.conn)
        self.write({'status': 'success', 'data': data})

    def post(self, *args, **kwargs):
        with open(os.path.join(os.path.dirname(__file__), '../data/station_names.json')) as fh:
            cities = json.loads(fh.read())
            for city in cities:
                message = insert_many_into_station(
                    conn=self.conn,
                    params=list(map(lambda x: (x['station_name'], x['station_code'], city['city']), city['stations']))
                )
                if message:
                    self.finish({'status': 'error', 'message': message})
                    break
            self.write({'status': 'success', 'message': '插入{}条监测站数据'.format(len(cities))})
