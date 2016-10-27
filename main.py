import requests


class BaseClient:
    BASE_URL = "https://api.vk.com/method/"

    method = None
    http_method = None

    def get_params(self):
        pass

    def get_json(self):
        pass

    def get_headers(self):
        pass

    def generate_url(self, method):
        return '{0}{1}'.format(self.BASE_URL, method)

    def _get_data(self, method, http_method):


        response = requests.get(self.generate_url(method), params = self.get_params())
        # todo выполнить запрос
        print(self.generate_url(method))
        return self.response_handler(response)

    def response_handler(self, response):
        return response

    def execute(self):
        return self._get_data(
            self.method,
            http_method=self.http_method
        )