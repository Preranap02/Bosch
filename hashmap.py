class SimpleHashMap:
    def __init__(self, capacity=10):
        self.capacity = capacity 
        self.buckets = [[] for _ in range(capacity)]

    def _hash(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        index = self._hash(key)
        bucket = self.buckets[index]
        for idx, (k, v) in enumerate(bucket):
            if k == key:
                bucket[idx] = (key, value)
                return
        bucket.append((key, value)) 

    def get(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        return None 

    def remove(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
        for idx, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[idx]
                return True
        return False 

    def __str__(self):
        items = []
        for bucket in self.buckets:
            items.extend(bucket)
        return '{' + ', '.join(f"{k}: {v}" for k, v in items) + '}'
hashmap = SimpleHashMap()
hashmap.put("apple", 90)
hashmap.put("banana", 70)
print("Initial hashmap:", hashmap)
hashmap.put("apple", 100)  
print("After updating apple:", hashmap)  # {'apple': 10, 'banana': 5}
print("Get apple:", hashmap.get("apple"))
print("Get orange:", hashmap.get("orange"))
hashmap.remove("banana")
print("After removing banana:", hashmap) 