import collections

from common import logger

LOG = logger.getLogger('deck')

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


if __name__ == '__main__':

    card = Card('7', 'diamonds')
    LOG.info("card is %s. [card.rank = %s][card.suit = %s]", card, card.rank, card.suit)

    french_deck = FrenchDeck()
    LOG.info('len of french_deck is %s', len(french_deck))

    # 对应的是__getitem__
    LOG.info('french_deck[0] = %s', french_deck[0])

    # 从sequence中随机获取一个元素 random.choice
    from random import choice
    LOG.info('random %s', choice(french_deck))
