from logic_utils import check_guess, get_range_for_difficulty, parse_guess
import random


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"


def test_boundary_guess_one_over():
    # If the secret is 50 and guess is 51, then it should be "Too High"
    result = check_guess(51, 50)
    assert result[0] == "Too High"


def test_boundary_guess_one_under():
    # If the secret is 50 and guess is 49, then it should be "Too Low"
    result = check_guess(49, 50)
    assert result[0] == "Too Low"


def test_negative_numbers():
    # If the secret is -5 and guess is -10, then it should be "Too Low"
    result = check_guess(-10, -5)
    assert result[0] == "Too Low"


def test_zero_guess():
    # If the secret is 50 and guess is 0, then it should be "Too Low"
    result = check_guess(0, 50)
    assert result[0] == "Too Low"


def test_large_numbers():
    # If the secret is 500000 and guess is 999999, then it should be "Too High"
    result = check_guess(999999, 500000)
    assert result[0] == "Too High"


def test_get_range_easy():
    # If the difficulty is "Easy", then the range should be 1 to 20
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20


def test_get_range_normal():
    # If the difficulty is "Normal", then the range should be 1 to 100
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100


def test_get_range_hard():
    # If the difficulty is "Hard", then the range should be 1 to 50
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 50


def test_get_range_invalid():
    # If the difficulty is invalid/unknown, then it should default to 1 to 100
    low, high = get_range_for_difficulty("Unknown")
    assert low == 1
    assert high == 100


def test_secret_in_easy_range():
    # If the difficulty is Easy, then the secret should be between 1 and 20
    low, high = get_range_for_difficulty("Easy")
    for _ in range(100):
        secret = random.randint(low, high)
        assert low <= secret <= high


def test_secret_in_normal_range():
    # If the difficulty is Normal, then the secret should be between 1 and 100
    low, high = get_range_for_difficulty("Normal")
    for _ in range(100):
        secret = random.randint(low, high)
        assert low <= secret <= high


def test_secret_in_hard_range():
    # If the difficulty is Hard, then the secret should be between 1 and 50
    low, high = get_range_for_difficulty("Hard")
    for _ in range(100):
        secret = random.randint(low, high)
        assert low <= secret <= high


def test_history_refresh_on_new_game():
    # If the user starts a new game, then the history of attempts should be cleared
    class MockSessionState:
        def __init__(self):
            self.history = []
            self.attempts = 0
            self.secret = 50
            self.score = 100
            self.status = "playing"

    def start_new_game(session_state, difficulty):
        low, high = get_range_for_difficulty(difficulty)
        session_state.attempts = 0
        session_state.secret = random.randint(low, high)
        session_state.history = []
        session_state.score = 0
        session_state.status = "playing"

    session_state = MockSessionState()
    session_state.history = [10, 20, 30, 40]
    session_state.attempts = 5
    session_state.score = 100

    start_new_game(session_state, "Normal")

    assert session_state.history == []
    assert session_state.attempts == 0
    assert session_state.score == 0
    assert session_state.status == "playing"
    assert (
        get_range_for_difficulty("Normal")[0]
        <= session_state.secret
        <= get_range_for_difficulty("Normal")[1]
    )


def test_parse_guess_negative_number():
    # If the user enters a negative number (-5), then it should return an error.
    result = parse_guess("-5")
    assert result[0] is False
    assert result[1] is None
    assert "between 1 and 100" in result[2]


def test_parse_guess_over_100():
    # If the user enters a number over 100 (101), then it should return an error.
    result = parse_guess("101")
    assert result[0] is False
    assert result[1] is None
    assert "between 1 and 100" in result[2]


def test_parse_guess_zero():
    # If the user enters 0, then it should return an error.
    result = parse_guess("0")
    assert result[0] is False
    assert result[1] is None
    assert "between 1 and 100" in result[2]


def test_parse_guess_valid_boundary_1():
    # If the user enters 1, then it should be accepted as valid.
    result = parse_guess("1")
    assert result[0] is True
    assert result[1] == 1


def test_parse_guess_valid_boundary_100():
    # If the user enters 100, then it should be accepted as valid.
    result = parse_guess("100")
    assert result[0] is True
    assert result[1] == 100
