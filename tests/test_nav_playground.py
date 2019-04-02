#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `nav_playground` package."""

import pytest

from nav_playground import nav_playground
from nav_playground import cli


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_cli():
    """Test the CLI."""

    parser = cli.parse_args(["--foo", "test"])
    assert parser.foo == "test"
