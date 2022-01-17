import pytest


@pytest.fixture(params=[1, 2, 3])
def login(request):
    return request.param


def pytest_configure(config):
    marker_list = ["a1", "a2"]
    for markers in marker_list:
        config.addinivalue_line("markers", markers)
