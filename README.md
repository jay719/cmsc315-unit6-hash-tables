# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?

I've worked with Python dictionaries before, but this assignment helped me better understand how they function as hash tables. I practiced inserting, retrieving, updating, and deleting key-value pairs while building a simple network device tracking system. It was interesting to see how hashing allows the program to find a device's IP address using its name instead of searching through every entry.

2. What challenges did you encounter, and how did you overcome them?

One thing I had to pay attention to was handling keys that didn't exist in the dictionary. Accessing a missing key directly would cause a KeyError, so I used get() and pop() with default values to avoid errors. Testing these cases helped me understand how to make dictionary operations more reliable.

3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.
   
One thing I had to pay attention to was handling keys that didn't exist in the dictionary. Accessing a missing key directly would cause a KeyError, so I used get() and pop() with default values to avoid errors. Testing these cases helped me understand how to make dictionary operations more reliable.
