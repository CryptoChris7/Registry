# Registry
A contract for making registries which are owned,
with transferable ownership.

Address: `0x48216df3d955d9a8afd28d417ff21d06647e6a6d`

## Basic rules of the contract:

1. All registries are identified by a natural (i.e. positive) number (called it's ID or reg_id).

2. Every registry has an owner, who can mutate it's entries.

3. Every owner has one default registry that can be used for
convenient operations.

4. Every registry can be used for lookups if you know it's ID.

## How stored data is structured:
```python
  sload(reg_id) # The owner of the registry.

  sload(sha3([reg_id, key]:arr)) # The value accosicated with "key" in the registry.

  sload(msg.sender) # The default registry to use for this owner's convenience functions
```
## API
Here are all the functions in the registry contract, with types indicated using Python 3 annotation syntax.
Mutating registry's could theoretically be done with one function, but I decided to split the functions up into three
different groups. The purpose of this is to reduce the occurrence of bugs by making the contract programmer's intentions
more explicit.

### Ownership

* `create_registry() -> int256`
  * Creates a new registry owned by the sender, and returns the registry id. If the sender doesn't already have a default registry, then the new registry is set as it's default.

* `get_owner(reg_id: int256) -> int256`
  * Takes a registry id and returns the address of the owner as an int256.

* `get_default_registry(owner: int256) -> int256`
  * Takes an address as an int256 and returns it's default registry. If the address doesn't have a default registry, the result of this function is zero.

* `set_default_registry(reg_id: int256) -> int256`
  * Takes a registry id the is owned by the sender, and set's the sender's default to it. Returns 1 on success and 0 on failure.

* `transfer_owner(new_owner: int256, reg_id: int256) -> int256`
  * Takes an address and a registry id, and set's the address as the registry's owner. Returns 1 on success, 0 on failure.

### Registration
These functions register a new key-val pair. If the key is already used in the registry, then these functions will
return 0, with the affect of not changing anything. On failure, these functions return 0, on success they return 1.

* `register(key: int256, val: int256) -> int256`
  * Registers a value under the given key at the sender's default registry.

* `register_by_id(reg_id: int256, reg_id: int256, key: int256) -> int256`
  * Registers a value under the given key at the specified registry.

### Updates
These functions change the value of an existing key-val pair in a registry. They return 1 on success and 0 on failure.
Failure modes are 1) not owning the registry you're trying to change and 2) trying to 'update' a key which is not
currently registered.

* `update(key: int256, val: int256) -> int256`
  * Updates the value associated with the key in the msg.sender's default registry.

* `update_by_id(reg_id: int256, key: int256, val: int256) -> int256`
  * Updates the value associated with the key in the specified registry.

### Removal
These functions remove key-val pairs from the registry. If a key isn't used in the registry, then these function fail.
The `remove` and `remove_by_id` functions return statuses similar to their registration counter-parts. They return 0
on failure and 1 on success. In the case of a failure nothing is changed about the registry's state. The `remove2` and
`remove_by_id2` functions are bit different: they return `[1, n]` on success where `n` is the length of their `keys`
input. On failure, they return `[0, i]` where `i` is the index of the key which caused the failure. Every key before
the index `i` in the input are removed, and every key at and after `i` are not. Failure means either that the `i`th key does
not exist in the specified registry or that the `msg.sender` doesn't have permission to modify the registry.

* `remove(key: int256) -> int256`
  * Removes a key-value pair from the default registry.

* `remove_by_id(reg_id: int256, key: int256) -> int256`
  * Removes a key-value pair from the specified registry.

* `remove2(keys: int256[]) -> int256[2]`
  * Removes a list of keys and their associated values from the registry.

* `remove_by_id2(reg_id: int256, keys: int256[]) -> int256[2]`
  * Removes a list of keys from the specified registry.

### Lookup

* `lookup(owner: int256, key: int256) -> int256`
  * Returns the value associated with a key in the owner's default registry.

* `lookup_by_id(reg_id: int256, key: int256) -> int256`
  * Returns the value associated with a key in the specified registry.

## Python Module
`registry.py` contains the necessary pieces of info for using PyContract to interact with the code,
namely the address and the ABI interface.

## Tests
Tests are found in the `test.py` file. To run them, install the dependency using `pip install -r test_requirements.txt`
(ideally in a virtualenv), and then run `py.test test.py`.