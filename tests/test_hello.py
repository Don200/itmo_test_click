import subprocess
import sys
import pytest

def test_hello_with_flag():
    """Test the hello command with the flag only."""
    result = subprocess.run(
        [sys.executable, "examples/hello.py", "--name"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "Hello, Flag!" in result.stdout

def test_hello_with_value():
    """Test the hello command with a name value."""
    result = subprocess.run(
        [sys.executable, "examples/hello.py", "--name", "Alice"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "Hello, Alice!" in result.stdout

def test_hello_without_flag_or_value():
    """Test the hello command without any arguments."""
    result = subprocess.run(
        [sys.executable, "examples/hello.py"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "Hello, Default!" in result.stdout