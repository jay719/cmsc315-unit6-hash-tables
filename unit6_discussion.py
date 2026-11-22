
"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    devices = {}

    # Dictionaries use hashing to store and find values using unique keys.
    # Each device name is a key, and its IP address is the value.
    devices["Router"] = "192.168.1.1"
    devices["Desktop"] = "192.168.1.10"
    devices["Laptop"] = "192.168.1.11"
    devices["Printer"] = "192.168.1.12"
    devices["Smart TV"] = "192.168.1.13"

    print("\n=== INSERT OPERATIONS ===")
    for name, ip in devices.items():
        print(f"{name}: {ip}")

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")

    # A dictionary can quickly find a value using its key.
    print("Router IP:", devices["Router"])
    print("Desktop IP:", devices["Desktop"])

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("Before update:", devices)

    # Assigning a new value to an existing key replaces the old value.
    devices["Desktop"] = "192.168.1.20"

    print("After update:", devices)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("Before deletion:", devices)

    # pop() removes the key and its associated value.
    devices.pop("Printer")

    print("After deletion:", devices)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")

    # get() returns a default message instead of raising a KeyError.
    print("Missing device:", devices.get("Tablet", "Device not found"))

    # pop() with a default safely handles a key that does not exist.
    print("Delete missing device:", devices.pop("Tablet", "Device not found"))

    # An empty dictionary contains no device records.
    empty_devices = {}
    print("Empty dictionary:", empty_devices)
    print("Is empty:", len(empty_devices) == 0)


if __name__ == "__main__":
    main()
