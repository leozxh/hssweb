import json
from selenium import webdriver
import logging.config
from os import path
from selenium.webdriver.chrome.service import Service

log_file_path = path.join(path.dirname(path.abspath(__file__)), '../config/log.conf')
logging.config.fileConfig(log_file_path)
logging = logging.getLogger()

class DriverManager:
    def __init__(self):
        # 读取配置文件
        config_path = path.join(path.dirname(path.abspath(__file__)), '../data/env.json')
        with open(config_path, 'r', encoding='utf-8') as f:
            self.config = json.load(f)

    def init_driver(self, env, log_message=None):
        """
        初始化Chrome浏览器驱动并打开指定URL
        :param env: 环境标识，如 'test', 'pre', 'dev'
        :param log_message: 可选的日志消息，用于记录操作信息
        :return: 返回初始化完成的WebDriver对象
        """
        url = self.config.get(env)
        if not url:
            raise ValueError(f"Invalid environment: {env}")

        driver_path = r"D:\chrome\chromedriver.exe"
        # 使用Service对象指定驱动路径
        service = Service(executable_path=driver_path)
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        if log_message:
            logging.info(log_message)
        driver.get(url)
        return driver

    def test_caps(self):
        """
        测试环境下的驱动初始化函数
        :return: 返回初始化完成的WebDriver对象
        """
        return self.init_driver("test", '访问测试环境官网，页面加载中')

    def pre_caps(self):
        """
        预生产环境下的驱动初始化函数
        :return: 返回初始化完成的WebDriver对象
        """
        return self.init_driver("pre", '访问预生产官网，页面加载中')

    def dev_caps(self):
        """
        正式环境下的驱动初始化函数
        :return: 返回初始化完成的WebDriver对象
        """
        return self.init_driver("dev", '访问狐少少正式环境官网，页面加载中')

# 示例用法
if __name__ == "__main__":
    driver_manager = DriverManager()
    driver = driver_manager.test_caps()

