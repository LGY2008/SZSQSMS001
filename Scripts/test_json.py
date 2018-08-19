import allure
import pytest


class Test():


    @allure.step(title="测试test_001方法：")
    def test_001(self):
        allure.attach("test001描述","执行打印输出语句")
        print("test001被执行")
        assert 1

    @pytest.allure.severity( pytest.allure.severity_level.CRITICAL)
    @allure.step(title="测试test_002方法：")
    def test_002(self):
        allure.attach("test002描述","执行打印输出语句")
        print("test001被执行")
        assert 0