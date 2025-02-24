from faker import Faker
import requests

from services.university.helpers.group_helper import GroupHelper

faker = Faker()


class TestGroupContract:

    def test_create_group_anonym(self, university_api_utils_anonym):
        group_helper = GroupHelper(university_api_utils_anonym)
        response = group_helper.post_group({"name": faker.name()})
        assert response.status_code == requests.status_codes.codes.unauthorized,\
            (f"Wrong status code: {response.status_code},"
             f" expected {requests.status_codes.codes.unauthorized}")
