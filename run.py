# -*-coding:utf-8 -*-
import pytest
import allure
import os

pytest.main(["-s", "-v", "./test_01.py", "--allure-severities", "blocker", "--alluredir", "./result/", "--clean-alluredir"])
# os.system('python -m pytest -s ./test_ss.py --alluredir=./result/')
os.system(r"allure serve ./result/")  # 用于本地渲染对外展示结果
# os.system(r"allure generate ./result/ -o ./report/ --clean")  #生成报告
# os.system(r"allure open -h 127.0.0.1 -p 8883 ./report/")    #本地打开报告