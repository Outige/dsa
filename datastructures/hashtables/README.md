# Hash Tables

A hash table (HT) is an abstraction on top of an array. Making use of a `hash function` for lookup and indexing.

There are implementations of HTs that can take in arbitrary data but for explanation in this README as well as the code examples. I will be using a simple case of storing string keys.



# Hash function

It is a function that takes in the data that will be stored and returns an index where the data will be stored in the underlying array

![Simple example](https://user-images.githubusercontent.com/41017214/223716291-138f6b46-e449-445a-9592-d29df3499e8e.png)


### Qualities of a good hash function

- Deterministic
- 0 <= Index < len(HT)
- Uses all of the data to calculate the hash
- Uses no additional data to calculate hash
- Even distribution of keys among the indexes of the underlying array



# Collisions

A collision occurs when two different keys hash to the same index of the array.


## Open addressing

Open addressing is one of the 2 classes of solutions to collision handling in a HT. The other being [Chaining](##Chaining). It should be noted that the collision detection solution dictates the underlying data structure used for the array of the HT.

In open addressing. The underlying structure of the HT is an array and each address in the array can only hold 1 entry of data.

In open addressing when there is a collisions, a walk is performed until the next open space is found in the HT. This walk can be implemented in various ways as discussed in the next 2 sub sections.


### Linear probing

In linear probing. When there is a collision. The solution is to loop over the rest of the array until an index is found to be un-used. This search will wrap around if the end of the array is reached.

One problem this introduces is `clustering`. This is a problem where large groups of indexes form. Making future collisions more likely, making longer chains and causing a vicious cycle.


### Quadratic probing

An improvement on linear probing. Where the probing step size doubles each time.

## Chaining

In chaining, the underlying structure of the HT is an array of linked lists (LL). In this case when a collision occurs, the key is appended to the LL at the index specified by the hash function.

This key can either be added to the head or the tail. Which is implementation dependent.



# Rehashing

Rehashing / resifting is a process where a hash table has gotten inefficient at it's current size and so a new table must be created of a new size. Usually double the pervious table size.

Then all the elements in the old table must be rehashed into the new table.


## Load factor

Load factor is a ratio indicating how full the hash table is.

```
    LoadFactor = m/n
```

Where m is the number of elements in the HT and n is the size of the HT.

Usually a constant LF is picked as a threshold. If this threshold is reached, then the table will be rehashed.

A common LF threshold is 0.75 (in java I believe).

In a chaining HT LF can tend to infinity if there is no rehashing. This number can only equal 1 in a table using linear probing



# Performance

HTs generally should only be used when the data can be unsorted. If the data is sorted the performance of the HT is similar to that of a LL.


## Average

- Insertion: O(1)
- Deletion: O(1)
- Lookup: O(1)

These are generally the metrics people think about when refiring to HT performance.


## Worst

- Insertion: O(n)
    - I believe O(1) if you insert at the head not the tail
- Deletion: O(n)
- Lookup: O(n)

Where n is the number of elements to hash.


## Improvements to performance

The best way to improve the performance of an HT is by reducing the number of collisions. This can be achieved by (but maybe not limited to)...


### Improving the hashing algorithm

With a better algorithm that more evenly distributes keys.

There is a concept of `perfect hashing`. This is a hashing algorithm that ensures no collisions. This is only possible if all keys are known ahead of time.

![code](https://user-images.githubusercontent.com/41017214/223724219-27667a10-ec36-4d62-9d6f-bb217c1aa366.png)


### Increasing the size of the array / lower LF threshold

With more open spaces there is less chance for collisions.


# Sources
- [Hash Tables - CS50 Shorts](https://www.youtube.com/watch?v=nvzVHwrrub0)
- [Big O cheat sheet](https://www.bigocheatsheet.com/
- https://www.youtube.com/watch?v=2Qhc-uSUCL4)
