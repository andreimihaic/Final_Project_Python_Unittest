import unittest
import HtmlTestRunner
from ProiectFinal.Test1_SinsayWebsiteOpen import SelectProducts
from ProiectFinal.Test2_AcceptCookiesChrome import AcceptCookiesChrome
from ProiectFinal.Test3_AcceptCookiesEdge import AcceptCookiesEdge
from ProiectFinal.Test4_AcceptCookiesFirefox import AcceptCookiesFirefox
from ProiectFinal.Test5_GoToStore import GoTOStoreTest
from ProiectFinal.Test6_SearchProducts import SearchProducts
from ProiectFinal.Test7_NotFoundProduct import NotFoundProduct
from ProiectFinal.Test8_FilterProducts import FilterProducts
from ProiectFinal.Test9_NavigateBack import NavigateBack
from ProiectFinal.Test10_ReturnHomepage import ReturnHomepage
from ProiectFinal.Test11_AddProductCart import AddProductCart
from ProiectFinal.Test12_EnterAccount import EnterAccount
from ProiectFinal.Test13_ShareButtons import SocialMediaButtons
from ProiectFinal.Test14_ChangeLanguage import ChangeLanguage


class TestSuite(unittest.TestCase):

    def test_suite(self):
        suite = unittest.TestSuite()
        suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(SelectProducts),
            unittest.defaultTestLoader.loadTestsFromTestCase(AcceptCookiesChrome),
            unittest.defaultTestLoader.loadTestsFromTestCase(AcceptCookiesEdge),
            unittest.defaultTestLoader.loadTestsFromTestCase(AcceptCookiesFirefox),
            unittest.defaultTestLoader.loadTestsFromTestCase(GoTOStoreTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(SearchProducts),
            unittest.defaultTestLoader.loadTestsFromTestCase(NotFoundProduct),
            unittest.defaultTestLoader.loadTestsFromTestCase(FilterProducts),
            unittest.defaultTestLoader.loadTestsFromTestCase(NavigateBack),
            unittest.defaultTestLoader.loadTestsFromTestCase(ReturnHomepage),
            unittest.defaultTestLoader.loadTestsFromTestCase(AddProductCart),
            unittest.defaultTestLoader.loadTestsFromTestCase(EnterAccount),
            unittest.defaultTestLoader.loadTestsFromTestCase(SocialMediaButtons),
            unittest.defaultTestLoader.loadTestsFromTestCase(ChangeLanguage),

        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_name='Test report',
            report_title='Sinsay test results'
        )
        result = runner.run(suite)
