from digitalocean_py import DigitalOceanAPI


class BlockStorage:
    api_object = None

    def __init__(self, api_object):
        """
        Constructor

        :param api_object:
        """

        self.api_object = api_object

    def list_all(self):
        """

        :return:
        :rtype:
        """
        return DigitalOceanAPI.get(self.api_object, 'volumes')

    def create_new_volume(self, size_gb, name, desc, region, snapshot_id):
        """
        Used for creating a new volume in block storage

        :param api_object:
        :param size_gb:
        :param name:
        :param desc:
        :param region:
        :param snapshot_id:

        :type api_object: object
        :type size_gb: integer
        :type name: string
        :type desc: string
        :type region: string
        :type snapshot_id: string

        :return:
        :rtype: string
        """

        payload = {'size_gigabytes': size_gb,
                   'name': name,
                   'description': desc,
                   'region': region,
                   'snapshot-id': snapshot_id}

        return DigitalOceanAPI.post(self.api_object, 'volumes', payload)

    def retrieve_block_volume(self, volume_id):
        """

        :param volume_id:
        :return:
        """

        return DigitalOceanAPI.get(self.api_object, 'volumes/' + volume_id)

    def retrieve_block_volume_byname(self, name, region):
        """

        :param name:
        :param region:
        :return:
        """

        return DigitalOceanAPI.get(self.api_object, 'volumes', {'name': name, 'region': region})

    def list_snapshots(self, volume_id):
        """

        :param volume_id:
        :return:
        """

        return DigitalOceanAPI.get(self.api_object, 'volumes/' + volume_id + '/snapshots')

    def create_snapshot_from_volume(self, volume_id, name):
        """

        :param volume_id:
        :param name:
        :return:
        """

        return DigitalOceanAPI.get(self.api_object, 'volumes/' + volume_id, {'name': name})

    def delete_volume_by_name(self, name, region):
        """

        :param name:
        :param region:
        :return:
        """

        return DigitalOceanAPI.delete(self.api_object, 'volumes', {'name': name, 'region': region})
