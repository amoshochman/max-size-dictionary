# max-size-dictionary

### A Python implementation of a Dictionary with max size: when attempting to enter one more element than the allowed ones, the least recently used element is deleted.

Both reading from and writing to the dictionary takes O(1) amortized time. </br>

In order to achieve that, for every received pair <key, value> we store <key, node>, where node includes the given value and also "next"+"previous". That way we have actually a linked list. In O(1), for each operation, we just move to the tail of the list the accessed element.