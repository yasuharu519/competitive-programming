from collections import defaultdict


class FrequencyTracker:

    def __init__(self):
        self.d = defaultdict(int)
        self.freq = defaultdict(set)

    def add(self, number: int) -> None:
        if number in self.d:
            prev = self.d[number]
            self.d[number] += 1
            if prev > 0:
                self.freq[prev].remove(number)
            self.freq[prev + 1].add(number)
        else:
            self.d[number] = 1
            self.freq[1].add(number)

    def deleteOne(self, number: int) -> None:
        if number in self.d and self.d[number] > 0:
            prev = self.d[number]
            self.d[number] -= 1
            self.freq[prev].remove(number)
            if prev - 1 > 0:
                self.freq[prev - 1].add(number)

    def hasFrequency(self, frequency: int) -> bool:
        if frequency in self.freq and len(self.freq[frequency]) > 0:
            return True
        return False


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)

if __name__ == "__main__":
    traq = FrequencyTracker()
    traq.deleteOne(5)
    traq.hasFrequency(1)
    traq.hasFrequency(1)
    traq.deleteOne(3)
    traq.hasFrequency(1)
    traq.hasFrequency(1)
    traq.add(7)
    traq.deleteOne(7)
    traq.deleteOne(7)