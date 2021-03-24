from influxdb import InfluxDBClient

json_body = [
    {
        "measurement": "trades",
        "tags": {
            "exchanges": "binance",
            "pair": "btcusd",
            "side": "buy"
        },
        "time": "2009-11-10T23:00:00Z",
        "fields": {
            "value": 0.64
        }
    }
]

client = InfluxDBClient('localhost', 8086, 'root', 'root', 'example')
client.create_database('example')
client.write_points(json_body)
result = client.query('select value from cpu_load_short;')

if __name__ == '__main__':
    print("Result: {0}".format(result))
