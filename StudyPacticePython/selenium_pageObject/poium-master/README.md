### poium

基于 selenium/appium 的 Page Objects 设计模式测试库。

* 提供了一组基于JavaScript API，实现部分selenium 不支持的操作。
* 完全兼容原生selenium/appium API。
* 对Selenium/appium部分API做了封装，使操作更简单。

#### Installation
------------

download install:

```shell
$ python setup.py install
```

pip install:
```
$ pip install poium
```

#### 简单例子：


使用poium实现百度搜索。

```python

# baidu_page.py
from poium import Page, PageElement

class BaiduIndexPage(Page):
    search_input = PageElement(css='#kw', timeout=5, describe="搜索输入框")
    search_button = PageElement(css='#su', timeout=5, describe="搜索按钮")


# test_baidu.py
from selenium import webdriver
from baidu_page import BaiduIndexPage

driver = webdriver.Chrome()

page = BaiduIndexPage(driver)
page.get("https://www.baidu.com")

page.search_input.send_keys("poium")
page.search_button.click()

driver.quit()
```
使用poium将元素 __定位__ 与 __操作__ 分离，这将会非常有助于规模化自动化测试用例的编写与维护。

#### 使用文档：

请阅读 [wiki](https://github.com/defnngj/poium/wiki)

#### 项目历史：

参考项目：https://github.com/eeaston/page-objects

参考项目已经不再维护，我阅读了原项目代码，虽然只有100多行，但设计非常精妙。本项目在此基础上进行开发。

原项目名：https://pypi.org/project/selenium-page-objects/

有一天，我向群里的同学推荐selenium-page-objects，有同学问是否支持appium，appium也是从selenium继承而来，我想为什么不能支持appium呢？
于是，加入了appium支持，但是 selenium-page-objects 已经不能表达对appium的支持，而且他似乎有点长了。

本项目的核心是 Page Objects的设计模式, 于是取了 __PO__，同时支持selenium/appium，于是取了 __ium__，那么新的项目命名为：__poium__。
