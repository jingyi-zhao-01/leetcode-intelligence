import logging
import time
from functools import wraps
import asyncio

logger = logging.getLogger(__name__)


def _format_arg(arg):
    """Helper to format a single argument for logging."""
    if isinstance(arg, list) and len(arg) > 5:
        return f"list(len={len(arg)})"

    arg_repr = repr(arg)
    if len(arg_repr) > 150:
        return arg_repr[:150] + "..."
    return arg_repr


def log_function_calls(func):
    """
    A decorator to log function success and execution time, including parameters.
    Handles both sync and async functions correctly.
    """

    @wraps(func)
    async def async_wrapper(*args, **kwargs):
        start_time = time.time()
        log_args = args
        if "." in func.__qualname__ and args:
            log_args = args[1:]
        arg_str = ", ".join(_format_arg(a) for a in log_args)
        kwarg_str = ", ".join(f"{k}={_format_arg(v)}" for k, v in kwargs.items())
        all_args = ", ".join(filter(None, [arg_str, kwarg_str]))

        try:
            result = await func(*args, **kwargs)
            duration = time.time() - start_time
            logger.info(f"{func.__name__}({all_args}) success (took {duration:.4f}s)")
            return result