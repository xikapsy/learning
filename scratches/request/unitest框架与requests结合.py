#1、导包
import unittest
import requests

#2、新建测试类->unittest.TestCase
class TestLogin(unittest.TestCase):

    #3、setup  在test方法之前，会被执行
    def setUp(self):
        #获取session对象
        self.session = requests.session()
        #登录URL
        self.url_login = "http://test-general-field-wow-api.k8s.startdtapi.com/api/v1/recognition/login"


    #4、tearDown  test方法执行之后，会被执行
    def tearDown(self):
        #关闭session
        self.session.close()

    #5、登录成功
    def test_login_success(self):
        data_login = {
            "userName": "zhangquan",
            "password": "e10adc3949ba59abbe56e057f20f883e" }
        r = self.session.post(self.url_login, data=data_login)

        #断言
        try:
           self.assertEquals(400, r.status_code)
        except AssertionError as e:
            print(e + "0")

    #6、登录失败
    def test_not_exist(self):
        data_login = {
            "userName": "zhangquan",
            "password": "e10adc3949ba59abbe56e057f20f883" }
        r = self.session.post(self.url_login, data=data_login)
        # 断言
        try:
            self.assertEquals(500, r.status_code)
            print("1")
        except AssertionError as e:
            print(e + "0")


if __name__ == '_main_':
    unittest2.main()
