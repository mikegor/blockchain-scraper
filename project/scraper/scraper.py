from unittest import TestLoader, TestSuite, TextTestRunner
from project.scraper.scripts.google_search import GoogleSearch
# import testtools as testtools

if __name__ == "__main__":

    print('XD')
    test_loader = TestLoader()
    # Test Suite is used since there are multiple test cases
    test_suite = TestSuite((
        test_loader.loadTestsFromTestCase(GoogleSearch),
        ))
 
    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)