import click
from typing import Any, Optional

def option(*param_decls: str, is_flag: bool = False, flag_value: Optional[Any] = None, default: Optional[Any] = None, **kwargs: Any) -> Any:
    """Decorator to define a command-line option."""
    
    def _option(f: Any) -> Any:
        # Custom handling for flag_value when is_flag is False
        if is_flag and flag_value is not None:
            # Adjust the default behavior to allow flag_value to be returned
            kwargs['default'] = flag_value
        
        # Call the original Click option decorator
        return click.option(*param_decls, is_flag=is_flag, flag_value=flag_value, default=default, **kwargs)(f)

    return _option

@click.command()
@option("--name", is_flag=False, flag_value="Flag", default="Default")
def hello(name: str) -> None:
    click.echo(f"Hello, {name}!")