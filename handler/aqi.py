import os
import json
from .base import BaseHandler
from db.aqi import *


class AqiHandler(BaseHandler):

    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        data = self.request.body
        aqi_for = json.loads(data)['type']
        if aqi_for == 'city':
            with open(os.path.join(os.path.dirname(__file__), '../data/aqi_ranking.json')) as fh:
                cities = json.loads(fh.read())
                message = insert_many_into_city_aqi(
                    conn=self.conn,
                    params=list(map(lambda x: (
                            x['aqi'],
                            x['area'],
                            x['co'],
                            x['co_24h'],
                            x['no2'],
                            x['no2_24h'],
                            x['o3'],
                            x['o3_24h'],
                            x['o3_8h'],
                            x['o3_8h_24h'],
                            x['pm10'],
                            x['pm10_24h'],
                            x['pm2_5'],
                            x['pm2_5_24h'],
                            x['primary_pollutant'],
                            x['quality'],
                            x['level'],
                            x['so2'],
                            x['so2_24h'],
                            x['time_point'].replace('T', ' ').replace('Z', '')
                        ), cities))
                )
                if not message:
                    self.write('post {}'.format(cities))
                else:
                    self.write('err: {}'.format(message))
        self.write(aqi_for)
