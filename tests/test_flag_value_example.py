import subprocess
import sys
import pytest
from click.testing import CliRunner
from examples.flag_value_example import hello

def test_flag_value_example() -> None:
    """Test the flag_value functionality of the hello command."""
    runner = CliRunner()
    
    # Test with no argument, should use the flag_value
    result = runner.invoke(hello, ['--name'])
    assert result.returncode == 0
    assert "Hello, Flag!" in result.output

    # Test with an argument, should use the provided value
    result = runner.invoke(hello, ['--name', 'Alice'])
    assert result.returncode == 0
    assert "Hello, Alice!" in result.output

    # Test with no arguments, should use the default value
    result = runner.invoke(hello, [])
    assert result.returncode == 0
    assert "Hello, Default!" in result.output