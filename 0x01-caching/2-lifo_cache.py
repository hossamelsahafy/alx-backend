#!/usr/bin/env python3
"""
    LIFO Caching
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Define Class LIFOCache"""
    def __init__(self):
        """__init__ Method"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Put Method"""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                last = self.cache_data.popitem(last=True)
                print("DISCARD: {}".format(last[0]))
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        return self.cache_data.get(key, None)
