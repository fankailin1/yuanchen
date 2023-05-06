# -*-coding:utf-8 -*-
import pytest
import allure
import log
@allure.feature('功能名称')
class TestTag(object):


    @allure.story('子功能名称')
    @allure.title("测试1")
    @allure.step("第一步")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("x", ["1"])
    def test_01(self, x):
        """
        测试描述：测试sss1
        """
        a = x
        print(a)
        with allure.step("步骤1"):
            allure.attach("结果1", "修改后的内容", allure.attachment_type.TEXT)
            log.logger.info(f"我的结果是{a}")
            assert a == "1"
        with allure.step("步骤2"):
            allure.attach("结果2", "修改后的内容", allure.attachment_type.TEXT)

    @allure.story('子功能名称')
    @allure.title("测试2")
    @allure.step("第二步")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("x,y", [("1","2")])
    def test_02(self, x, y):
        """
        测试描述：测试sss2
        """
        a = x
        print(a)
        with allure.step("步骤1"):
            allure.attach("结果1", "修改后的内容", allure.attachment_type.TEXT)
            assert a == "1"
        with allure.step("步骤2"):
            allure.attach("结果2", "修改后的内容", allure.attachment_type.TEXT)