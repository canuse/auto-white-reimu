import bisect
import re
from typing import Iterable

from tile.set import TileSet
from tile.tile import Tile

_tile_group_regex = re.compile(r"[0-9]+[%s]" % (''.join(Tile.SUIT | Tile.HONOR)))


def tiles_from_string(token: str) -> Iterable[Tile]:
    for group in _tile_group_regex.finditer(token):
        group_value = group.group(0)
        numbers, color = group_value[:-1], group_value[-1]
        yield from (Tile(int(number), color) for number in numbers)


def tile_set_from_string(token: str) -> TileSet:
    tile_set = TileSet(tiles_from_string(token))
    tile_set.re_sort()
    return tile_set


def distinct(iterable: Iterable):
    unique = []
    for item in iterable:
        index = bisect.bisect_left(unique, item)
        if index >= len(unique) or unique[index] != item:
            yield item
            unique.insert(index, item)
