import os
import json
from .base import BaseHandler
from db.city import insert_many_into_city, select_from_city, select_all_from_city


class CityHandler(BaseHandler):

    def get(self, *args, **kwargs):
        name = self.get_argument('name', None)
        if name:
            data = select_from_city(conn=self.conn, city=name)
        else:
            data = select_all_from_city(conn=self.conn)
        self.write('get {}'.format(data))

    def post(self, *args, **kwargs):
        with open(os.path.join(os.path.dirname(__file__), '../data/querys.json')) as fh:
            cities = json.loads(fh.read())['cities']
            message = insert_many_into_city(conn=self.conn, params=list(map(lambda x: (x, ), cities)))
            if not message:
                self.write('post {}'.format(cities))
            else:
                self.write('err: {}'.format(message))
