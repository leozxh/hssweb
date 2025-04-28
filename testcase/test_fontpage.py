from businessView.fontpageView import FontPageView
from businessView.siginView import SiginView
import unittest
import logging
from common.caps import DriverManager


class FontPageTest(unittest.TestCase):
    """首页功能测试"""

    @classmethod
    def setUpClass(cls):
        cls.driver_manager = DriverManager()
        cls.driver = cls.driver_manager.dev_caps()
        cls.sigin_view = SiginView(cls.driver)
        cls.fontpage_view = FontPageView(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        logging.info('Executing test case')

    def tearDown(self):
        logging.info('Test case execution completed')

    def test_1_login(self):
        """登录测试"""
        data = self.sigin_view.read_json_data('../data/account.json', 'account1')
        self.sigin_view.login_action(data['username'], data['password'])

    def test_2_video(self):
        """视频操作测试"""
        logging.info('Verifying video detail functionality')
        self.fontpage_view.video_action()


if __name__ == '__main__':
    unittest.main()
