#!/usr/bin/env python3
'''
Task 1: 
'''


from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''
       `BaseCaching` and is a caching system.
    '''

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''
        `item`  `key`
        '''

        if key is None or item is None:
            return

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item

    def get(self, key):
        '''
        return the value in `self.cache_data` linked to `key`
        '''
        return self.cache_data.get(key, None)
