"""
Tests for the secret file writing functionality in vault_anyconfig package.
"""
# pylint: disable=attribute-defined-outside-init
# pylint: disable=too-few-public-methods
# pylint: disable=no-self-use
# pylint: disable=unused-argument
from os.path import abspath, normpath

import pytest
from hypothesis import given, example
import hypothesis.strategies as strat


class TestFileNormFuzzing:
    @given(
        file_path=strat.text(
            min_size=1, alphabet=strat.characters(blacklist_categories=("C"))
        )
    )
    @example(file_path=" ")
    @example(file_path="//")
    def test_different_file_path(self, file_path):
        """
        Tests that secret keys, whitespace in paths, and hidden files are all handled correctly
        """

        abs_path_1 = abspath(file_path)
        abs_path_2 = abspath(abs_path_1)

        assert abs_path_1 == abs_path_2

        norm_path_1 = normpath(file_path)
        norm_path_2 = normpath(norm_path_1)

        assert norm_path_1 == norm_path_2
