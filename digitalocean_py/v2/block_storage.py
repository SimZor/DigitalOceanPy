from digitalocean_py import DigitalOceanAPI

class BlockStorage:
    @staticmethod
    def list_all(api_object):
        return DigitalOceanAPI.get(api_object, 'volumes')

    @staticmethod
    def create_new_volume(api_object):
        DigitalOceanAPI.put()
