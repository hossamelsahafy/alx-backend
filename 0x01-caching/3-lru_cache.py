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
                last = next(iter(self.cache_data))
                print("DISCARD: {}".format(last))
                del self.cache_data[last]
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)

    def get(self, key):
        """Get Method"""
        return self.cache_data.get(key, None)
