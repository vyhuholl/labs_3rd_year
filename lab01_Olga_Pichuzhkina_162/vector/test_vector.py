import unittest

from vector import Vector


class TestVector(unittest.TestCase):

    def test_repr(self):
        v = Vector([1, 2, 3])

        self.assertEqual(str(v), "Vector([1, 2, 3])")
        self.assertEqual(repr(v), str(v))

        v = Vector([1.0, 2, 3.0])

        self.assertEqual(str(v), "Vector([1.0, 2, 3.0])")
        self.assertEqual(repr(v), str(v))

    def test_ndim(self):
        v = Vector([1, 2, 3])

        self.assertEqual(v.ndim(), 3)

        v.append(1)

        self.assertEqual(v.ndim(), 4)

        self.assertEqual(v.ndim(), len(v))

    def test_clear(self):
        v = Vector([1, 2, 3])
        v = v.clear()

        self.assertTrue(not v)
        with self.assertRaises(AttributeError):
            v.append(1)

        w = Vector([1, 2, 3])
        with self.assertRaises(TypeError):
            v + w

    def test_argmin(self):
        v = Vector([1, 2, 3])

        self.assertEqual(v.argmin(), 1)

        v.append(-2)
        self.assertEqual(v.argmin(), -2)
        self.assertEqual(v[v.argmin()], 3)

    def test_argmax(self):
        v = Vector([0, 1, 2])

        self.assertEqual(v.argmax(), 2)

        v.append(4)
        v.append(3)
        self.assertEqual(v.argmax(), 4)
        self.assertEqual(v[v.argmax()], 3)

    def test_add(self):
        v = Vector([1, 2, 3])
        w = Vector([3, 2, 1])

        self.assertEqual(v + w, Vector([4, 4, 4]))
        self.assertEqual((v + w)[0], (v + w)[1])
        self.assertEqual((v + w)[1], (v + w)[2])

    def test_sub(self):
        v = Vector([1, 2, 3])
        w = Vector([1, 2, 3])

        self.assertEqual(v - w, Vector([0, 0, 0]))
        self.assertEqual(sum(v - w), 0)
        self.assertEqual(len(v - w), 3)

    def test_mul(self):
        v = Vector([1, 2, 3])
        w = Vector([3, 2, 1])
        u = Vector([-1, -1, -1])

        self.assertEqual(v * w, Vector([3, 4, 3]))
        self.assertEqual(len(v * w), 3)
        self.assertEqual(v * w * u, Vector([-3, -4, -3]))

    def test_truediv(self):
        v = Vector([4, 3, 0])
        w = Vector([1, 2, 3])
        u = Vector([0, 0, 0])

        self.assertEqual(v / w, Vector([4, 1.5, 0]))
        self.assertEqual(len(v * w), 3)
        with self.assertRaises(ZeroDivisionError):
            v / u


if __name__ == "__main__":
    unittest.main()
