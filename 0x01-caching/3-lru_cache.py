#!/usr/bin/env python3
"""
    LRU Caching
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """Define Class LRUCache Class"""

    def __init__(self):
        """__init__ Method"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Put Method"""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                last = self.cache_data.popitem(last = False)
                print("DISCARD: {}".format(last[0]))
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)

    def get(self, key):
        """Get Method"""
        return self.cache_data.get(key, None)
