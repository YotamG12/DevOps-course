import pytest
from hello import greet

def test_greet():
    assert greet("World") == "Hello, World!"
