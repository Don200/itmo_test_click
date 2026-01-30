from click.testing import CliRunner
from src.click.decorators import option

@click.command()
@option("--name", is_flag=False, flag_value="Flag", default="Default")
def hello(name: str) -> None:
    click.echo(f"Hello, {name}!")

def test_hello_with_flag_value() -> None:
    runner = CliRunner()
    result = runner.invoke(hello, ['--name'])
    assert result.exit_code == 0
    assert result.output.strip() == "Hello, Flag!"

def test_hello_with_default_value() -> None:
    runner = CliRunner()
    result = runner.invoke(hello, [])
    assert result.exit_code == 0
    assert result.output.strip() == "Hello, Default!"