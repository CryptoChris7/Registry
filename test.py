from serpent_tests import Tester

def main():
    myTest = Tester('registry.se')
    a1 = myTest.accounts[0]
    a2 = myTest.accounts[1]
    a2Send = {'sender':a2.privkey}
    test_cases = [('register', ('foo', 123), {}, 1),
                  ('register', ('foo', 456), a2Send, 1),
                  ('lookup', (a1.address_as_int, 'foo'), {}, 123),
                  ('lookup', (a2.address_as_int, 'foo'), a2Send, 456),
                  ('my_lookup', ('foo',), {}, 123),
                  ('register', ('foo', 789), {}, 0),
                  ('my_lookup', ('foo',), {}, 123),
                  ('update', ('foo', 789), {}, 1),
                  ('my_lookup', ('foo',), {}, 789),
                  ('remove', ('foo',), {}, 1),
                  ('multiregister', (['bar', 'baz'], [100, 200]), {}, [1, 0, 0]),
                  # foo was removed earlier
                  ('multiremove', (['foo', 'baz'],), {}, [0, int('foo'.encode('hex'), 16)]),
                  ('my_lookup', ('baz',), {}, 200),
                  ('multiupdate', (['bar', 'baz'], [110, 210]), {}, [1, 0, 0])]

    myTest.run_tests(test_cases)

if __name__ == '__main__':
    main()
