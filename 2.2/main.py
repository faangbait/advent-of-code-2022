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

LOSE_CONDITIONS = {
    RPSThrow.ROCK: RPSThrow.PAPER,      # rock is covered by paper
    RPSThrow.PAPER: RPSThrow.SCISSORS,  # paper is cut by scissors
    RPSThrow.SCISSORS: RPSThrow.ROCK    # scissors are crushed by rock
}

Contest = namedtuple('Contest', ['villain', 'hero'])


def decode_throw(strategy: str) -> RPSThrow:
    """ 
    We'll just change this to have the villain throw the thing 
    that gives us the result we want
    """

    if strategy in ['A']:
        return RPSThrow.ROCK
    if strategy in ['B']:
        return RPSThrow.PAPER
    if strategy in ['C']:
        return RPSThrow.SCISSORS

    raise Exception("Invalid strategy input")


def decode_outcome(strategy: str) -> RPSResult:
    if strategy in ['X']:
        return RPSResult.LOSE
    if strategy in ['Y']:
        return RPSResult.DRAW
    if strategy in ['Z']:
        return RPSResult.WIN

    raise Exception("Invalid strategy input")


with open("input") as infile:
    lines = infile.readlines()

    total_points = 0
    line_number = 0

    for line in lines:
        line_number += 1
        r = line.split(" ")

        opp_throw = decode_throw(r[0].strip())
        desired_result = decode_outcome(r[1].strip())

        if desired_result == RPSResult.LOSE:
            strategy = Contest(
                opp_throw,
                WIN_CONDITIONS.get(opp_throw)
            )
        elif desired_result == RPSResult.WIN:
            strategy = Contest(
                opp_throw,
                LOSE_CONDITIONS.get(opp_throw)
            )
        else:
            strategy = Contest(
                opp_throw,
                opp_throw
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
