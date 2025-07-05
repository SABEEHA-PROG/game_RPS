"""Rock Paper Scissors game logic. mock test """
from unittest.mock import patch
from rps_game import determine_winner

def test_user_wins_mocked_computer_choice():
    """Rock Paper Scissors game logic test_user_wins_mocked_computer_choice"""
    with patch("rps_game.get_computer_choice", return_value="scissors"):
        result = determine_winner("rock", "scissors")  # Use mocked value directly
        assert result == "user"

def test_computer_wins_mocked_computer_choice():
    """Rock Paper Scissors game logic test_computer_wins_mocked_computer_choice"""
    with patch("rps_game.get_computer_choice", return_value="rock"):
        result = determine_winner("scissors", "rock")
        assert result == "computer"

def test_tie_mocked_computer_choice():
    """Rock Paper Scissors game logic test_tie_mocked_computer_choice"""
    with patch("rps_game.get_computer_choice", return_value="paper"):
        result = determine_winner("paper", "paper")
        assert result == "tie"
