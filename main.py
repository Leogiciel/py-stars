import unittest

import star_worker
from chain import Chain


class MyTest(unittest.TestCase):
    chain = Chain('11001001000', '10000110011')

    def test_need_to_change(self):
        self.assertFalse(self.chain.need_to_change(0))
        self.assertTrue(self.chain.need_to_change(1))

    def test_can_change_rank(self):
        self.assertFalse(self.chain.can_change_rank(1))
        self.assertTrue(self.chain.can_change_rank(10))

    def test_change(self):
        self.assertFalse(self.chain._state[10]) # pylint: disable=W0212
        self.chain._change(10) # pylint: disable=W0212
        self.assertTrue(self.chain._state[10]) # pylint: disable=W0212

    def test_worker(self):
        self.assertEqual(star_worker.compute('1101\n0100'), 2)
        self.assertEqual(star_worker.compute('101010\n010101'), 26)
        self.assertEqual(star_worker.compute('11001001000\n10000110011'), 877)


if __name__ == '__main__':
    unittest.main(exit=False)
