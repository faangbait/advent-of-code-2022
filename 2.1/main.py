from collections import namedtuple
from enum import Enum


class RPSThrow(Enum):
    """ The value of each throw is included with this enum """
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class RPSResult(Enum):
    """ The value of each result is included with this enum """
    WIN = 6
    DRAW = 3
    LOSE = 0


WIN_CONDITIONS = {
    RPSThrow.ROCK: RPSThrow.SCISSORS,   # rock crushes scissors
    RPSThrow.PAPER: RPSThrow.ROCK,      # paper covers rock
    RPSThrow.SCISSORS: RPSThrow.PAPER   # scissors cut paper
}

Contest = namedtuple('Contest', ['villain', 'hero'])


def decode_throw(strategy: str) -> RPSThrow:

    if strategy in ['A', 'X']:
        return RPSThrow.ROCK
    if strategy in ['B', 'Y']:
        return RPSThrow.PAPER
    if strategy in ['C', 'Z']:
        return RPSThrow.SCISSORS

    raise Exception("Invalid strategy input")


with open("input") as infile:
    lines = infile.readlines()

    total_points = 0
    line_number = 0

    for line in lines:
        line_number += 1
        r = line.split(" ")

        strategy = Contest(
            decode_throw(r[0].strip()),
            decode_throw(r[1].strip())
        )

        round_points = 0
        res = None

        if WIN_CONDITIONS.get(strategy.hero) == strategy.villain:
            res = RPSResult.WIN
        elif WIN_CONDITIONS.get(strategy.villain) == strategy.hero:
            res = RPSResult.LOSE
        else:
            res = RPSResult.DRAW

        round_points += res.value               # add result value
        round_points += strategy.hero.value     # add throw value
        
        total_points += round_points
        # print(f"[{line_number}] Opp: {strategy.villain}\t\tUs: {strategy.hero}\t\t {res}\t\t+{round_points}={total_points}")

    print(
        "Playing by the strategy guide, we achieve a score of: "
        f"{total_points}"
    )
