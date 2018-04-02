import os
import json
from .base import BaseHandler
from db.base import execute_select
from db.city import insert_many_into_city


class CityHandler(BaseHandler):

    def get(self, *args, **kwargs):
        data = execute_select(conn=self.conn, sql=SELECT_FROM_CITY)
        self.write('get {}'.format(data))

    def post(self, *args, **kwargs):
        with open(os.path.join(os.path.dirname(__file__), '../data/querys.json')) as fh:
            cities = json.loads(fh.read())['cities']
            message = insert_many_into_city(conn=self.conn, params=list(map(lambda x: (x, ), cities)))
            if not message:
                self.write('post {}'.format(cities))
            else:
                self.write('err: {}'.format(message))
