import os
import json
from .base import BaseHandler


class AqiHandler(BaseHandler):

    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        data = self.request.body
        aqi_for = json.loads(data)['type']
        self.write(aqi_for)
