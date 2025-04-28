from baseView.baseView import BaseView
import time
import csv
import os
import logging
from faker import Faker
import random
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import json


class Common(BaseView):
    """常用功能封装"""

    def get_current_time(self):
        """获取当前时间"""
        return time.strftime("%Y-%m-%d %H_%M_%S")

    def capture_screenshot(self, module):
        """获取屏幕截图"""
        timestamp = self.get_current_time()
        screenshot_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'screenshots', f'{module}_{timestamp}.png')
        logging.info(f'Capturing screenshot for {module}')
        self.driver.get_screenshot_as_file(screenshot_path)


    def read_json_data(self, json_file, account_key):
        """读取JSON文件指定账号的数据"""
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data.get(account_key, {})

    def generate_random_email(self):
        """生成随机邮箱"""
        fake = Faker(locale='zh_CN')
        return f"{random.randint(1, 99999)}@testcg.com"

    def wait_for_element_to_be_clickable(self, locator):
        """
        等待元素可点击。

        :param locator: 元素定位器，例如 (By.ID, "element_id")
        :return: 可点击的元素对象
        :raises TimeoutException: 如果在指定时间内元素不可点击
        """
        timeout = 10  # 默认等待时间
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return element
        except TimeoutException:
            logging.error(f"元素 {locator} 在 {timeout} 秒内不可点击")
            raise TimeoutException(f"元素 {locator} 在 {timeout} 秒内不可点击")
        except Exception as e:
            logging.error(f"等待元素可点击时发生错误: {str(e)}")
            raise Exception(f"等待元素可点击时发生错误: {str(e)}")

    def get_toast_text(self, toast_message, timeout=10):
        try:
            toast_locator = (By.XPATH, f"//*[contains(text(), '{toast_message}')]")
            toast_element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(toast_locator)
            )
            return toast_element.text
        except Exception as e:
            logging.error(f"未能找到Toast提示: {e}")
            return None

    def generate_normal_comment(self):
        """随机生成正常评论"""
        fake = Faker(locale='zh_CN')

        # 定义一些针对短视频和图文内容的评论模板
        comment_templates = [
            "这个视频的{}真好。",
            "非常喜欢这个视频的{}。",
            "{}非常出色。",
            "这个视频的{}让人印象深刻。",
            "看了这个视频，觉得{}很棒。",
            "这个视频的{}搭配得很不错。",
            "这个视频的{}让我感到{}。",
            "这个视频的{}真是{}。",
            "这个视频的{}很{}。",
            "这个视频的{}让人{}。"
        ]

        # 针对短视频和图文内容的关键词
        keywords = [
            "清晰度", "剪辑", "镜头运用", "故事情节", "创意点", "表达方式",
            "色彩搭配", "构图", "视觉冲击力", "背景音乐", "音效", "配乐",
            "观看体验", "情感共鸣", "启发性"
        ]

        # 针对关键词的描述语句
        keyword_descriptions = {
            "清晰度": ["很高", "非常清晰", "细节丰富"],
            "剪辑": ["流畅", "紧凑", "富有节奏感"],
            "镜头运用": ["巧妙", "多样", "富有表现力"],
            "故事情节": ["引人入胜", "有趣", "感人"],
            "创意点": ["独特", "新颖", "有创意"],
            "表达方式": ["生动", "形象", "贴切"],
            "色彩搭配": ["和谐", "鲜艳", "舒适"],
            "构图": ["精美", "合理", "有层次感"],
            "视觉冲击力": ["强烈", "震撼", "吸引人"],
            "背景音乐": ["动听", "恰到好处", "增强氛围"],
            "音效": ["逼真", "丰富", "增强效果"],
            "配乐": ["优美", "贴合画面", "提升情感"],
            "观看体验": ["愉快", "顺畅", "沉浸"],
            "情感共鸣": ["强烈", "深刻", "真实"],
            "启发性": ["高", "值得思考", "引人深思"]
        }

        # 随机选择一个模板
        template = random.choice(comment_templates)

        # 随机选择关键词
        keyword = random.choice(keywords)

        # 根据关键词选择描述语句
        if keyword in keyword_descriptions:
            description = random.choice(keyword_descriptions[keyword])
        else:
            description = fake.word()  # 如果没有特定描述，使用随机单词

        # 格式化模板生成最终评论
        if '{}' in template:
            comment = template.format(keyword, description)
        else:
            comment = template.format(keyword)

        return comment

    pass
