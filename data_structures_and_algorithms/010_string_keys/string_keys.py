"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        idx = self.calculate_hash_value(string)
        if idx > -1:
            self.table[idx] = string

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        idx = self.calculate_hash_value(string)
        if idx > -1 and self.table[idx] == string:
            return idx
        return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        result = -1
        if len(string) > 0:
            result = ord(string[0]) * 100
            if len(string) > 1:
                result += ord(string[1])

        return result
    
# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8089
print(hash_table.calculate_hash_value('PYTHON'))

# Test lookup edge case
# Should be -1
print(hash_table.lookup('PYTHON'))

# Test store
hash_table.store('PYTHON')
# Should be 8089
print(hash_table.lookup('PYTHON'))

# Test store edge case
hash_table.store('PYTHON3')
# Should be 8089
print(hash_table.lookup('PYTHON3'))
