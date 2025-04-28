import logging
from common.caps import DriverManager
from common.elementlibrary import Login
from time import sleep



class SiginView(Login):
    def __init__(self, driver):
        super().__init__(driver)
    def login_action(self, username, password):
        self.driver.execute_script("document.body.style.zoom='1.0'")
        logging.info('点击登录')
        loginelement = self.wait_for_element_to_be_clickable(self.login)
        loginelement.click()
        logging.info('切换密码登录页面')
        self.find(*self.password).click()
        try:
            # 输入用户名
            self.find(*self.username_type).send_keys(username)
            logging.info('用户手机号是:%s' % username)

            # 输入密码
            self.find(*self.password_type).send_keys(password)
            logging.info('密码是:%s' % password)

            # 勾选协议
            self.find(*self.agree).click()

            # 点击登录
            lgbtn = self.wait_for_element_to_be_clickable(self.loginBtn)
            lgbtn.click()

            # 验证Toast提示
            toast_text = self.get_toast_text("登录成功")
            if toast_text:
                logging.info(f"Toast文本验证成功: {toast_text}")
            else:
                logging.error("Toast文本验证失败")


        except Exception as e:
            logging.error(f'登录失败，错误信息: {e}')
            print("登录失败")

if __name__ == '__main__':
    # 创建 DriverManager 实例
    driver_manager = DriverManager()
    # 使用 pre_caps 方法初始化 WebDriver
    driver = driver_manager.dev_caps()
    try:
        l = SiginView(driver)
        logging.info('登录功能验证')
        l.login_action('13297941815', '654321')
    finally:
        driver.quit()  # 注释掉此行