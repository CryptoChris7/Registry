from serpent_tests import Tester

def main():
    myTest = Tester('registry.se')
    a1 = myTest.accounts[0]
    a2 = myTest.accounts[1]
    a2Send = {'sender':a2.privkey}
    test_cases = [('register', ('foo', 123), {}, 1),
                  ('register', ('foo', 456), a2Send, 1),
                  ('get_val', (a1.address_as_int, 'foo'), {}, 123),
                  ('get_val', (a2.address_as_int, 'foo'), a2Send, 456),
                  ('get_own_val', ('foo',), {}, 123),
                  ('register', ('foo', 789), {}, 0),
                  ('get_own_val', ('foo',), {}, 123),
                  ('update', ('foo', 789), {}, 1),
                  ('get_own_val', ('foo',), {}, 789),
                  ('unregister', ('foo',), {}, 1)]
    myTest.run_tests(test_cases)

if __name__ == '__main__':
    main()
