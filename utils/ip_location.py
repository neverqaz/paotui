# -*- coding: utf-8 -*-
import requests
import json


class IP_Location(object):
    def __init__(self):
        self.url = "http://api.map.baidu.com/location/ip"
        self.ak = "unrcs1AVyGvK5Y085KID6mBmkrK62Dmw"

    def getlocation(self):
        requset_url = "{url}?ak={ak}&coor=bd09ll".format(url=self.url, ak=self.ak)
        result = requests.get(requset_url).text.encode("utf-8").decode('unicode_escape')

        return result


if __name__ == "__main__":
    ip = IP_Location().getlocation()
    print(ip)
    # http://api.map.baidu.com/marker?location=111.66035052,40.82831887&title = 我的位置&content=百度奎科大厦&output=html&src=webapp.baidu.openAPIdemo
    # http://api.map.baidu.com/geocoder/v2/?address = 呼和浩特市赛罕区内蒙古农业大学&output =json&ak=unrcs1AVyGvK5Y085KID6mBmkrK62Dmw&callback=showLocation
