from digitalocean_py import DigitalOceanAPI, v2

api = DigitalOceanAPI('Bearer token');

test_call = v2.account.get_user_info(DigitalOceanAPI)
