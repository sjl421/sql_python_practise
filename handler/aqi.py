import os
import json
from .base import BaseHandler
from db.aqi import *


def format_city_aqi(data):
    keys = (
        'aqi',
        'area',
        'co',
        'co_24h',
        'no2',
        'no2_24h',
        'o3',
        'o3_24h',
        'o3_8h',
        'o3_8h_24h',
        'pm10',
        'pm10_24h',
        'pm2_5',
        'pm2_5_24h',
        'quality',
        'level',
        'so2',
        'so2_24h',
        'primary_pollutant',
        'time_point'
    )
    return list(map(lambda city: dict(zip(keys, city)), data))


def format_station_aqi(data):
    keys = (
        'aqi',
        'area',
        'co',
        'co_24h',
        'no2',
        'no2_24h',
        'o3',
        'o3_24h',
        'o3_8h',
        'o3_8h_24h',
        'pm10',
        'pm10_24h',
        'pm2_5',
        'pm2_5_24h',
        'position_name',
        'primary_pollutant',
        'quality',
        'so2',
        'so2_24h',
        'time_point'
    )
    return list(map(lambda station: dict(zip(keys, station)), data))


class CityAqiHandler(BaseHandler):

    def get(self, *args, **kwargs):
        name = self.get_argument('name', None)
        if name:
            data = select_from_city_aqi(city=name)
        else:
            data = select_all_from_city_aqi()
        self.write({'status': 'success', 'count': len(data), 'data': format_city_aqi(data)})

    def post(self, *args, **kwargs):
        with open(os.path.join(os.path.dirname(__file__), '../data/aqi_ranking.json')) as fh:
            cities = json.loads(fh.read())
            message = insert_many_into_city_aqi(
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
                self.write({'status': 'success', 'message': '插入{}条城市空气质量数据'.format(len(cities))})
            else:
                self.write({'status': 'error', 'message': message})


class StationAqiHandler(BaseHandler):

    def get(self, *args, **kwargs):
        city = self.get_argument('city', None)
        if city:
            data = select_from_station_aqi(city=city)
        else:
            data = select_all_from_city_aqi()
        self.write({'status': 'success', 'count': len(data), 'data': format_station_aqi(data)})

    def post(self, *args, **kwargs):
        with open(os.path.join(os.path.dirname(__file__), '../data/all_cities.json')) as fh:
            cities = json.loads(fh.read())
            message = insert_many_into_station_aqi(
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
                    x['position_name'],
                    x['station_code'],
                    x['area'],
                    x['primary_pollutant'],
                    x['quality'],
                    x['so2'],
                    x['so2_24h'],
                    x['time_point'].replace('T', ' ').replace('Z', '')
                ), cities))
            )
            if not message:
                self.write({'status': 'success', 'message': '插入{}条监测站空气质量数据'.format(len(cities))})
            else:
                self.write({'status': 'error', 'message': message})
