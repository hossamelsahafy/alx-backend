#!/usr/bin/env python3
"""
    LFU Caching
"""
from base_caching import BaseCaching


class LFUCache (BaseCaching):
    """
        Defien Class LFUCache
    """
    def __init__(self):
        super().__init__()
        self.freq = {}
        self.freq_of_keys = {}
        self.min_freq = 0

    def put(self, key, item):
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if len(self.cache_data) > 0:
                min_freq_keys = self.freq.get(self.min_freq, [])
                if min_freq_keys:
                    discard_key = min_freq_keys.pop(0)
                    del self.cache_data[discard_key]
                    del self.freq_of_keys[discard_key]
                    print(f"DISCARD: {discard_key}")

        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq_of_keys[key] += 1
        else:
            self.cache_data[key] = item
            self.freq_of_keys[key] = 1
            self.freq_of_keys[key] = 1
            self.min_freq = 1

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None

        self.freq_of_keys[key] += 1
        return self.cache_data[key]
