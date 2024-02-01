import requests

from pythonProject.api.conftest import SERVICE_URL

from pythonProject.api.src.baseclasses.response import Response
from pythonProject.api.src.shemas.post import POST_SCHEMA


def test_getting_posts():
    r = requests.get(url=SERVICE_URL)
    response = Response(r)
    response.assert_status_code(200).validate(POST_SCHEMA)
