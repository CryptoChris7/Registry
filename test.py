from serpent_tests import ContractTest, default_accounts

A0 = default_accounts[0]
A1 = default_accounts[1]
A2 = default_accounts[2]
A3 = default_accounts[3]


class RegistryTest(ContractTest):
    source = 'registry.se'

    def test_create(self):
        self.assertEqual(
            self.contract.create(sender=A0.private_key),
            1)

    def test_count(self):
        self.assertEqual(
            self.contract.count(),
            1)

    def test_getOwner(self):
        self.assertEqual(
            self.contract.getOwner(1),
            A0.address)

    def test_changeOwner(self):
        with self.assertTxFail():
            self.contract.changeOwner(
                1,
                A1.address,
                sender=A1.private_key)

        self.assertTrue(
            self.contract.changeOwner(
                1,
                A1.address,
                sender=A0.private_key))

    def test_add(self):
        self.assertTrue(
            self.contract.add(
                1,
                b'foo',
                A1.address,
                sender=A1.private_key))
        self.assertFalse(
            self.contract.add(
                1,
                b'foo',
                A2.address,
                sender=A1.private_key))
        with self.assertTxFail():
            self.contract.add(
                1,
                b'bar',
                A1.address,
                sender=A0.private_key)

    def test_update(self):
        self.assertTrue(
            self.contract.update(
                1,
                b'foo',
                A2.address,
                sender=A1.private_key))
        self.assertFalse(
            self.contract.update(
                1,
                b'bar',
                A3.address,
                sender=A1.private_key))
        with self.assertTxFail():
            self.contract.update(
                1,
                b'foo',
                A3.address,
                sender=A3.private_key)

    def test_lookup(self):
        self.assertEqual(
            self.contract.lookup(
                1,
                b'foo'),
            A2.address)

    def test_remove(self):
        self.assertTrue(
            self.contract.remove(
                1,
                b'foo',
                sender=A1.private_key))
        self.assertFalse(
            self.contract.remove(
                1,
                b'foo',
                sender=A1.private_key))
        with self.assertTxFail():
            self.contract.remove(
                1,
                b'foo',
                sender=A3.private_key)

if __name__ == '__main__':
    RegistryTest.run_tests()
