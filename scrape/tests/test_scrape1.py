import pytest
from scraper.scrape1 import hello_world


def test_helloworld():
    output = hello_world()
    expected = "Hello world"
    assert output == expected
