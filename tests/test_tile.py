from unittest import TestCase

from tile import tile
from tile import utils


class TestTile(TestCase):
    def test_count(self):
        hand1 = utils.tile_set_from_string("1234555s1234m4567p123s5547z")
        self.assertEqual(hand1[tile.Tile(1, 's')], 2)
        self.assertEqual(hand1[tile.Tile(4, 's')], 1)
        self.assertEqual(hand1[tile.Tile(5, 's')], 3)
        self.assertEqual(hand1[tile.Tile(5, 'p')], 1)

    def test_tile_ordering(self):
        hand1 = utils.tile_set_from_string("123456789m123456789s123456789p1234567z")
        assert sorted(hand1.keys()) == list(
            utils.tile_set_from_string("123456789m123456789p123456789s1234567z").keys())
