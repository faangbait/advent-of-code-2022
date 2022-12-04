import io, sys
sys.path.append('/home/ss/dev/advent-of-code-2022')
from main import main

def test_main():
    fakefile = io.TextIOWrapper(
        io.BytesIO(
b"""
"""
        )
    )
    assert main(fakefile) == 0
