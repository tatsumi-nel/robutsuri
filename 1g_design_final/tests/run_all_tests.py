import unittest

def suite():
    test_suite = unittest.TestSuite()

    all_test_suite = unittest.defaultTestLoader.discover(".")

    for ts in all_test_suite:
        test_suite.addTest(ts)

    return test_suite


if __name__ == "__main__":
    my_suite = suite()
    unittest.TextTestRunner().run(my_suite)

