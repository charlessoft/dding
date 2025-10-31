# -*- coding: utf-8 -*-
import argparse
import sys

from dding.notify import notify_dding, notify_feishu


def main():
    if len(sys.argv) == 2:
        print(sys.argv[1])
        notify_dding(group='default', content=sys.argv[1], title='',msgtype='text')
    elif len(sys.argv) == 3:
        notify_dding(group=sys.argv[1], content=sys.argv[2], title='',msgtype='text')
    else:
        parser = argparse.ArgumentParser()
        parser.add_argument('--platform', default='dding', choices=['dding', 'feishu'], 
                          help='选择通知平台: dding(钉钉) 或 feishu(飞书)')
        parser.add_argument('--group', default='default')
        parser.add_argument('--content', default='')
        parser.add_argument('--title', default='')
        parser.add_argument('--msgtype', default='text')
        args = parser.parse_args()

        params = vars(args)
        # print(params)
        platform = params.pop('platform')  # 取出platform参数

        # 根据平台选择调用不同的函数
        if platform == 'feishu':
            notify_feishu(**params)
        else:
            notify_dding(**params)


def usage():
    print("usage: dding group=[custom name] content=hello")
    print("usage: dding --group default --content hello --title hello --msgtype markdown")
    print("usage: dding --content hello --msgtype text")
    print("example: dding helloworld")


def test1():
    content="### 杭州天气 \n> 1111"
    # content="### 杭州天气 \n 1111"

def test_feishu():
    notify_feishu(group='default', title='hello',content=sys.argv[1], msgtype='text')

if __name__ == '__main__':
    main()
    # test1()

