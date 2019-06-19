from data import ExchangePlatform
from binance.client import Client
import tornado.ioloop
import config
import logging
import signal

PULL_INTERVAL_MS = 5 * 60
JITTER = 0.13

logging.basicConfig(level='DEBUG')
log = logging.getLogger(__name__)


class ExchangePuller:
    def __init__(self, exchange_platform: ExchangePlatform):
        def exit_handler(sig, frame):
            log.info('exiting')
            tornado.ioloop.IOLoop.instance().add_callback_from_signal(self.stop)
        
        signal.signal(signal.SIGTERM, exit_handler)
        signal.signal(signal.SIGINT,  exit_handler)

        self.conf = exchange_platform
        # self.client = Client(exchange_platform.api_key, exchange_platform.secret_key)
        self.cnt = 0

    def run(self):
        log.info('starting')
        def schedule_func():
            #DO SOMETHING#
            # balances = self.client.get_account()
            log.debug(self.cnt)
            self.cnt += 1

        #milliseconds
        main_loop = tornado.ioloop.IOLoop.current()
        self.sched = tornado.ioloop.PeriodicCallback(schedule_func, PULL_INTERVAL_MS, JITTER)
        #start your period timer
        self.sched.start()
        #start your loop
        main_loop.start()
        main_loop.stop()
        log.info('shutdown')

    async def stop(self):
        log.info('shutting down')
        self.sched.stop()
        tornado.ioloop.IOLoop.current().stop()


if __name__ == '__main__':
   
    binance_conf = ExchangePlatform(name='Binance',
                                    api_key=config.API_KEY,
                                    secret_key=config.SECRET_KEY)
    exchange_puller = ExchangePuller(binance_conf)
    exchange_puller.run()
