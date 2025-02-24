import random

from faker import Faker

from services.auth.helpers.auth_helper import AuthHelper
from services.university.helpers.group_helper import GroupHelper
from services.university.helpers.student_helper import StudentHelper
from services.auth.helpers.user_helper import UserHelper
from utils.api_utils import ApiUtils

faker = Faker()

AUTH_URL = 'http://localhost:8000'
UNIVERSITY_URL = 'http://localhost:8001'

REGISTER_ENDPOINT = "/auth/register/"
LOGIN_ENDPOINT = "/auth/login/"

ME_ENDPOINT = "/users/me/"

GROUP_ENDPOINT = "/groups/"

STUDENT_ENDPOINT = "/students/"

username = faker.user_name()
password = '!@#2325' + faker.password()

auth_api_utils = ApiUtils(AUTH_URL)
authorization_helper = AuthHelper(api_utils=ApiUtils(AUTH_URL))
response = authorization_helper.post_register(
    data={
        'username': username,
        'password': password,
        'password_repeat': password,
        'email': faker.email(),
    }
)
response = authorization_helper.post_login(
    data={
        'username': username,
        'password': password,
    }
)

access_token = response.json()['access_token']

admin_auth_api_utils = ApiUtils(AUTH_URL, headers={'Authorization': f'Bearer {access_token}'})
user_admin_helper = UserHelper(admin_auth_api_utils)

admin_university_api_utils = ApiUtils(UNIVERSITY_URL, headers={'Authorization': f'Bearer {access_token}'})

group_admin_helper = GroupHelper(admin_university_api_utils)
student_admin_helper = StudentHelper(admin_university_api_utils)

response = user_admin_helper.get_me()
response = group_admin_helper.post_group(json={
    "name": faker.name(),
})

response = student_admin_helper.post_student(
    json={
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "email": faker.email(),
        'degree': random.choice(
            [
                'Associate',
                'Bachelor',
                'Master',
                'Doctorate',
            ]
        ),
        "phone": faker.numerify('+7##########'),
        'group_id': response.json().get('id'),
    }
)
