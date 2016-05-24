# Registry
A contract for making registries which are owned,
with transferable ownership.

## Basic rules of the contract:

1. All registries are identified by a natural (i.e. positive) number (called it's ID or reg_id).

2. Every registry has an owner, who can mutate it's entries.

3. Every owner has one default registry that can be used for
convenient operations.

4. Every registry can be used for lookups if you know it's ID.

## How stored data is structured:

  sload(reg_id) # The owner of the registry.

  sload(sha3([reg_id, key]:arr)) # The value accosicated with "key" in the registry.

  sload(msg.sender) # The default registry to use for this owner's convenience functions

