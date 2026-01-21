import array


class HashTable:
    def __init__(self):
        self.MAX=20
        # Initializing array of 20 elements with None
        self.array=[[] for _ in range(self.MAX)]

    def get_hash(self, key):
        hash=0
        for char in key:
            hash+=ord(char)  # Calculating total sum of ASCII values of characters in the key
        return hash % self.MAX

    def __setitem__(self, key, value):
        index = self.get_hash(key)  # Generating index using hash function for key 'march 6'
        found=False
        for idx, element in enumerate(self.array[index]):
            if len(element)==2 and element[0]==key:
                self.array[index][idx]=(key, value)
                found=True
                break 
        if not found:
            self.array[index].append((key, value))
   
    def __getitem__(self, key):
        index = self.get_hash(key)
        for element in self.array[index]:
            if element[0]==key:
                return element[1]
    
    def __delitem__(self, key):
        index = self.get_hash(key)
        for idx, element in enumerate(self.array[index]):
            if element[0] == key:
                del self.array[index][idx]
                break


t = HashTable()
t['march 6']= 310
t['march 7']= 340
print(t.array)
print(t['march 6'])
del t['march 6']
print(t.array)




