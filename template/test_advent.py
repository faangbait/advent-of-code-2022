import io
from main import main

def test_main():
    fakefile = io.TextIOWrapper(
        io.BytesIO(
b"""
"""
        )
    )
    assert main(fakefile) == 0
