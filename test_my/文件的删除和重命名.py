# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     文件的删除和重命名
   Description :
   Author :       fengwentao@changjing.ai
   date：          2022/6/19
-------------------------------------------------
   Change Activity:
                   2022/6/19:
-------------------------------------------------
"""
import os
dir = r"F:\学习资料\拉勾大数据开发高薪 【完结】"

def renameAndDelete(path):
    filenames = os.listdir(path)
    for filename in filenames:
        srcfilepath = os.path.join(path,filename)
        if os.path.isdir(srcfilepath):
            renameAndDelete(srcfilepath)
        else:
            if "【海量资源：666java.com】" in srcfilepath:
                destFilepath = srcfilepath.replace("【海量资源：666java.com】","")
                print("源文件:%s, 目的文件: %s"%(srcfilepath,destFilepath))
                os.rename(srcfilepath,destFilepath)
            if "【海量 资源：666java.com】" in srcfilepath:
                destFilepath = srcfilepath.replace("【海量 资源：666java.com】","")
                print("源文件:%s, 目的文件: %s"%(srcfilepath,destFilepath))
                os.rename(srcfilepath,destFilepath)
            if srcfilepath.endswith("downloading"):
                print("删除文件:%s"%srcfilepath)
                os.remove(srcfilepath)
renameAndDelete(dir)