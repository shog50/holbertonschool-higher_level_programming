#!/usr/bin/env python3
"""
CountedIterator tracks iteration count.
"""


class CountedIterator:
    """Iterator that counts items fetched."""

    def __init__(self, iterable):
        """Initialize iterator and counter."""
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Return next item, increment count."""
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration("No more items.")

    def get_count(self):
        """Return number of items iterated."""
        return self.count


if __name__ == "__main__":
    """Test CountedIterator."""
    data = [1, 2, 3, 4]
    counted_iter = CountedIterator(data)

    try:
        while True:
            item = next(counted_iter)
            print(f"Got {item}, total {counted_iter.get_count()} items.")
    except StopIteration as e:
        print(e)
