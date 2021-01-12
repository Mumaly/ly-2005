import unittest
from selenium import webdriver
import time
from config.denglu import DL
from selenium.webdriver.support.select import Select
import pyautogui
from HTMLTestRunnerNew import HTMLTestRunner


d=DL()
class Test_d2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        d.Login()
    @classmethod
    def tearDownClass(cls):
        d.dr.close()
        d.dr.quit()
    def test_01zcxz(self):#正常批量生成防伪码
        try:
           d.dr.find_element_by_xpath("/html/body/section/aside/div/ul/li[2]/ul/li[1]/a").click()
           d.dr.find_element_by_xpath("/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input").clear()
           d.dr.find_element_by_class_name("form-control").send_keys("222444888")
           d.dr.find_element_by_name("code_pre").send_keys("XKXK")
           Select(d.dr.find_element_by_xpath("//*[@id='code_type']")).select_by_index(3)
           Select(d.dr.find_element_by_id("txm_type")).select_by_visible_text("数字和字母")
           d.dr.find_element_by_xpath("/html/body/section/section/section/div/div/section/div/form/div[5]/div[2]/input").clear()
           d.dr.find_element_by_xpath("/html/body/section/section/section/div/div/section/div/form/div[5]/div[2]/input").send_keys(11)
           d.dr.find_element_by_name("code_count").send_keys(100)
           d.dr.find_element_by_xpath("/html/body/section/section/section/div/div/section/div/form/div[7]/div[1]/div/div[1]").click()
           d.dr.find_element_by_xpath("/html/body/section/section/section/div/div/section/div/form/div[7]/div[1]/div/div[2]/div/div[2]/div[19]").click()
           d.dr.find_element_by_css_selector(".btn.btn-danger").click()
           aa=d.dr.find_element_by_xpath("/html/body/div[3]/div").text
           self.assertEqual(aa,"恭喜，已成功生成100个防伪码！",msg="断言失败")
        except Exception as ff:
            print("异常显示:",ff)

    def test_02cfxz(self):#批量生成防伪码反例-生成批次输入重复
        try:
           d.dr.find_element_by_xpath("/html/body/section/aside/div/ul/li[2]/ul/li[1]/a").click()
           d.dr.find_element_by_xpath("/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input").clear()
           d.dr.find_element_by_class_name("form-control").send_keys("7777")
           d.dr.find_element_by_name("code_pre").send_keys("LALA")
           Select(d.dr.find_element_by_xpath("//*[@id='code_type']")).select_by_index(3)
           Select(d.dr.find_element_by_id("txm_type")).select_by_visible_text("数字和字母")
           d.dr.find_element_by_xpath("/html/body/section/section/section/div/div/section/div/form/div[5]/div[2]/input").clear()
           d.dr.find_element_by_xpath("/html/body/section/section/section/div/div/section/div/form/div[5]/div[2]/input").send_keys(11)
           d.dr.find_element_by_name("code_count").send_keys(10)
           d.dr.find_element_by_xpath("/html/body/section/section/section/div/div/section/div/form/div[7]/div[1]/div/div[1]").click()
           d.dr.find_element_by_xpath("/html/body/section/section/section/div/div/section/div/form/div[7]/div[1]/div/div[2]/div/div[2]/div[19]").click()
           d.dr.find_element_by_css_selector(".btn.btn-danger").click()
           aa=d.dr.find_element_by_xpath("/html/body/div[3]/div").text
           self.assertEqual(aa,"恭喜，已成功生成10个防伪码！",msg="断言失败")
        except Exception as ff:
            print("异常显示:",ff)

    def test_03zcdg(self):#正常单个生成防伪码
        try:
           d.dr.find_element_by_xpath("/html/body/section/aside/div/ul/li[2]/ul/li[2]/a").click()
           d.dr.find_element_by_xpath("/html/body/section/section/section/div/div/section/div/form/div[7]/div/button").click()
           aa=d.dr.find_element_by_xpath("/html/body/div[3]/div").text
           self.assertEqual(aa,"恭喜，成功生成一个防伪码！",msg="断言失败")
        except Exception as ff:
            print("异常显示:",ff)

    def test_04dgcf1(self):#单个生成防伪码反例-物流码重复
        try:
           d.dr.find_element_by_xpath("/html/body/section/aside/div/ul/li[2]/ul/li[2]/a").click()
           d.dr.find_element_by_xpath("/html/body/section/section/section/div/div/section/div/form/div[3]/div[1]/input").clear()
           d.dr.find_element_by_xpath("/html/body/section/section/section/div/div/section/div/form/div[3]/div[1]/input").send_keys("9627794312356")
           d.dr.find_element_by_xpath("/html/body/section/section/section/div/div/section/div/form/div[7]/div/button").click()
           aa=d.dr.find_element_by_class_name("layui-layer-content").text
           self.assertEqual(aa,"物流码有重复！!",msg="断言失败")
        except Exception as ff:
            print("异常显示:",ff)

    def test_05xgfwm(self):#按物流码，正常批量修改防伪码
        try:
            d.dr.find_element_by_link_text("批量修改防伪码").click()
            d.dr.find_element_by_name("txm").send_keys("9343279968652")
            d.dr.find_element_by_xpath("/html/body/section/section/section/div[1]/div/section/div/form/div[2]/div[1]").click()
            d.dr.find_element_by_xpath("/html/body/section/section/section/div[1]/div/section/div/form/div[2]/div[1]/div/div[2]/div/div[2]/div[7]").click()
            d.dr.find_element_by_css_selector(".btn.btn-danger").click()
            aa=d.dr.find_element_by_xpath("/html/body/div[3]/div").text
            self.assertEqual(aa,"批量修改成功",msg="断言失败")
        except Exception as ff:
            print("异常显示:",ff)

    def test_06sc(self):#按查询次数，正常删除防伪码
        try:
            d.dr.find_element_by_xpath("/html/body/section/aside/div/ul/li[2]/ul/li[4]/a").click()
            d.dr.find_element_by_name("hits").clear()
            d.dr.find_element_by_name("hits").send_keys(10)
            d.dr.find_element_by_xpath("/html/body/section/section/section/div[4]/div/section/div/form/div[2]/div/button").click()
            aa=d.dr.find_element_by_xpath("/html/body/div[3]/div").text
            self.assertEqual(aa,"查询数>=10的防伪码批量删除成功",msg="断言失败")
        except Exception as ff:
            print("异常显示:",ff)

    def test_07sc(self):#查询次数输入为空，删除防伪码
        try:
            d.dr.find_element_by_xpath("/html/body/section/aside/div/ul/li[2]/ul/li[4]/a").click()
            d.dr.find_element_by_name("hits").clear()
            d.dr.find_element_by_xpath("/html/body/section/section/section/div[4]/div/section/div/form/div[2]/div/button").click()
            aa=d.dr.find_element_by_xpath("/html/body/div[3]/div").text
            self.assertEqual(aa,"查询数>=的防伪码批量删除成功")
        except Exception as ff:
            print("异常显示:",ff)

    def test_08ztxg(self):#按物流码,修改防伪码状态
        try:
            d.dr.find_element_by_xpath("/html/body/section/aside/div/ul/li[2]/ul/li[5]/a").click()
            d.dr.find_element_by_xpath("//*[@id='txm']").send_keys("ZL8JCMMSMR5")
            Select(d.dr.find_element_by_id("qiyong")).select_by_index(1)
            d.dr.find_element_by_xpath("/html/body/section/section/section/div[1]/div/section/div/form/div[3]/div/button").click()
            aa=d.dr.find_element_by_xpath("/html/body/div[3]/div").text
            self.assertEqual(aa,"操作成功！",msg="断言失败")
        except Exception as ff:
            print("异常显示:",ff)

    def test_09ztxg(self):#防伪码批量导出
        try:
            d.dr.find_element_by_xpath("/html/body/section/aside/div/ul/li[2]/ul/li[7]/a").click()
            d.dr.find_element_by_xpath("/html/body/section/section/section/div[1]/div/section/div/form/div[5]/div/button").click()
            handles=d.dr.window_handles
            d.dr.switch_to.window(handles[-1])
            d.dr.find_element_by_xpath("/html/body/div[1]/div/a[1]").click()
            pyautogui.moveTo(502,412)
            pyautogui.click()
            time.sleep(4)
            pyautogui.moveTo(759, 492)
            pyautogui.click()
            time.sleep(4)
        except Exception as ff:
            print("异常显示:",ff)

if __name__ == '__main__':
    vv=unittest.TestSuite()
    vv.addTest(Test_d2('test_09ztxg'))
    gg=unittest.TextTestRunner(verbosity=2)
    gg.run(vv)
    # f = open(r'D:\pycharm\pycharm_project\溯源防伪码\test_report\test.html', 'wb')  # 以二进制模式打开一个文件
    # runner = HTMLTestRunner(f, title='防伪码测试报告', description='防伪码用例描述',tester='ly')
    # runner.run(vv)
