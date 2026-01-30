import click
from typing import Any, Callable, Optional

def custom_option(*args, is_flag: bool = False, flag_value: Optional[Any] = None, **kwargs) -> Callable:
    """Custom option decorator to handle flag_value correctly."""
    def decorator(f: Callable) -> Callable:
        # Wrap the original option functionality
        original_option = click.option(*args, is_flag=is_flag, **kwargs)

        # Define a new function that checks for the flag_value
        def wrapper(*args, **kwargs):
            # Check if the flag is provided without an argument
            if is_flag and flag_value is not None and kwargs.get(args[0].name) is None:
                kwargs[args[0].name] = flag_value
            return original_option(f)(*args, **kwargs)

        return wrapper

    return decorator