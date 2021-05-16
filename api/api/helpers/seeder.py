import yaml
from icecream import ic
from api import ROOT_PATH
from api.models.user import User
from api.models.base import get_db


def load_seed_data():
    with open(f'{ROOT_PATH}/seeds/users.yml', 'r') as file:
        users = yaml.load(file)
        db = next(get_db())
        for key, details in users['users'].items():
            ic(key)
            ic(details)
            new_user = User(id=key,
                            email=details['email'],
                            hashed_password=details['password'],
                            binance_api_key=details['binance_api_key'],
                            binance_api_secret=details['binance_api_secret'])
            db.merge(new_user)
        db.commit()


if __name__ == '__main__':
    load_seed_data()
