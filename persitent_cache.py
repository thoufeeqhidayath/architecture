from diskcache import Cache

import os
class PersistentCache:
    def __init__(self, directory_path) -> None:
        if directory_path:
            self.directory_path = directory_path
        else:
            raise Exception("directory path cannot be empty")


    def set(self, key, value):
        with Cache(os.path.abspath(self.directory_path)) as cache:
            cache.set(key, value, retry=True)

    def get(self,key):
        with Cache(os.path.abspath(self.directory_path)) as cache:
             return cache.get(key)

    def remove(self,key):
        with Cache(os.path.abspath(self.directory_path)) as cache:
             return cache.pop(key,None)

