from collections import defaultdict

class TimeMap:
    """ Implement a time-based key-value data structure that supports: Storing multiple values for the same key at specified time stamps
Retrieving the key's value at a specified timestamp
Implement the TimeMap class: TimeMap() Initializes the object.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns the most recent value of key if set was previously called on it and the most recent timestamp for that key prev_timestamp is less than or equal to the given timestamp (prev_timestamp <= timestamp). If there are no values, it returns "".
Note: For all calls to set, the timestamps are in strictly increasing order.

    Returns:
        _type_: _description_
    """
# create a heap for effecient times
    def __init__(self):
        self.store = defaultdict(list) # {key, heap}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
        #heapq.heappush(self.store[key], (timestamp, value))


    # O(log m) space
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        # O(log m) time and O(1) space solution (Binary search)
        l, r = 0, len(self.store[key]) - 1
        res = ""

        while l <= r:
            m = l + ((r - l) // 2)
            if self.store[key][m][0] > timestamp:
                r = m - 1
            elif self.store[key][m][0] < timestamp:
                l = m + 1
                res = self.store[key][m][1]
            else: # if the timestamp is equal
                return self.store[key][m][1]


        return res

        # Heaps
        # O(logm) time and space solution
        # if key not in self.store:
        #     return ""

        # buffers = [] # (timestamp, key)

        # while self.store[key] and self.store[key][0][0] <= timestamp:
        #     item = heapq.heappop(self.store[key])
        #     buffers.append(item)

        # for item in buffers:
        #     heapq.heappush(self.store[key], item)
            
        # return buffers[-1][1] if buffers else ""

