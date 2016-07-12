from serpent_tests import ContractTest, Accounts


def test_registry():
    myTest = ContractTest('registry.se')
    # Use a different sender sometimes to show the ownership stuff.
    for i, account in enumerate(Accounts[:3]):
        reg_id = i + 1
        foo_val = 2**(i+1)
        bar_val = 3**(i+1)
        kwds = {'sender':account.privkey}
        myTest.create_registry(kwds=kwds, compare=reg_id) # creates a registry for the account
        myTest.get_owner(args=(reg_id,), compare=account.as_int, kwds=kwds) # the registry is owned by the account
        myTest.get_default_registry(args=(account.as_int,), compare=reg_id, kwds=kwds) # the account's default registry
        myTest.register(args=('foo', foo_val), compare=1, kwds=kwds) # adds a new key
        myTest.register(args=('foo', foo_val - 1), compare=0, kwds=kwds)  # can't update with register
        myTest.register_by_id(args=(reg_id, 'bar', bar_val), compare=1, kwds=kwds) # registers using id
        myTest.register_by_id(args=(reg_id, 'bar', bar_val - 1), compare=0, kwds=kwds) # can't update
        myTest.lookup(args=(account.as_int, 'foo'), compare=foo_val, kwds=kwds) # looks up the val in foo
        myTest.lookup_by_id(args=(reg_id, 'bar'), compare=bar_val, kwds=kwds) # looks up the val in bar
        myTest.update(args=('foo', foo_val - 1), compare=1, kwds=kwds) # updates foo
        myTest.update(args=('foo1', foo_val), compare=0, kwds=kwds)  #can't register with update
        myTest.update_by_id(args=(reg_id, 'bar', bar_val - 1), compare=1, kwds=kwds) # updates bar
        myTest.update_by_id(args=(reg_id, 'bar1', bar_val), compare=0, kwds=kwds) # can't register here either
        myTest.state.mine(1, coinbase=account.address)

    a0, a1, a2 = Accounts[:3]
    a0_send = {'sender': a0.privkey}
    a1_send = {'sender': a1.privkey}
    a2_send = {'sender': a2.privkey}
    myTest.transfer_owner(args=(a0.as_int, 2), compare=1, kwds=a1_send)  #a1 transfered reg_id 2 to a0
    myTest.get_default_registry(args=(a1.as_int,), compare=0) #a1 no longer has reg2 as default
    myTest.get_owner(args=(2,), compare=a0.as_int) #a0 now owns reg 2
    myTest.lookup(args=(a0.as_int, 'foo'), compare=1) #a0 still uses reg 1 by default
    myTest.set_default_registry(args=(2,), compare=1, kwds=a0_send) #set new default to reg 2
    myTest.lookup(args=(a0.as_int, 'foo'), compare=3) #now a0 uses reg 2
    myTest.remove(args=('foo',), compare=1, kwds=a0_send) #a0 removes foo from reg 2
    myTest.lookup(args=('foo',), compare=0) #lookup returns 0
    myTest.lookup_by_id(args=(2, 'bar'), compare=8)
    myTest.remove_by_id(args=(2, 'bar'), compare=1, kwds=a0_send) # a0 removes bar from reg 2
    myTest.lookup_by_id(args=(2, 'bar'), compare=0) # foo removed from reg 1, returns 0
    myTest.remove_by_id2(args=(1, ['foo', 'bar']), compare=[1, 2], kwds=a0_send) # a0 removes foo and bar from reg 1
    myTest.lookup_by_id(args=(1, 'foo'), compare=0) # lookup now returns 0
    myTest.remove2(args=(['foo', 'bar'],), compare=[1, 2], kwds=a2_send) # a2 removes foo and bar from reg 3
    myTest.lookup_by_id(args=(3, 'foo'), compare=0)
    myTest.lookup_by_id(args=(3, 'bar'), compare=0)

