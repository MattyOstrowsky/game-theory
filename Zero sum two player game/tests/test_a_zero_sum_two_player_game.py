import numpy as np
from a_zero_sum_two_player_game.game import (
    load_data,
    find_dominant_column,
    find_dominant_row,
    maxmin,
    minmax,
)

sample = np.array([[0.2, 0.3, 0.4], [0.5, 0.1, 0.0], [0.1, 0.2, 0.3]])
file = "/home/gunater/Dokumenty/" "A-zero-sum-two-player-game/" "game-theory/sample.txt"


def test_load_data():
    data = load_data(file)
    assert np.array_equal(data, sample)


def test_find_dominant_row():
    assert np.array_equal(
        find_dominant_row(sample), np.array([[0.2, 0.3, 0.4], [0.5, 0.1, 0.0]])
    )


def test_find_dominant_column():
    assert np.array_equal(
        find_dominant_column(sample),
        np.array([[0.2, 0.3, 0.4], [0.5, 0.1, 0.0], [0.1, 0.2, 0.3]]),
    )


def test_minmax():
    value, index = minmax(sample)
    assert value == 0.3 and index == 2


def test_maxmin():
    value, index = maxmin(sample)
    assert value == 0.2 and index == 1
