import functools

from loguru import logger
from datetime import timedelta
from typing import ParamSpec
from typing import Callable
from typing import TypeVar

from timeit import default_timer as timer

P = ParamSpec("P")
R = TypeVar("R")


def logger_wraps(
    *,
    entry: bool = True,
    exit: bool = True,
    level: str = "DEBUG",
):
    def wrapper(func: Callable[P, R]) -> Callable[P, R]:
        func_name = func.__name__

        @functools.wraps(func)
        def wrapped(*args: P.args, **kwargs: P.kwargs) -> R:
            logger_ = logger.opt(depth=1)
            if entry:
                logger_.log(level, f"Entering `{func_name}` (args={args}, kwargs={kwargs})")

            start_time = timer()
            result = func(*args, **kwargs)
            end_time = timer()

            if exit:
                time_taken = timedelta(seconds=end_time - start_time)
                logger_.log(level, f"Exiting `{func_name}` (time taken: {time_taken}) (result={result})")

            return result

        return wrapped

    return wrapper
