import unittest

import sys
sys.path.append('../lib')

from cross_section import CrossSection

class CrossSectionTest(unittest.TestCase):

    def test_sets(self):
        xs = CrossSection()
        xs.set_d(0, 1.0)
        xs.set_siga(0, 2.0)
        xs.set_nusigf(0, 3.0)
        xs.set_xi(0, 1.0)
        xs.set_d(1, 11.0)
        xs.set_siga(1, 12.0)
        xs.set_nusigf(1, 13.0)
        xs.set_xi(1, 0.0)
        xs.set_smat([[1.0, 2.0],[3.0, 4.0]])
        #   sm(kg, kkg)
        # 
        #             kkg
        #           0     1
        #   kg 0   1.0   2.0
        #      1   3.0   4.0

        self.assertEqual(xs.dif(0), 1.0)
        self.assertEqual(xs.siga(0), 2.0)
        self.assertEqual(xs.nusigf(0), 3.0)
        self.assertEqual(xs.xi(0), 1.0)
        self.assertEqual(xs.dif(1), 11.0)
        self.assertEqual(xs.siga(1), 12.0)
        self.assertEqual(xs.nusigf(1), 13.0)
        self.assertEqual(xs.xi(1), 0.0)
        self.assertEqual(xs.sigs(0,0), 1.0)
        self.assertEqual(xs.sigs(0,1), 2.0)
        self.assertEqual(xs.sigs(1,0), 3.0)
        self.assertEqual(xs.sigs(1,1), 4.0)        

    def test_sets3(self):
        xs1 = CrossSection()
        xs1.set([[1.0, 2.0, 3.0, 1.0],[11.0, 12.0, 13.0, 0.0]])
        xs1.set_smat( [[1.0, 2.0], [3.0, 4.0]])
        xs1_ref = CrossSection()
        xs1_ref.set(xs1)
        self.assertEqual(xs1, xs1_ref)
    
    def test_operation_add(self):
        xs1 = CrossSection()
        xs1.set([[1.0, 2.0, 3.0, 1.0],[11.0, 12.0, 13.0, 0.0]])
        xs1.set_smat( [[1.0, 2.0], [3.0, 4.0]])

        xs2 = CrossSection()
        xs2.set([[1.0, 2.0, 3.0, 1.0],[11.0, 12.0, 13.0, 0.0]])
        xs2.set_smat( [[1.0, 2.0], [3.0, 4.0]])

        xs3 = xs1 + xs2

        xs3_ref = CrossSection()
        xs3_ref.set([[2.0, 4.0, 6.0, 2.0],[22.0, 24.0, 26.0, 0.0]])
        xs3_ref.set_smat( [[2.0, 4.0], [6.0, 8.0]])

        self.assertEqual(xs3, xs3_ref)

    def test_operation_sub(self):
        xs1 = CrossSection()
        xs1.set([[1.0, 2.0, 3.0, 1.0],[11.0, 12.0, 13.0, 0.0]])
        xs1.set_smat( [[1.0, 2.0], [3.0, 4.0]])

        xs2 = CrossSection()
        xs2.set([[2.0, 4.0, 6.0, 2.0],[22.0, 24.0, 26.0, 0.0]])
        xs2.set_smat( [[2.0, 4.0], [6.0, 8.0]])
    
        xs3 = xs2 - xs1

        xs3_ref = CrossSection()
        xs3_ref.set([[1.0, 2.0, 3.0, 1.0],[11.0, 12.0, 13.0, 0.0]])
        xs3_ref.set_smat( [[1.0, 2.0], [3.0, 4.0]])

        self.assertEqual(xs3, xs3_ref)

    def test_operation_mul(self):
        xs1 = CrossSection()
        xs1.set([[1.0, 2.0, 3.0, 1.0],[11.0, 12.0, 13.0, 0.0]])
        xs1.set_smat( [[1.0, 2.0], [3.0, 4.0]])

        xs2 = xs1 * 2.0

        xs2_ref = CrossSection()
        xs2_ref.set([[2.0, 4.0, 6.0, 2.0],[22.0, 24.0, 26.0, 0.0]])
        xs2_ref.set_smat( [[2.0, 4.0], [6.0, 8.0]])

        self.assertEqual(xs2, xs2_ref)

        xs3 = 2.0 * xs1
        xs3_ref = xs2_ref
        self.assertEqual(xs3, xs3_ref)

        xs4 = 2.0 * xs1 * 3.0
        xs4_ref = CrossSection()
        xs4_ref.set([[6.0, 12.0, 18.0, 6.0],[66.0, 72.0, 78.0, 0.0]])
        xs4_ref.set_smat( [[6.0, 12.0], [18.0, 24.0]])
        xs4.debug()
        xs4_ref.debug()

        self.assertEqual(xs4, xs4_ref)



if __name__ == '__main__':
    unittest.main()
