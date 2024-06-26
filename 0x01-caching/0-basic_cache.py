#!/usr/bin/env python3
"""
    Basic dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Define Basicache Class"""
    def put(self, key, item):
        """Put Method"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get Method"""
        return self.cache_data.get(key, None)
