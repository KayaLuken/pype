class Placeholder:
    def __repr__(self):
        return '_'

    def __str__(self):
        return '_'


_ = Placeholder()

__all__ = ['_']
