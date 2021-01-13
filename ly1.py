import requests
import unittest
import json
class Sousuo_lcgl(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_06lclb(self):#输入不存在的物流码搜素
        url="http://123.57.140.190/manage/list_lcsy.php"
        headers={
            "Cookie":"PHPSESSID=10rckm92rat69jkbamfhpr14m5",
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data={"txm":"dsaldskadkadnadsada"}
        re=requests.post(url=url,headers=headers,data=data).text
        self.assertNotIn("dsaldskadkadnadsada",re,msg="断言失败")
        print(123)
if __name__ == '__main__':
    vv=unittest.TestSuite()
    vv.addTest(Sousuo_lcgl('test_06lclb'))
    gg=unittest.TextTestRunner(verbosity=2)
    gg.run(vv)
