#!/usr/bin/env python3
"""
    FIFO caching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
        Define Class FIFO caching
    """
    def __init__(self):
        """__init__ Method"""
        super().__init__()

    def put(self, key, item):
        """Put Method"""
        if key is not None and item is not None:
            if len(self.cache_data) > self.MAX_ITEMS:
                old = next(iter(self.cache_data))
                print("DISCARD: {}".format(old))
                del self.cache_data[old]
            self.cache_data[key] = item

    def get(self, key):
        """Get Method"""
        return self.cache_data.get(key, None)
