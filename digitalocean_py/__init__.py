import requests


class DigitalOceanAPI:
    token = ""
    endpoint = "https://api.digitalocean.com/v2/"
    headers = {'Authorization': token,
               'Content-Type': 'application/json'}

    def __init__(self, token):
        """

        :param token: API Key Token
        """
        self.token = token

    def get(self, endpoint_extension):
        """
        Method for the GET request type

        :param endpoint_extension: endpoint extension for the api call to make (i.e. /account)
        :return: response in form of JSON
        """
        url = self.endpoint + '/' + endpoint_extension

        response = requests.get(url,
                                headers=self.headers)

        return response.text

    def delete(self):
        return ""

    def put(self):
        return ""

    def post(self):
        return ""

    def head(self):
        return ""

