from feeder.dal import DAL


class BaseFetcher:
    def __init__(self):
        self.dal = DAL()

    def run(self):
        """
        Start listening websockets.
        """
        pass

    def sync(self):
        """
        Sync history using REST API.
        """
        raise NotImplementedError

    def get_user_balance(self):
        raise NotImplementedError
    
    def get_trades(self):
        raise NotImplementedError


if __name__ == '__main__':
    BaseFetcher().get_user_balance()
