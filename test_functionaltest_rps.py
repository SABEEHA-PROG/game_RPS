"""Rock Paper Scissors game logic. functional test """
import builtins
from rps_game import play_game

def test_play_game(monkeypatch, capsys):
    """Rock Paper Scissors game logic test_play_game"""
    # Simulate a sequence of user inputs
    inputs = iter(["rock", "banana", "scissors", "exit"])  # banana is invalid
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    # Run the game
    play_game()

    # Capture printed output
    captured = capsys.readouterr()
    output = captured.out

    # Assert key phrases appear in output
    assert "Computer chose:" in output
    assert "Invalid choice." in output
    assert "Final Score" in output
    assert "You:" in output or "Computer:" in output
