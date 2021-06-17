import sys
from time import sleep
from loguru import logger, _defaults
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions  as EC

class TestLol():
    def setup(self):
        logger.add(sink=sys.stdout,format=_defaults.LOGURU_FORMAT)
        logger.info("开始测试")
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def teardown(self):
        logger.info("测试结束")
        self.driver.close()
        self.driver.quit()

    def test_click(self):
        logger.info("打开网址百度")
        self.driver.get("https://www.baidu.com")
        def wait(x):
            return len(self.driver.find_elements(By.XPATH,"//*[@id='kw']")) >= 1
        WebDriverWait(self.driver,10).until(wait)
        # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID,"kw")))
        logger.info("输入英雄联盟")
        self.driver.find_element_by_id("kw").send_keys("英雄联盟")
        logger.info("点击英雄联盟")
        self.driver.find_element_by_id("su").click()
        self.driver.find_element_by_link_text("英雄联盟全新官方网站-腾讯游戏").click()
