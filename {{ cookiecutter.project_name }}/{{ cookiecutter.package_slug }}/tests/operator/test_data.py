from {{ cookiecutter.package_slug }}.operator import data
import pytest
import urllib


def test_get_data():
    with pytest.raises(urllib.error.URLError):
        data.get_data('fake_url', 'fake_location')
