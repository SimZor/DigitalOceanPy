from digitalocean_py import DigitalOceanAPI


class BlockStorageActions:
    api_object = None

    def __init__(self, api_object):
        """
        Constructor

        :param api_object:
        """

        self.api_object = api_object

    def attach_volume_to_droplet(self, volume_id, droplet_id, region, type='attach'):
        """
        Used to attach a existing volume to a droplet

        :param volume_id:
        :param droplet_id:
        :param region:
        :param type:

        :return:
        :rtype: JSON object
        """

        return DigitalOceanAPI.post(self.api_object,
                                    'volumes/' + volume_id + '/actions',
                                    {'type': type,
                                     'droplet_id': droplet_id,
                                     'region': region})

    def attach_volume_to_droplet_by_name(self, droplet_id, volume_name, region, type='attach'):
        """
        Used for attaching a volume to a droplet by a name

        :param droplet_id:
        :param volume_name:
        :param region:
        :param type:

        :return:
        :rtype:
        """

        return DigitalOceanAPI.post(self.api_object,
                                    'volumes/actions',
                                    {'type': type,
                                     'droplet_id': droplet_id,
                                     'volume_name': volume_name,
                                     'region': region})

    def remove_volume_from_droplet(self, volume_id, droplet_id, region, type='attach'):
        """

        :param volume_id:
        :param droplet_id:
        :param region:
        :param type:
        :return:
        """
        return DigitalOceanAPI.post(self.api_object,
                                    'volumes/' + volume_id + '/actions',
                                    {'type': type,
                                     'droplet_id': droplet_id,
                                     'region': region})

    def remove_volume_from_droplet_byname(self, droplet_id, volume_name, region, type='attach'):
        """

        :param droplet_id:
        :param volume_name:
        :param region:
        :return:
        """
        return DigitalOceanAPI.post(self.api_object,
                                    'volumes/' + 'actions',
                                    {'type': type,
                                     'droplet_id': droplet_id,
                                     'volume_name': volume_name,
                                     'region': region})

    def rezise_volume(self, volume_id, size_gb, region, type='resize'):
        """

        :param self:
        :param volume_id:
        :param size_gb:
        :param region:
        :param type:
        :return:
        """
        return DigitalOceanAPI.post(self.api_object,
                                    'volumes/' + volume_id + '/actions',
                                    {'type': type,
                                     'size_gigabytes': size_gb,
                                     'region': region})

    def list_all_actions(self, volume_id):
        """

        :param volume_id:
        :return:
        """
        return DigitalOceanAPI.get(self.api_object,
                                   'volumes/' + volume_id + '/actions')

    def get_volume_action(self, volume_id, action_id):
        """

        :param volume_id:
        :param action_id:
        :return:
        """
        return DigitalOceanAPI.get(self.api_object,
                                   'volumes/' + volume_id + '/actions/' + action_id)

