from datetime import datetime
from typing import List
import os

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS


class DAL:
    def __init__(self):
        token = os.getenv("INFLUXDB_TOKEN")
        self.org = os.getenv("INFLUXDB_ORG")
        self.bucket = os.getenv("INFLUXDB_BUCKET")
        self.client = InfluxDBClient(url="http://localhost:8086", token=token)
        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)

    def write(self, trade):
        self.write_api.write(self.bucket, self.org, trade)
