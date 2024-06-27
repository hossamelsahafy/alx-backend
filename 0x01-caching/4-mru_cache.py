#!/usr/bin/env python3
"""
    MRU Caching
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Define Class MRUCache"""
    def __init__(self):
        """__init__ Method"""
        super().__init__()
        self.MRU_keys = []

    def put(self, key, item):
        """Put Method"""
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS\
                    and key not in self.MRU_keys:
                d_k = self.MRU_keys.pop()
                del self.cache_data[d_k]
                print("DISCARD: {}".format(d_k))
            if key in self.MRU_keys:
                self.MRU_keys.remove(key)
            self.cache_data[key] = item
            self.MRU_keys.append(key)

    def get(self, key):
        """Get Method"""
        if key in self.MRU_keys:
            self.MRU_keys.remove(key)
            self.MRU_keys.append(key)
        value = self.cache_data.get(key)
        return value
