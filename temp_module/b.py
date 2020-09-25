from __future__ import print_function

from temp_module.a import A

class B:
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return self.x == other.x
