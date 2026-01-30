import subprocess
import sys
import pytest

def test_hello_with_flag_value() -> None:
    """Test the hello command with the flag value."""
    result = subprocess.run(
        [sys.executable, "src/click/examples/hello.py", "--name"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "Hello, Flag!" in result.stdout

def test_hello_with_default_value() -> None:
    """Test the hello command without the flag."""
    result = subprocess.run(
        [sys.executable, "src/click/examples/hello.py"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "Hello, Default!" in result.stdout