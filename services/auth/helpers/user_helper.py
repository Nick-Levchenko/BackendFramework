import requests

from services.general.helpers.base_helper import BaseHelper


class UserHelper(BaseHelper):
    GET_ME_ENDPOINT = '/users/me'

    def get_me(self) -> requests.Response:
        response = self.api_utils.get(self.GET_ME_ENDPOINT)
        return response
