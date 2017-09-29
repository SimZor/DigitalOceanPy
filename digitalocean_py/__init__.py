import requests


class DigitalOceanAPI:
    token = ""
    endpoint = "https://api.digitalocean.com/v2/" + '/'
    headers = {'Authorization': token,
               'Content-Type': 'application/json'}

    def __init__(self, token):
        """

        :param token: API Key Token
        """
        self.token = token

    def get(self, endpoint_extension, payload):
        """
        Method for the GET request type

        :param endpoint_extension: endpoint extension for the api call to make (i.e. /account)
        :param payload:

        :type endpoint_extension:
        :type payload:

        :return: response in form of JSON
        :rtype:
        """
        self.endpoint += endpoint_extension

        response = requests.get(self.endpoint,
                                params=payload)

        response = requests.get(response.url,
                                headers=self.headers)

        return response

    def delete(self, endpoint_extension, payload):
        self.endpoint += endpoint_extension

        response = requests.delete(self.endpoint,
                                   params=payload)

        response = requests.delete(response.url,
                                   headers=self.headers)

    def put(self):
        return ""

    def post(self, endpoint_extension, payload):
        """

        :param endpoint_extension:
        :param payload:

        :return:
        :rtype:
        """

        self.endpoint += endpoint_extension

        response = requests.post(self.endpoint,
                                 headers=self.headers,
                                 data=payload)

        response.json()
        return response.text

    def head(self):
        return ""

