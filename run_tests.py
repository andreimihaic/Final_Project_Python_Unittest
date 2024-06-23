import unittest
import HtmlTestRunner
from ProiectFinal.Test1_SinsayWebsiteOpen import TestWebsiteOpen
from ProiectFinal.Test2_AcceptCookies import TestAcceptCookies
from ProiectFinal.Test3_GoToStore import TestGoTOStore
from ProiectFinal.Test4_HeaderIsDisplayed import TestHeaderIsDisplayed
from ProiectFinal.Test5_CheckSearchButtonIsDisplayed import TestCheckSearchButtonIsDisplayed
from ProiectFinal.Test6_SearchProducts import TestSearchProducts
from ProiectFinal.Test7_FilterProducts import TestFilterProducts
from ProiectFinal.Test8_NotFoundProduct import TestNotFoundProduct
from ProiectFinal.Test9_SortListAscending import TestSortListAscending
from ProiectFinal.Test10_TestNavigateBack import TestNavigateBack
from ProiectFinal.Test11_ReturnHomepage import TestReturnHomepage
from ProiectFinal.Test12_AuthenticationWithEmptyFields import TestAuthenticationWithEmptyFields
from ProiectFinal.Test13_AuthenticationWrongUsernameAndPassword import TestAuthenticationWrongUserAndPassword
from ProiectFinal.Test14_ShareButtons import TestSocialMediaIcons
from ProiectFinal.Test15_ChangeLanguage import TestChangeLanguage


class TestSuite(unittest.TestCase):

    def test_suite(self):
        suite = unittest.TestSuite()
        suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestWebsiteOpen),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestAcceptCookies),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestGoTOStore),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestHeaderIsDisplayed),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestCheckSearchButtonIsDisplayed),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestSearchProducts),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestFilterProducts),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestNotFoundProduct),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestSortListAscending),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestNavigateBack),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestReturnHomepage),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestAuthenticationWithEmptyFields),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestAuthenticationWrongUserAndPassword),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestSocialMediaIcons),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestChangeLanguage)
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_name='Test report',
            report_title='Sinsay test results'
        )
        result = runner.run(suite)
