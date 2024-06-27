#!/usr/bin/env python3
"""
    LRU Caching
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    def __init__(self):
        """__init__ Method"""
        super().__init__()

    def put(self, key, item):
        """Put Method"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last = next(iter(self.cache_data))
            del self.cache_data[last]
            print(f"DISCARD: {last}")

    def get(self, key):
        """Get Method"""
        if key is None or key not in self.cache_data:
            return None
        value = self.cache_data.pop(key)
        self.cache_data[key] = value
        return value
