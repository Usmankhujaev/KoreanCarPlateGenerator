import numpy as np
import cv2 
import random
import codecs
import argparse
# -*- coding: utf-8-sig-*-

class LicensePlate:
    def __init__(self):
        self.img_width = None
        self.img_height = None
        self.hg_path = {}
        self.digit_path = {}
        self.pType = None
        self.city_path=None
        self.pTypelist = ["RPA1", "RPA2", "RCA1", "RCA2", "LVPA1", "LVCA1"]
        self.digit_list=[]
        self.training_dir = "image/train/"

    def regularPersonalAfter1(self):
        # Width 335mm - 1081 px
        self.img_width = 1081
        # Height 155mm - 500px
        self.img_height = 500
        # 45mm - 145px
        self.num_width = 145
        # 83mm - 268px
        self.num_height = 268
        # 49mm - 158px
        self.hg_width = 158
        # 83mm - 268px
        self.hg_height = 268
        # (46.2mm, 4.0mm) - (149px, 13px)
        self.start_coord = [(149,13), 
                                        (149, 13+self.num_width), 
                                        (149, 13+self.num_width*2),
                                        (149, 13+self.num_width*2+self.hg_width),
                                        (149, 13+self.num_width*3+self.hg_width),
                                        (149, 13+self.num_width*4+self.hg_width),
                                        (149, 13+self.num_width*5+self.hg_width)]

        self.digit_path = {
            "0":cv2.imread("image/type1/0.jpg"),
            "1":cv2.imread("image/type1/1.jpg"),
            "2":cv2.imread("image/type1/2.jpg"),
            "3":cv2.imread("image/type1/3.jpg"),
            "4":cv2.imread("image/type1/4.jpg"),
            "5":cv2.imread("image/type1/5.jpg"),
            "6":cv2.imread("image/type1/6.jpg"),
            "7":cv2.imread("image/type1/7.jpg"),
            "8":cv2.imread("image/type1/8.jpg"),
            "9":cv2.imread("image/type1/9.jpg")
        }
        self.hg_path={
            "beo":cv2.imread("image/type1/beo.jpg"),
            "bu":cv2.imread("image/type1/bu.jpg"),
            "da":cv2.imread("image/type1/da.jpg"),
            "deo":cv2.imread("image/type1/deo.jpg"),
            "do":cv2.imread("image/type1/do.jpg"),
            "du":cv2.imread("image/type1/du.jpg"),
            "eo":cv2.imread("image/type1/eo.jpg"),
            "ga":cv2.imread("image/type1/ga.jpg"),
            "geo":cv2.imread("image/type1/geo.jpg"),
            "go":cv2.imread("image/type1/go.jpg"),
            "gu":cv2.imread("image/type1/gu.jpg"),
            "ha":cv2.imread("image/type1/ha.jpg"),
            "heo":cv2.imread("image/type1/heo.jpg"),
            "ho":cv2.imread("image/type1/ho.jpg"),
            "jeo":cv2.imread("image/type1/jeo.jpg"),
            "ju":cv2.imread("image/type1/ju.jpg"),
            "la":cv2.imread("image/type1/la.jpg"),
            "leo":cv2.imread("image/type1/leo.jpg"),
            "lo":cv2.imread("image/type1/lo.jpg"),
            "lu":cv2.imread("image/type1/lu.jpg"),
            "ma":cv2.imread("image/type1/ma.jpg"),
            "meo":cv2.imread("image/type1/meo.jpg"),
            "mo":cv2.imread("image/type1/mo.jpg"),
            "mu":cv2.imread("image/type1/mu.jpg"),
            "na":cv2.imread("image/type1/na.jpg"),
            "neo":cv2.imread("image/type1/neo.jpg"),
            "no":cv2.imread("image/type1/no.jpg"),
            "nu":cv2.imread("image/type1/nu.jpg"),
            "seo":cv2.imread("image/type1/seo.jpg"),
            "su":cv2.imread("image/type1/su.jpg"),
            "u":cv2.imread("image/type1/u.jpg")
        }

    def regularPersonalAfter2(self):
        # Width 520mm - 1679 px
        self.img_width = 1679
        # Height 110mm - 355px
        self.img_height = 355
        # 56mm - 181px
        self.num_width = 181
        # 83mm - 268px
        self.num_height = 268
        # 95mm - 307px
        self.hg_width = 307
        # 83mm - 268px
        self.hg_height = 268
        # (13.5mm, 44.0mm) - (44px, 142px)
        self.start_coord = [(44,142), 
                                (44, 142+self.num_width), 
                                (44, 142+self.num_width*2),
                                (44, 142+self.num_width*2+self.hg_width),
                                (44, 142+self.num_width*3+self.hg_width),
                                (44, 142+self.num_width*4+self.hg_width),
                                (44, 142+self.num_width*5+self.hg_width)]
        self.digit_path = {
            "0":cv2.imread("image/type2/0.jpg"),
            "1":cv2.imread("image/type2/1.jpg"),
            "2":cv2.imread("image/type2/2.jpg"),
            "3":cv2.imread("image/type2/3.jpg"),
            "4":cv2.imread("image/type2/4.jpg"),
            "5":cv2.imread("image/type2/5.jpg"),
            "6":cv2.imread("image/type2/6.jpg"),
            "7":cv2.imread("image/type2/7.jpg"),
            "8":cv2.imread("image/type2/8.jpg"),
            "9":cv2.imread("image/type2/9.jpg")
        }
        self.hg_path={
            "beo":cv2.imread("image/type2/beo.jpg"),
            "bo":cv2.imread("image/type2/bo.jpg"),
            "bu":cv2.imread("image/type2/bu.jpg"),
            "da":cv2.imread("image/type2/da.jpg"),
            "deo":cv2.imread("image/type2/deo.jpg"),
            "do":cv2.imread("image/type2/do.jpg"),
            "du":cv2.imread("image/type2/du.jpg"),
            "eo":cv2.imread("image/type2/eo.jpg"),
            "ga":cv2.imread("image/type2/ga.jpg"),
            "geo":cv2.imread("image/type2/geo.jpg"),
            "go":cv2.imread("image/type2/go.jpg"),
            "gu":cv2.imread("image/type2/gu.jpg"),
            "heo":cv2.imread("image/type2/heo.jpg"),
            "jeo":cv2.imread("image/type2/jeo.jpg"),
            "ju":cv2.imread("image/type2/ju.jpg"),
            "la":cv2.imread("image/type2/la.jpg"),
            "leo":cv2.imread("image/type2/leo.jpg"),
            "lo":cv2.imread("image/type2/lo.jpg"),
            "lu":cv2.imread("image/type2/lu.jpg"),
            "ma":cv2.imread("image/type2/ma.jpg"),
            "meo":cv2.imread("image/type2/meo.jpg"),
            "mo":cv2.imread("image/type2/mo.jpg"),
            "mu":cv2.imread("image/type2/mu.jpg"),
            "na":cv2.imread("image/type2/na.jpg"),
            "neo":cv2.imread("image/type2/neo.jpg"),
            "no":cv2.imread("image/type2/no.jpg"),
            "nu":cv2.imread("image/type2/nu.jpg"),
            "o":cv2.imread("image/type2/o.jpg"),
            "seo":cv2.imread("image/type2/seo.jpg"),
            "so":cv2.imread("image/type2/so.jpg"),
            "su":cv2.imread("image/type2/su.jpg"),
            "u":cv2.imread("image/type2/u.jpg")
        }

    def regularCommercialAfter1(self):
        # Width 335mm - 1081 px
        self.img_width = 1081
        # Height 170mm - 549px
        self.img_height = 549
        # 95mm - 307px
        self.top_hg_width = 307
        # 48mm - 155px
        self.top_hg_height = 155
        # 60mm - 192px
        self.btn_hg_width = 192
        # 92mm - 297px
        self.btn_hg_height = 297
        # 62mm - 200px
        self.num_width = 200
        # 92mm - 297px
        self.num_height = 297
        # 48mm - 155px
        self.top_num_height = 155
        # 38mm - 123px
        self.top_num_width = 123
        # (9.0mm, 65+17mm) - (29px, 210+55px)
        self.top_start_coord = [(29,265),
                                                (29,265+self.top_hg_width),
                                                (29,265+self.top_hg_width+self.num_width)]

        # (11+48+9mm , 9.5mm) - (36+155+29, 31)
        self.start_coord = [(29,265),
                                        (29,265+self.top_hg_width),
                                        (29,265+self.top_hg_width+self.top_num_width),
                                        (220, 31),
                                        (220, 31+self.btn_hg_width),
                                        (220, 31+self.btn_hg_width+self.num_width),
                                        (220, 31+self.btn_hg_width+self.num_width*2),
                                        (220, 31+self.btn_hg_width+self.num_width*3)]

        self.city_path = {
            "busan":cv2.imread("image/type3/busan.jpg"),
            "cheonbuk":cv2.imread("image/type3/cheonbuk.jpg"),
            "chungbuk":cv2.imread("image/type3/chungbuk.jpg"),
            "chungnam":cv2.imread("image/type3/chungnam.jpg"),
            "daegu":cv2.imread("image/type3/daegu.jpg"),
            "daejeon":cv2.imread("image/type3/daejon.jpg"),
            "gangwon":cv2.imread("image/type3/gangwon.jpg"),
            "gwangju":cv2.imread("image/type3/gwangju.jpg"),
            "gyeongi":cv2.imread("image/type3/gyeongi.jpg"),
            "incheon":cv2.imread("image/type3/incheon.jpg"),
            "jeju":cv2.imread("image/type3/jeju.jpg"),
            "kyeongbuk":cv2.imread("image/type3/kyeongbuk.jpg"),
            "kyeongnam":cv2.imread("image/type3/kyeongnam.jpg"),
            "seoul":cv2.imread("image/type3/seoul.jpg"),
            "ulsan":cv2.imread("image/type3/ulsan.jpg")
        }
        self.digit_path =  {
            "0":cv2.imread("image/type3/0.jpg"),
            "1":cv2.imread("image/type3/1.jpg"),
            "2":cv2.imread("image/type3/2.jpg"),
            "3":cv2.imread("image/type3/3.jpg"),
            "4":cv2.imread("image/type3/4.jpg"),
            "5":cv2.imread("image/type3/5.jpg"),
            "6":cv2.imread("image/type3/6.jpg"),
            "7":cv2.imread("image/type3/7.jpg"),
            "8":cv2.imread("image/type3/8.jpg"),
            "9":cv2.imread("image/type3/9.jpg")
        }
        self.hg_path={
            "a":cv2.imread("image/type3/a.jpg"),
            "ba":cv2.imread("image/type3/ba.jpg"),
            "sa":cv2.imread("image/type3/sa.jpg"),
            "ja":cv2.imread("image/type3/ja.jpg")
        }
    
    def regularCommercialAfter2(self):
        # Width 520mm - 1679px
        self.img_width = 1679
        # Height 110mm - 355px
        self.img_height = 355
        # 55mm = 178px
        self.top_hg_width = 178
        # 83mm - 268px
        self.top_hg_height = 268
        # 55mm - 178px
        self.top_num_width = self.num_width =178
        # 83mm - 268px
        self.top_num_height = self.num_height = 268
        # 71mm - 229px
        self.btn_hg_width = 229
        # 83mm - 268px
        self.btn_hg_height = 268
        # (13.5mm, 32.0mm) - (44px, 103px)
        self.start_coord = [(44,103),
                                        (44,103+self.top_hg_width),
                                        (44,103+self.top_hg_width+self.top_num_width),
                                        (44, 103+self.top_hg_width+self.top_num_width*2),
                                        (44, 103+self.top_hg_width+self.top_num_width*2+self.btn_hg_width),
                                        (44, 103+self.top_hg_width+self.top_num_width*2+self.btn_hg_width+self.num_width),
                                        (44, 103+self.top_hg_width+self.top_num_width*2+self.btn_hg_width+self.num_width*2),
                                        (44, 103+self.top_hg_width+self.top_num_width*2+self.btn_hg_width+self.num_width*3)]
        
        self.city_path = {
            "busan":cv2.imread("image/type4/busan.jpg"),
            "cheonbuk":cv2.imread("image/type4/cheonbuk.jpg"),
            "chungbuk":cv2.imread("image/type4/chungbuk.jpg"),
            "chungnam":cv2.imread("image/type4/chungnam.jpg"),
            "daegu":cv2.imread("image/type4/daegu.jpg"),
            "daejeon":cv2.imread("image/type4/daejon.jpg"),
            "gangwon":cv2.imread("image/type4/gangwon.jpg"),
            "gwangju":cv2.imread("image/type4/gwangju.jpg"),
            "gyeongi":cv2.imread("image/type4/gyeongi.jpg"),
            "incheon":cv2.imread("image/type4/incheon.jpg"),
            "jeju":cv2.imread("image/type4/jeju.jpg"),
            "jeonnam":cv2.imread("image/type4/jeonnam.jpg"),
            "kyeongbuk":cv2.imread("image/type4/kyeongbuk.jpg"),
            "kyeongnam":cv2.imread("image/type4/kyeongnam.jpg"),
            "seoul":cv2.imread("image/type4/seoul.jpg"),
            "ulsan":cv2.imread("image/type4/ulsan.jpg")
        }
        self.digit_path =  {
            "0":cv2.imread("image/type4/0.jpg"),
            "1":cv2.imread("image/type4/1.jpg"),
            "2":cv2.imread("image/type4/2.jpg"),
            "3":cv2.imread("image/type4/3.jpg"),
            "4":cv2.imread("image/type4/4.jpg"),
            "5":cv2.imread("image/type4/5.jpg"),
            "6":cv2.imread("image/type4/6.jpg"),
            "7":cv2.imread("image/type4/7.jpg"),
            "8":cv2.imread("image/type4/8.jpg"),
            "9":cv2.imread("image/type4/9.jpg")
        }
        self.hg_path={
            "a":cv2.imread("image/type4/a.jpg"),
            "ba":cv2.imread("image/type4/ba.jpg"),
            "sa":cv2.imread("image/type4/sa.jpg"),
            "ja":cv2.imread("image/type4/ja.jpg")
        }

    def largeVehiclesPersonalAfter1(self):
        # Width 440mm - 1420px
        self.img_width = 1420
        # Height 200mm - 646px
        self.img_height = 646
        # 59mm - 178px
        self.num_width = 190
        # 105mm - 339px
        self.num_height = 339
        # 64mm - 207px
        self.hg_width = 207
        # 105mm - 339px
        self.hg_height = 339
        # (60.0mm, 11.0mm) - (194px, 36px)
        self.start_coord = [(194,36), 
                                        (194, 36+self.num_width), 
                                        (194, 36+self.num_width*2),
                                        (194, 36+self.num_width*2+self.hg_width),
                                        (194, 36+self.num_width*3+self.hg_width),
                                        (194, 36+self.num_width*4+self.hg_width),
                                        (194, 36+self.num_width*5+self.hg_width)]
        self.digit_path =  {
            "0":cv2.imread("image/type5/0.jpg"),
            "1":cv2.imread("image/type5/1.jpg"),
            "2":cv2.imread("image/type5/2.jpg"),
            "3":cv2.imread("image/type5/3.jpg"),
            "4":cv2.imread("image/type5/4.jpg"),
            "5":cv2.imread("image/type5/5.jpg"),
            "6":cv2.imread("image/type5/6.jpg"),
            "7":cv2.imread("image/type5/7.jpg"),
            "8":cv2.imread("image/type5/8.jpg"),
            "9":cv2.imread("image/type5/9.jpg")
        }
        self.hg_path={
            "beo":cv2.imread("image/type5/beo.jpg"),
            "bo":cv2.imread("image/type5/bo.jpg"),
            "bu":cv2.imread("image/type5/bu.jpg"),
            "da":cv2.imread("image/type5/da.jpg"),
            "deo":cv2.imread("image/type5/deo.jpg"),
            "do":cv2.imread("image/type5/do.jpg"),
            "du":cv2.imread("image/type5/du.jpg"),
            "eo":cv2.imread("image/type5/eo.jpg"),
            "ga":cv2.imread("image/type5/ga.jpg"),
            "geo":cv2.imread("image/type5/geo.jpg"),
            "go":cv2.imread("image/type5/go.jpg"),
            "gu":cv2.imread("image/type5/gu.jpg"),
            "heo":cv2.imread("image/type5/heo.jpg"),
            "jeo":cv2.imread("image/type5/jeo.jpg"),
            "jo":cv2.imread("image/type5/jo.jpg"),
            "ju":cv2.imread("image/type5/ju.jpg"),
            "la":cv2.imread("image/type5/la.jpg"),
            "lo":cv2.imread("image/type5/lo.jpg"),
            "lu":cv2.imread("image/type5/lu.jpg"),
            "ma":cv2.imread("image/type5/ma.jpg"),
            "meo":cv2.imread("image/type5/meo.jpg"),
            "mo":cv2.imread("image/type5/mo.jpg"),
            "mu":cv2.imread("image/type5/mu.jpg"),
            "na":cv2.imread("image/type5/na.jpg"),
            "neo":cv2.imread("image/type5/neo.jpg"),
            "no":cv2.imread("image/type5/no.jpg"),
            "nu":cv2.imread("image/type5/nu.jpg"),
            "o":cv2.imread("image/type5/o.jpg"),
            "reo":cv2.imread("image/type5/reo.jpg"),
            "seo":cv2.imread("image/type5/seo.jpg"),
            "so":cv2.imread("image/type5/so.jpg"),
            "su":cv2.imread("image/type5/su.jpg"),
            "u":cv2.imread("image/type5/u.jpg")
        }

    def largeVehiclesCommercialAfter1(self):
        # Width 440mm - 1420 px
        self.img_width = 1420
        # Height 220mm - 710px
        self.img_height = 710
        # (75+32mm, 11.0mm) - (242+103px, 36px)
        self.top_start_coord = (345,36)
        # 126mm - 410px
        self.top_hg_width = 410
        # 61mm - 197px
        self.top_hg_height = 197
        # 50mm - 161px
        self.top_num_width = 161
        # 61mm - 197px
        self.top_num_height = 197

        # (11+61+12mm , 17mm) - (36+197+37, 52)
        self.start_coord = (265,52)
        # 89mm - 186px
        self.btn_hg_width = 186
        # 116mm - 374px
        self.btn_hg_height = 374
        # 78mm - 286px
        self.num_width = 286
        # 116mm - 374px
        self.num_height = 374
        # (9.0mm, 65+17mm) - (29px, 210+55px)
        self.top_start_coord = [(29,265),
                                                (29,265+self.top_hg_width),
                                                (29,265+self.top_hg_width+self.num_width)]

        # (11+48+9mm , 9.5mm) - (36+155+29, 31)
        self.start_coord = [(29,265),
                                        (29,265+self.top_hg_width),
                                        (29,265+self.top_hg_width+self.top_num_width),
                                        (220, 31),
                                        (220, 31+self.btn_hg_width),
                                        (220, 31+self.btn_hg_width+self.num_width),
                                        (220, 31+self.btn_hg_width+self.num_width*2),
                                        (220, 31+self.btn_hg_width+self.num_width*3)]

        self.city_path = {
            "busan":cv2.imread("image/type6/busan.jpg"),
            "cheonbuk":cv2.imread("image/type6/jeonbuk.jpg"),
            "chungbuk":cv2.imread("image/type6/chungbuk.jpg"),
            "chungnam":cv2.imread("image/type6/chungnam.jpg"),
            "daegu":cv2.imread("image/type6/daegu.jpg"),
            "daejeon":cv2.imread("image/type6/daejeon.jpg"),
            "gangwon":cv2.imread("image/type6/gangwon.jpg"),
            "gwangju":cv2.imread("image/type6/gwangju.jpg"),
            "gyeongi":cv2.imread("image/type6/gyeongi.jpg"),
            "incheon":cv2.imread("image/type6/incheon.jpg"),
            "jeju":cv2.imread("image/type6/jeju.jpg"),
            "kyeongbuk":cv2.imread("image/type6/kyeongbuk.jpg"),
            "kyeongnam":cv2.imread("image/type6/kyeongnam.jpg"),
            "seoul":cv2.imread("image/type6/seoul.jpg"),
            "ulsan":cv2.imread("image/type6/ulsan.jpg")
        }
        self.digit_path =  {
            "0":cv2.imread("image/type6/0.jpg"),
            "1":cv2.imread("image/type6/1.jpg"),
            "2":cv2.imread("image/type6/2.jpg"),
            "3":cv2.imread("image/type6/3.jpg"),
            "4":cv2.imread("image/type6/4.jpg"),
            "5":cv2.imread("image/type6/5.jpg"),
            "6":cv2.imread("image/type6/6.jpg"),
            "7":cv2.imread("image/type6/7.jpg"),
            "8":cv2.imread("image/type6/8.jpg"),
            "9":cv2.imread("image/type6/9.jpg")
        }
        self.hg_path={
            "a":cv2.imread("image/type6/a.jpg"),
            "ba":cv2.imread("image/type6/ba.jpg"),
            "sa":cv2.imread("image/type6/sa.jpg"),
            "ja":cv2.imread("image/type6/ja.jpg")
        }
        
    def create_image(self, height, width, channel, rgb_color=(0,0,0)):
        """Create new image(numpy array) filled with certain color in RGB"""
        # Create black blank image
        image = np.zeros((height, width, 3), dtype=np.uint8)
        # cv2.cvtColor(image, image, cv2.COLOR_BGR2Lab)
        # Since OpenCV uses BGR, convert the color first
        color = tuple(reversed(rgb_color))
        # Fill image with color
        image[:] = color
        return image

    def sortedDigitsOneLine(self):
        img = self.create_image(self.img_height, self.img_width, 3, (255,255,255))
        num_list=[]
        for i in range(7):
            k, v = random.choice(list(self.digit_path.items()))
            digits = cv2.resize(v, (self.num_width,self.num_height))
            self.digit_list.append(digits)
            num_list.append(k)
        hangul_k, hangul_v = random.choice(list(self.hg_path.items()))
        self.digit_list[2] = cv2.resize(hangul_v, (self.hg_width, self.hg_height))
        num_list[2] = hangul_k
        for i in range(7):
            x1, y1 = self.start_coord[i]
            x2, y2, _ = self.digit_list[i].shape
            img[x1:x2+x1, y1:y2+y1] = self.digit_list[i]
        return self.training_dir+''.join(num_list), img
    
    def sortedDigitsTwoLine(self):
        img = self.create_image(self.img_height, self.img_width, 3, (255,255,255))
        num_list=[]
        for i in range(8):
            k, v = random.choice(list(self.digit_path.items()))
            digits = cv2.resize(v, (self.num_width,self.num_height))
            self.digit_list.append(digits)
            num_list.append(k)
        hangul_k, hangul_v = random.choice(list(self.hg_path.items()))
        city_k, city_v = random.choice(list(self.city_path.items()))
        self.digit_list[0] = cv2.resize(city_v, (self.top_hg_width, self.top_hg_height))
        self.digit_list[1] = cv2.resize(self.digit_list[1], (self.top_num_width, self.top_num_height))
        self.digit_list[2] = cv2.resize(self.digit_list[2], (self.top_num_width, self.top_num_height))
        self.digit_list[3] = cv2.resize(hangul_v, (self.btn_hg_width, self.btn_hg_height))
        num_list[0] = city_k
        num_list[3] = hangul_k
        for i in range(8):
            x1, y1 = self.start_coord[i]
            x2, y2, _ = self.digit_list[i].shape
            img[x1:x2+x1, y1:y2+y1] = self.digit_list[i]
        return self.training_dir+''.join(num_list), img

    def sortedDigitsOneLineCity(self):
        img = self.create_image(self.img_height, self.img_width, 3, (255,255,255))
        num_list=[]
        for i in range(8):
            k, v = random.choice(list(self.digit_path.items()))
            digits = cv2.resize(v, (self.num_width,self.num_height))
            self.digit_list.append(digits)
            num_list.append(k)
        hangul_k, hangul_v = random.choice(list(self.hg_path.items()))
        city_k, city_v = random.choice(list(self.city_path.items()))
        self.digit_list[0] = cv2.resize(city_v, (self.top_hg_width, self.top_hg_height))
        self.digit_list[1] = cv2.resize(self.digit_list[1], (self.top_num_width, self.top_num_height))
        self.digit_list[2] = cv2.resize(self.digit_list[2], (self.top_num_width, self.top_num_height))
        self.digit_list[3] = cv2.resize(hangul_v, (self.btn_hg_width, self.btn_hg_height))
        num_list[0] = city_k
        num_list[3] = hangul_k
        for i in range(8):
            x1, y1 = self.start_coord[i]
            x2, y2, _ = self.digit_list[i].shape
            img[x1:x2+x1, y1:y2+y1] = self.digit_list[i]
        return self.training_dir+''.join(num_list), img

    def generatePlate(self, pType):
        #Make Rectangle
        if pType == "RPA1":
            self.regularPersonalAfter1()
            saveStr, img = self.sortedDigitsOneLine()
        elif pType == "RPA2":
            self.regularPersonalAfter2()
            saveStr, img = self.sortedDigitsOneLine()
        elif pType == "RCA1":
            self.regularCommercialAfter1()
        elif pType == "RCA2":
            self.regularCommercialAfter2()
            saveStr, img = self.sortedDigitsTwoLine()
        elif pType == "LVPA1":
            self.largeVehiclesPersonalAfter1()
            saveStr, img = self.sortedDigitsOneLine()
        elif pType == "LVCA1":
            self.largeVehiclesCommercialAfter1()
            saveStr, img = self.sortedDigitsTwoLine()
        else :
            print("Type is unvalid. Please Check Again!")
            exit()
        cv2.imwrite(saveStr+".jpg", img)

ap = argparse.ArgumentParser()
ap.add_argument("-t", "--train", required=True, type=str, default='Test',
	help="path to Output image to be folder")
ap.add_argument("-n", "--num", type=int, default=1,help="Number of Car plate Data")
ap.add_argument("-p", "--type", type=int, default=random.randrange(0,7),
	help="Number of Car plate Data Type")

args = vars(ap.parse_args())
if __name__ == '__main__':
    main = LicensePlate()
    if args["type"] >6 or args["type"] < 1:
        print("Type is unvalid!")
        exit()
    import sys
    print(sys.stdin.encoding)
    if args["train"] == "train":
        main.training_dir = "image/train/"
        main.training_dir = main.training_dir + 'type'+ str(args["type"])+'/'
        print(main.training_dir)
    elif args["train"] == "test":
        main.training_dir = "image/test/"
        main.training_dir = main.training_dir + 'type'+ str(args["type"])+'/'
        print(main.training_dir)
    else:
        print("Please Check -t should --train or --test")
        exit()
    for i in range(args["num"]):
        main.generatePlate(main.pTypelist[args["type"]-1])