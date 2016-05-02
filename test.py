from serpent_tests import Tester

def main():
    myTest = Tester('registry.se')
    a1 = myTest.accounts[0]
    a2 = myTest.accounts[1]
    a2Send = {'sender':a2.privkey}
    test_cases = [('addToRegistry', ('foo', 123, 0), {}, 1),
                  ('addToRegistry', ('foo', 456, 0), a2Send, 1),
                  ('getVal', (a1.address_as_int, 'foo'), {}, 123),
                  ('getVal', (a2.address_as_int, 'foo'), a2Send, 456),
                  ('getOwnVal', ('foo',), {}, 123),
                  ('addToRegistry', ('foo', 789, 0), {}, 0),
                  ('getOwnVal', ('foo',), {}, 123),
                  ('addToRegistry', ('foo', 789, 1), {}, 1),
                  ('getOwnVal', ('foo',), {}, 789)]
    myTest.run_tests(test_cases)

if __name__ == '__main__':
    main()
