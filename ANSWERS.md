Interview Questions
Be prepared to demonstrate your understanding of this week's concepts by answering questions on the following topics. You might prepare by writing down your answers beforehand.

1) Hashing functions

The hash() function returns the hash value of the object if it has one. Hash values are integers. They are used to quickly compare dictionary keys during a dictionary lookup. Objects can implement the __hash__() method.

When we talk about hash tables, we're actually talking about dictionary. While an array can be used to construct hash tables, array indexes its elements using integers. ... Dictionaries in Python are implemented using hash tables. It is an array whose indexes are obtained using a hash function on the keys.


2) Collision resolution

Collision

A collision occurs when two items/values get the same slot/index, i.e. the hashing function generates same slot number for multiple items. If proper collision resolution steps are not taken then the previous item in the slot will be replaced by the new item whenever the collision occurs.

Collision Resolution

There are generally two ways to resolve a collision:

	1. Linear Probing - One way to resolve collision is to find another open slot whenever there is a collision and store the item in that open slot. The search for open slot starts from the slot where the collision happened. It moves sequentially through the slots until an empty slot is encountered. The movement is in a circular fashion. It can move to the first slot while searching for an empty slot. Hence, covering the entire hash table. This kind of sequential search is called Linear Probing.
	
	2. Chaining - The other way to resolve collision is Chaining. This allows multiple items exist in the same slot/index. This can create a chain/collection of items in a single slot. When the collision happens, the item is stored in the same slot using chaining mechanism.

3) Performance of basic hash table operations
	#Create Hash Table 
	hash_table = [None] * 10
	print (hash_table) 
	
	#Insert into Hash Table 
	def insert(hash_table, key, value):
    hash_key = hashing_func(key)
    hash_table[hash_key] = value 
 
	insert(hash_table, 10, 'Nepal')
	print (hash_table)
	
	#Create an empty hash table 
	hash_table = [[] for _ in range(10)]
	print (hash_table)
	
4) Load factor 
    May be described as how much data we have in our array. As we load data into our array, we need to know how full the array is relative to how large it is. Lambda = number of entries in data structure / size of array. if we have an array with 25 full slots with a capacity of 100, our load factor is .25. 

5) Automatic resizing

    A dynamic array is similar to an array, but with the difference that its size can be dynamically modified at runtime.

6) Various use cases for hash tables

1. Cryptography: Verify file integrity with a hash checksum.
2. Database indexing.
