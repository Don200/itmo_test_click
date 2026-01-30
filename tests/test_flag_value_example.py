import subprocess
import sys
import pytest

def test_flag_value_example() -> None:
    """Test the flag_value functionality of the hello command."""
    # Test with no argument, should use the flag_value
    result = subprocess.run(
        [sys.executable, 'examples/flag_value_example.py', '--name'],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "Hello, Flag!" in result.stdout

    # Test with an argument, should use the provided value
    result = subprocess.run(
        [sys.executable, 'examples/flag_value_example.py', '--name', 'Alice'],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "Hello, Alice!" in result.stdout

    # Test with no arguments, should use the default value
    result = subprocess.run(
        [sys.executable, 'examples/flag_value_example.py'],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "Hello, Default!" in result.stdout