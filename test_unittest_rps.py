"""Rock Paper Scissors game logic unit_testing ."""
from rps_game import determine_winner, is_valid_choice

def test_user_wins():
    """Rock Paper Scissors game logic user_wins"""
    assert determine_winner("rock", "scissors") == "user"
    assert determine_winner("paper", "rock") == "user"
    assert determine_winner("scissors", "paper") == "user"

def test_computer_wins():
    """Rock Paper Scissors game logic computer_wins"""
    assert determine_winner("rock", "paper") == "computer"
    assert determine_winner("paper", "scissors") == "computer"
    assert determine_winner("scissors", "rock") == "computer"

def test_tie_cases():
    """Rock Paper Scissors game logic tie_cases"""
    assert determine_winner("rock", "rock") == "tie"
    assert determine_winner("paper", "paper") == "tie"
    assert determine_winner("scissors", "scissors") == "tie"

def test_valid_choices():
    """Rock Paper Scissors game logic validate_choices"""
    assert is_valid_choice("rock") is True
    assert is_valid_choice("paper") is True
    assert is_valid_choice("scissors") is True
    assert is_valid_choice("banana") is False
