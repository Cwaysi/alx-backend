#!/usr/bin/env python3

'''
dictionary
'''


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''
    A class `Ba
    '''

    def put(self, key, item):
        '''
        `key`
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''
        returnhe_data` linked to `key`
        '''

        return self.cache_data.get(key, None)
