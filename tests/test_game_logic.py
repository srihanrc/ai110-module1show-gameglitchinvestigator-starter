import os
import sys

# Ensure project root is on sys.path so tests can import project modules
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win"
    assert result[1] == "🎉 Correct!"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"
    assert result[1] == "📉 Go LOWER!"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"
    assert result[1] == "📈 Go HIGHER!"


def test_get_range_for_difficulty():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)


def test_parse_guess_and_errors():
    ok, val, err = parse_guess("42")
    assert ok and val == 42 and err is None

    ok, val, err = parse_guess("42.0")
    assert ok and val == 42

    ok, val, err = parse_guess("")
    assert not ok and "enter a guess" in err.lower()

    ok, val, err = parse_guess("abc")
    assert not ok and "not a number" in err.lower()


def test_update_score_behavior():
    # Winning gives at least 10 points even on large attempt numbers
    new = update_score(0, "Win", 100)
    assert new >= 10

    # Too High alternates +5 on even attempt numbers, -5 on odd
    assert update_score(0, "Too High", 2) == 5
    assert update_score(0, "Too High", 3) == -5

    # Too Low always subtracts 5
    assert update_score(10, "Too Low", 1) == 5
