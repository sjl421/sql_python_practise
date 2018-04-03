import os
import json
from .base import BaseHandler
from db.station import insert_many_into_station, select_from_station, select_all_from_station


class StationHandler(BaseHandler):

    def get(self, *args, **kwargs):
        name = self.get_argument('name', None)
        if name:
            data = select_from_station(conn=self.conn, station=name)
        else:
            data = select_all_from_station(conn=self.conn)
        self.write('get {}'.format(data))

    def post(self, *args, **kwargs):
        with open(os.path.join(os.path.dirname(__file__), '../data/station_names.json')) as fh:
            cities = json.loads(fh.read())
            for city in cities:
                message = insert_many_into_station(
                    conn=self.conn,
                    params=list(map(lambda x: (x['station_name'], x['station_code'], city['city']), city['stations']))
                )
            if not message:
                self.write('post {}'.format(cities))
            else:
                self.write('err: {}'.format(message))
