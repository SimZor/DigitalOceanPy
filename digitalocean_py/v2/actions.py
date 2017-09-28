from digitalocean_py import DigitalOceanAPI

class Actions():
    @staticmethod
    def list_all_actions(api_object):
        return DigitalOceanAPI.get(api_object, 'actions')

    @staticmethod
    def retrive_exisiting_action(api_object, action_id):
        return DigitalOceanAPI.get(api_object, 'actions/' + action_id)
