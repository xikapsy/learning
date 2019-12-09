#导包
import unittest
import time



#定义测试类

class TestCase1(unittest.TestCase):

    #测试环境搭建
    def setUp(self):
        pass

    # 测试用例
    def test_Case1(self):
        print("用例")

        try:
            assert  1+1 == 2
            print("Case1")
        except:
            print("1+1 != 2")

    #测试用例2
    #setup->case1->tearDown->setup->case2->tearDown
    def test_Case2(self):

        try:
            print("Case2")
        except:
            print("not test")

    #测试环境销毁
    def tearDown(self):
        pass


    # 测试用例3
    # 不放在setup及tearDown中间，依旧会在case2之后被执行

    def test_Case3(self):


        self.assertEqual(2,2)
        print("Case3")

#测试类2
#会在类1执行后执行
class TestCase2(unittest.TestCase):

    #测试环境搭建
    def setUp(self):
        pass

     # 测试环境销毁
    def tearDown(self):
        pass
    # 测试用例
    def test_Case1(self):
        print("Case4")

        try:
            assert  2+2 == 3
            print("2+2 != 3")
        except:
            print("1+1 != 2")

#测试用例执行
#
if __name__ == '__main__':
    #测试用例集合
    suite = unittest.TestSuite()
    # 添加测试用例

    # 将需要执行的case添加到Test Suite中，没有添加的不会被执行
    suite.addTest(TestCase1('test_Case1'))
    suite.addTest(TestCase2('test_Case1'))



    # TextTestRunner 有三个参数，它们都有默认参数：
    # 1. verbosity 分别三个级别： 0  1  2   它们输出的测试报告详细程度不同，2 最详细
    # 2. stream 关系着测试报告的位置，如果默认为None的话，测试报告会输出到控制台
    # 3. descriptions 测试报告的描述
    # 报告存放的文件夹
    dir_path = './'
    # 报告命名加上时间格式化
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    # 报告绝对路径
    report_path = dir_path + now + ' TextTestRunner.txt'

    with open(report_path, 'w', encoding='utf-8') as file:
        runner = unittest.TextTestRunner(stream=file, descriptions='TextTestRunner',verbosity=2)
    #运行
        runner.run(suite)

