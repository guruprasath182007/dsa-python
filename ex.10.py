import sys

class MaxHeap:
    def __init__(self, cap):
        self.cap = cap
        self.n = 0
        self.a = [0] * (cap + 1)
        self.a[0] = sys.maxsize
        self.root = 1

    def parent(self, i):
        return i // 2

    def swap(self, i, j):
        self.a[i], self.a[j] = self.a[j], self.a[i]

    def insert(self, val):
        if self.n >= self.cap:
            print("Heap is full. Cannot insert.")
            return
        self.n += 1
        self.a[self.n] = val
        i = self.n
        while self.a[i] > self.a[self.parent(i)]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

if __name__ == "__main__":
    print("Inserting elements into the maxHeap:")
    h = MaxHeap(15)
    vals = [5,8,2,20,17,32,15,12,22]

    for val in vals:
        print(f"Inserting {val}")
        h.insert(val)
       
    print("\nFinal array representation after all insertions:")
    print(h.a[1 : h.n + 1])
