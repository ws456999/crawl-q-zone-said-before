# coding=utf-8

import time
import sys
import getpass
import os
from selenium import webdriver
from lxml import etree
from show import create_word_cloud

sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)

friend = input("请输入准备爬的好友号： ") # 朋友的空间要求允许你能访问
user = input("请输入你的qq号： ")
pw = getpass.getpass('请输入密码： ')

path = './save/' + friend
new_path = os.path.join(path)
if not os.path.isdir(new_path):
  os.makedirs(new_path)

# 获取浏览器驱动
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://user.qzone.qq.com/" + friend + "/311")
driver.switch_to_frame('login_frame')

driver.find_element_by_id("switcher_plogin").click()
driver.find_element_by_id("u").send_keys(user)
driver.find_element_by_id("p").send_keys(pw)

time.sleep(3)

driver.find_element_by_id("login_button").click()
driver.switch_to.default_content()


next_num = 0
while True:
  for i in range(1, 6):
    height = 20000 * i
    strWord = "window.scrollBy(0," + str(height)+")"
    driver.execute_script(strWord)
    time.sleep(4)

  # 很多时候网页由多个<frame>或<iframe>组成，webdriver默认定位的是最外层的frame，
  # 所以这里需要选中一下说说所在的frame，否则找不到下面需要的网页元素
  driver.switch_to.frame("app_canvas_frame")
  selector = etree.HTML(driver.page_source)
  divs = selector.xpath('//*[@id="msgList"]/li/div[3]')

  with open('save/' + friend + "/words.txt",'a', encoding='utf-8') as f:
    for div in divs:
      qq_name = div.xpath('./div[2]/a/text()')
      qq_content = div.xpath('./div[2]/pre/text()')
      qq_time = div.xpath('./div[4]/div[1]/span/a/text()')
      qq_name = qq_name[0] if len(qq_name)>0 else ''
      qq_content = qq_content[0] if len(qq_content)>0 else ''
      qq_time = qq_time[0] if len(qq_time)>0 else ''
      print(qq_name,qq_time,qq_content)
      f.write(qq_content+"\n")

  # 当已经到了尾页，“下一页”这个按钮就没有id了，可以结束了
  if driver.page_source.find('pager_next_' + str(next_num)) == -1:
    create_word_cloud(friend)
    driver.quit()
    break

  driver.find_element_by_id('pager_next_' + str(next_num)).click()
  next_num += 1
  # 因为在下一个循环里首先还要把页面下拉，所以要跳到外层的frame上
  driver.switch_to.parent_frame()