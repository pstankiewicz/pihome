try:
    from .local import *
except ImportError as e:
    print(e)
    from .base import *
