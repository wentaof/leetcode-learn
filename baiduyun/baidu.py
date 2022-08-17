import os
import time

# 开关某应用
class baidu():

    def __init__(self):
        pass

    def open(self,path):
        os.startfile(path)

    def close(self,project_name):
        os.system('%s%s' % ("taskkill /F /IM ", project_name))

        pass

    def run(self):
        while True:
            path  = r"D:\app\baiduyun\BaiduNetdisk\BaiduNetdisk.exe"
            self.open(path)
            time.sleep(60)
            proname  = "baidunetdisk.exe"
            self.close(proname)

if __name__ == '__main__':
    b =baidu()
    b.run()