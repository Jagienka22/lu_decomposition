from unittest import TestCase

from numpy.testing import assert_allclose

import faktoryzacja


class TestFacto_lu(TestCase):
    def test1_facto_lu(self):
        l, u = faktoryzacja.facto_lu([[2, 4], [1, 2]])
        rtol = 1e-5
        atol = 0
        # self.assertTrue((l == [[1., 0.], [0.5, 1.]]).all())
        assert_allclose(l, [[1., 0.], [0.5, 1.]], rtol, atol)
        # self.assertTrue((u == [[2., 4.], [0., 0.]]).all())
        assert_allclose(u, [[2., 4.], [0., 0.]], rtol, atol)

    def test2_facto_lu(self):
        l, u = faktoryzacja.facto_lu([[0, 1], [1, 0]])
