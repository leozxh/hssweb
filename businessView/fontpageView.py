# 首页功能:页面卡片跳转对应详情页
import logging
import random
from common.caps import DriverManager
from common.elementlibrary import fontpage
from time import sleep
from businessView.siginView import SiginView


class FontPageView(fontpage):

    def video_action(self):
        #点击视频
        self.find(*self.video).click()
        #点赞视频
        self.find(*self.like).click()
        # 验证Toast提示
        toast_text = self.get_toast_text("点赞成功")
        if toast_text:
            logging.info(f"Toast文本验证成功: {toast_text}")
        else:
            logging.error("Toast文本验证失败")
        # 取消点赞视频
        self.find(*self.like).click()
        #点击评论
        self.find(*self.comment).click()
        #输入评论
        random_comment = self.generate_normal_comment()
        self.find(*self.comment_type).send_keys(random_comment)
        #点击评论提交
        self.find(*self.comment_submit).click()
        #关闭评论框
        self.find(*self.commentcls).click()




if __name__ == '__main__':
    # 创建 DriverManager 实例
    driver_manager = DriverManager()
    # 使用 dev_caps 方法初始化 WebDriver
    driver = driver_manager.dev_caps()
    try:
        # 创建siginView实例并调用登录方法
        sigin_view = SiginView(driver)
        logging.info('登录功能验证')
        sigin_view.login_action('13297941815', '654321')

        # 创建fontpageView实例并调用video_action方法
        fontpage_view = FontPageView(driver)
        logging.info('视频功能验证')
        fontpage_view.video_action()
    finally:
        sleep(3)
        #driver.quit()