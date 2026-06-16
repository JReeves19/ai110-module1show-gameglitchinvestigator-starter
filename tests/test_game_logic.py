from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

# Tests targeting the swapped hint message bug:
# guess > secret must say "Go LOWER", guess < secret must say "Go HIGHER"

def test_hint_says_go_lower_when_guess_too_high():
    # Regression: bug had "Go HIGHER!" returned when guess exceeded secret
    outcome, message = check_guess(46, 12)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_hint_says_go_higher_when_guess_too_low():
    # Regression: bug had "Go LOWER!" returned when guess was below secret
    outcome, message = check_guess(5, 12)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_hint_correct_with_string_secret_too_high():
    # Regression: type-alternation bug passed secret as str on even attempts,
    # causing a TypeError fallback whose messages were also swapped
    outcome, message = check_guess(46, "12")
    assert outcome == "Too High"
    assert "LOWER" in message

def test_hint_correct_with_string_secret_too_low():
    outcome, message = check_guess(5, "12")
    assert outcome == "Too Low"
    assert "HIGHER" in message
