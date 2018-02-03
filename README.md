# crawl-q-zone-said-before

> python3 爬好友qq空间说说，并生产云图

## env
目前仅支持在mac/python3/firefox环境下运行

## dependence
- selenium
- wordcloud
- matplotlib
- jieba
- geckodriver

## preview

最终生成的云图
![Screenshot](./save/xxxxxxxx/cloud.png)

## usage

crawle qq-friend-zone-said-before via command-line

``` bash

Example:

  # clone
  git clone git@github.com:ws456999/crawl-q-zone-said-before.git

  # enter
  cd crawl-q-zone-said-before

  # run
  python3 crawler.py

  # input
  friend = input("请输入准备爬的好友号： ") # 朋友的空间要求允许你能访问
  user = input("请输入你的qq号： ")
  pw = getpass.getpass('请输入密码： ')


```

## License
MIT
