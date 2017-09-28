from digitalocean_py.digitaloceanapi import DigitalOceanAPI


class Account:
    @staticmethod
    def get_user_info():
        return DigitalOceanAPI.get('account')