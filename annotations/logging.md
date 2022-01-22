# logging.py

The [file](../example_module/logging.py) has some codes that use loguru to do the logging part of the scripts.

## logger_wraps
It's a decorator for python just to log the in and out for some function.

This is inspired by a snippet code from [https://loguru.readthedocs.io/en/stable/resources/recipes.html#logging-entry-and-exit-of-functions-with-a-decorator](https://loguru.readthedocs.io/en/stable/resources/recipes.html#logging-entry-and-exit-of-functions-with-a-decorator).

I have add some things at this decorator:
- Calculate the time to run the function
- Calculate the time to run the function- Add some Python3.10 Type Hinting (inspired by [
- Add some Python3.10 Type Hinting (inspired by [**anthonywritescode** YouTube channel](https://www.youtube.com/watch?v=fwZoxWyMGM8))
  - typing.Callable - [docs](https://docs.python.org/3/library/typing.html#callable)
  - typing.ParamSpec - [docs](https://docs.python.org/3/library/typing.html#typing.ParamSpec)