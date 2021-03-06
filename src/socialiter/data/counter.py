import struct
from enum import IntEnum

import found

from socialiter.base import SpacePrefix


INTEGER_STRUCT = "<q"
ONE = struct.pack(INTEGER_STRUCT, 1)
MINUS_ONE = struct.pack(INTEGER_STRUCT, -1)


class Counter:
    class KIND(IntEnum):
        TOKEN = 0
        WORD = 1

    def __init__(self, kind, name):
        self.kind = kind
        self.name = name

    @found.transactional
    async def get(self, tr):
        key = found.pack((SpacePrefix.COUNTERS.value, self.kind.value, self.name))
        value = await tr.get(key)
        if value is None:
            return 0
        else:
            out = struct.unpack(INTEGER_STRUCT, value)[0]
            return out

    @found.transactional
    async def increment(self, tr):
        # XXX: what happens in case of overflow
        key = found.pack((SpacePrefix.COUNTERS.value, self.kind.value, self.name))
        await tr.add(key, ONE)

    @found.transactional
    async def decrement(self, tr):
        key = found.pack((SpacePrefix.COUNTERS.value, self.kind.value, self.name))
        await tr.add(key, MINUS_ONE)
