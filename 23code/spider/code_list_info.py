# -*- encoding:utf-8 -*-


#抓去列表信息
class Code_list(object):
    """docstring for Code_list"""
    def __init__(self, img_convery=None,app_title=None,upload_time=None,app_desc=None,category_txt_href=None,app_category=None):
        super(Code_list, self).__init__()
        self.img_convery = img_convery
        self.app_title = app_title
        self.upload_time = upload_time
        self.app_desc = app_desc
        self.category_txt_href = category_txt_href
        self.app_category = app_category

    def __str__(self):
        return self.img_convery+" @ " + self.app_title +" @ " + self.upload_time +" @ " + self.app_desc +" @ "+self.category_txt_href + " @ " + self.app_category
