from serpent_tests import ContractTester, Accounts, Assert

class TestRegistry:
    def test(self):
        myTest = ContractTester('registry.se')
        # Use a different sender sometimes to show the ownership stuff.
        for i, account in enumerate(Accounts):
            sender = {'sender':account.prikvey}
            myTest.create_registry(kwds=sender, expects=(i+1))
        
        for i, account in enumerate(Accounts):
            pass
        myTest.register(args=('foo', 123), expects=1)
        myTest.register(args=('foo', 456), expects=1, kwds=a1send)
        myTest.lookup(args=(a0.as_int, 'foo'), expects=123)
        myTest.lookup(args=(a1.as_int, 'foo'), expects=456)
        myTest.update(args=('foo', 789), expects=1)
        myTest.update(args=('bar', 1337), expects=0)
'''
    test_cases = [('create_registry', (), {}, 1),
                  ('create_registry', (), a2Send, 2),
                  ('register', ('foo', 123), {}, 1),
                  ('register', ('foo', 456), a2Send, 1),
                  ('lookup', (a1.address_as_int, 'foo'), {}, 123),
                  ('lookup', (a2.address_as_int, 'foo'), a2Send, 456),
                  ('my_lookup', ('foo',), {}, 123),
                  ('register', ('foo', 789), {}, 0),
                  ('my_lookup', ('foo',), {}, 123),
                  ('update', ('foo', 789), {}, 1),
                  ('my_lookup', ('foo',), {}, 789),
                  ('remove', ('foo',), {}, 1)]

    myTest.run_tests(test_cases)

if __name__ == '__main__':
    main()
'''
