from chain import Chain
import unittest
import star_worker


class MyTest(unittest.TestCase):
    def test(self):
        chain = Chain('11001001000\n10000110011')
        self.assertFalse(chain.need_to_change(0))
        self.assertTrue(chain.need_to_change(1))
        self.assertFalse(chain.can_change_rank(1))
        self.assertTrue(chain.can_change_rank(10))
        self.assertFalse(chain.state[10])
        chain.change(10)
        self.assertTrue(chain.state[10])
        self.assertEqual(star_worker.compute('1101\n0100'), 2)
        self.assertEqual(star_worker.compute('101010\n010101'), 26)
        self.assertEqual(star_worker.compute('11001001000\n10000110011'), 877)


if __name__ == '__main__':
    unittest.main()

