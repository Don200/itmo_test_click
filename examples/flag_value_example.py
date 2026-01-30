import click

@click.command()
@click.option("--name", is_flag=False, flag_value="Flag", default="Default")
def hello(name: str) -> None:
    """Greets the user with the provided name or a default value."""
    click.echo(f"Hello, {name}!")

if __name__ == "__main__":
    hello()