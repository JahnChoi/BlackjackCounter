# Counts:
# -1 --> Ace, Jack, Queen, King (all worth 10)
#  0 --> 7, 8, 9
# +1 --> 2, 3, 4, 5, 6

# DONE (7/30/17)

class Card:
    def __init__(self, value):
        self._value = value
        if self._value in ['10', 'J', 'Q', 'K', 'A']:
            self._count = -1
        elif self._value in ['7', '8', '9']:
            self._count = 0
        else:
            self._count = 1
            
    def get_value(self):
        return self._value

    def get_count(self):
        return self._count