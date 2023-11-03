"""
Написать программу, позволяющую конкатенировать два языка.
Входные данные: 
    Цепочки языка L1, цепочки языка L2. Количество цепочек в языке <= 10000, длина цепочки <= 100
Выходные данные: 
    Цепочки получившегося языка L1L2.
"""


class Handler:
    """
    Handler class created for a more convenient code structure.
    """

    @staticmethod
    def _max_chainsize(lang: list) -> int:
        max_length = 0
        for chain in lang:
            if len(chain) > max_length:
                max_length = len(chain)

        return max_length

    def concatenate(self, l1: list, l2: list) -> list:
        """
        Concatenate chains of 2 languages

        Args:
            l1 (list): A langauge chains
            l2 (list): An other langauge chains

        Returns:
            list: Concatenated lang chains (l1l2)
        """

        expressions = [
            (len(l1) <= 10000),
            (len(l2) <= 10000),
            (self._max_chainsize(l1) <= 100),
            (self._max_chainsize(l2) <= 100),
        ]
        if not all(expressions):
            return ['The conditions of the task are violated']

        l1l2 = []
        for chain1 in l1:
            for chain2 in l2:
                l1l2.append(chain1 + chain2)

        return l1l2


Concatenator = Handler()

lang1 = ['a', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj']
lang2 = ['A', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG', 'HH', 'II', 'JJ']


result = Concatenator.concatenate(lang1, lang2)
print(result)
