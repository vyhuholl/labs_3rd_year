import unittest

from buckets import Buckets

try:
    from sol_buckets_corrected import Buckets as BucketsCorrected
except (ModuleNotFoundError, ImportError):
    from buckets_corrected import Buckets as BucketsCorrected


class TestBuckets(unittest.TestCase):

    @unittest.skip("Buckets FAILED")
    def test_buckets(self):

        # FAILED
        try:
            b = Buckets()

        default = [[1], [2]]
        b = Buckets(5, default)

        # FAILED
        self.assertNotEqual(id(default), id(b.default))

        default[-1].append(3)
        # OK
        self.assertTrue(b.find(3,  [2, 3]))

        default.append([3])
        b.clear(3)
        # FAILED
        self.assertFalse(b.find(3, [3]))

        item = 125
        b.add(0, item)
        item += 1
        # FAILED
        self.assertTrue(b.find(0, item))

    def test_buckets_corrected(self):

        default = [[1], [2]]
        bc = BucketsCorrected(5, default)

        self.assertNotEqual(id(default), id(bc.default))

        default[-1].append(3)
        self.assertTrue(bc.find(1,  [2, 3]))

        default.append([3])
        bc.clear(3)
        self.assertFalse(bc.find(3, [3]))

    def test_together(self):
        default = [[1], [2]]
        b = Buckets(5, default)
        bc = BucketsCorrected(5, default)

        default[-1].append(3)
        default.append([3])

        b.clear(1)
        bc.clear(1)

        self.assertTrue(bc.default == bc.buckets[1] != default)
        self.assertTrue(b.default == b.buckets[1] == default)


if __name__ == "__main__":
    unittest.main()
