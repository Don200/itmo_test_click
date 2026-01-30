import click
import pytest
from click.testing import CliRunner
from src.click.decorators import custom_option

@click.command()
@custom_option("--name", is_flag=False, flag_value="Flag", default="Default")
def hello(name: str) -> None:
    click.echo(f"Hello, {name}!")

def test_hello_with_flag_value():
    runner = CliRunner()
    result = runner.invoke(hello, ["--name"])
    assert result.exit_code == 0
    assert result.output.strip() == "Hello, Flag!"

def test_hello_with_default_value():
    runner = CliRunner()
    result = runner.invoke(hello)
    assert result.exit_code == 0
    assert result.output.strip() == "Hello, Default!"

def test_hello_with_custom_value():
    runner = CliRunner()
    result = runner.invoke(hello, ["--name", "Custom"])
    assert result.exit_code == 0
    assert result.output.strip() == "Hello, Custom!"