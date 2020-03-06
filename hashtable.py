from linkedlist import LinkedList

class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]
        self.size = 0

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        Running time(Best Case): O(N) Because each bucket has 1 itme
        Running time(Average Case): O(N) Because have to traverse the list of buckets and the items within each bucket"""

        # Collect all keys in each bucket

        all_keys = []
        # Loop through the buckets in the hashtable
        for bucket in self.buckets:
            for key, value in bucket.items(): # Loop through all the keys and vaules in one bucket
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Running time(Best Case): O(N) Because each bucket has 1 item
        Running time(Average Case): O(N) Because have to traverse the list of buckets and the items within each bucket"""
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket

        # Function very similar to the keys() within this class
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        Running time(Best Case): O(N) or O(b*L) Because each bucket has 1 item
        Running time(Average Case): O(N) Because each bucket has many items"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Running time(Average Case): O(N) or O(b*L) Because have to loop through the items in buckets
        OR Running time(Best Case): O(1) Because only have to get the size from the class property"""

        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket

        return self.size

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Running time(Average Case): O(L) or O(n/b) When each bucket has multiple items
        Running time(Best Case): O(1) When each bucket has only 1 item"""

        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket

        bucket = self.buckets[self._bucket_index(key)] # Finds the bucket (or it's index)

        if bucket.find(lambda item: item[0] == key): # If item is found in the bucket
            return True
        return False # Item is not found in bucket

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Running time(Average Case): O(L) or O(n/b) When there are multiple items in a bucket
        Running time(Best Case): O(1) When there is one/first item in bucket"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, return value associated with given key
        # TODO: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))

        bucket = self.buckets[self._bucket_index(key)] # Finds bucket

        found_item = bucket.find(lambda item: item[0] == key) # Finds the item in the bucket and assigns it to found_item

        if found_item: # If item is found, return the value of it, which locates at index 1
            return found_item[1]
        else:
            raise KeyError(f'Key not found: {key}')


    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Running time(Average Case): O(L) or O(n/b) When there are multiple items in a bucket
        Running time(Best Case): O(1) When there is one/first item in bucket"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket

        bucket = self.buckets[self._bucket_index(key)] # Finds the bucket with given key

        found_item = bucket.find(lambda item: item[0] == key) # Finds the item in the bucket and assigns it to item

        if found_item:
            bucket.delete((found_item[0], found_item[1])) # Since tuple must delete and then append
            bucket.append((key, value))
            # OR can use replace function
            # bucket.replace(found_item, (key, value))
        else:
            bucket.append((key, value))
            self.size += 1


    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        Running time(Average Case): O(L) or O(n/b) When there are multiple items in a bucket
        Running time(Best Case): O(1) When there is one/first item in bucket"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))

        # Run Time: O(1)
        bucket = self.buckets[self._bucket_index(key)] # Finds the bucket with given key
        # Run Time: O(L) b/c, on average, it's L = (total num of items)/(total num of buckets) OR O(1), if only one/first item in the bucket
        found_item = bucket.find(lambda item: item[0] == key) # Finds the item in the bucket and assigns it to found_item

        # Run Time: O(1)
        # If item found, delete it, else raise error if not found
        if found_item:
            bucket.delete(found_item)
            self.size -= 1
        else:
            raise KeyError("Key not found: {}".format(key))


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
