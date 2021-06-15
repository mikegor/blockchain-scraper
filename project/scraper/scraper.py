from unittest import TestLoader, TestSuite, TextTestRunner
from project.scraper.scripts.google_search import GoogleSearch

if __name__ == "__main__":

    test_loader = TestLoader()
    test_suite = TestSuite((
        test_loader.loadTestsFromTestCase(GoogleSearch),
        ))
 
    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)