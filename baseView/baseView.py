import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseView(object):
    def __init__(self, driver):
        """
        初始化BaseView类，接收一个WebDriver实例。

        :param driver: WebDriver实例
        """
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def find(self, *loc):
        """
        查找单个元素，使用WebDriverWait等待元素出现。

        :param loc: 元素定位器，例如 (By.ID, "element_id")
        :return: 找到的元素
        :raises Exception: 如果元素未找到，抛出异常
        """
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(loc)
            )
            self.logger.info(f"Element found: {loc}")
            return element
        except Exception as e:
            self.logger.error(f"Element not found: {loc}, error: {e}")
            raise

    def finds(self, *loc):
        """
        查找多个元素，使用WebDriverWait等待元素出现。

        :param loc: 元素定位器，例如 (By.ID, "element_id")
        :return: 找到的元素列表
        :raises Exception: 如果元素未找到，抛出异常
        """
        try:
            elements = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(loc)
            )
            self.logger.info(f"Elements found: {loc}")
            return elements
        except Exception as e:
            self.logger.error(f"Elements not found: {loc}, error: {e}")
            raise

    def get_window_size(self):
        """
        获取当前窗口的大小。

        :return: 窗口大小的字典，包含宽度和高度
        """
        size = self.driver.get_window_size()
        self.logger.info(f"Window size: {size}")
        return size

    def swipe(self, start_x, start_y, end_x, end_y, duration):
        """
        在移动设备上执行滑动操作。

        :param start_x: 起始点的X坐标
        :param start_y: 起始点的Y坐标
        :param end_x: 结束点的X坐标
        :param end_y: 结束点的Y坐标
        :param duration: 滑动持续时间（毫秒）
        :raises Exception: 如果滑动失败，抛出异常
        """
        try:
            self.driver.swipe(start_x, start_y, end_x, end_y, duration)
            self.logger.info(f"Swiped from ({start_x}, {start_y}) to ({end_x}, {end_y})")
        except Exception as e:
            self.logger.error(f"Swipe failed, error: {e}")
            raise
