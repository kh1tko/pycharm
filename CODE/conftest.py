import pytest


@pytest.fixture(params=[('username1', 'password1'), ('username2', 'password2'), ('username3', 'password3')])
def loginfixture(request):
    return request.param
