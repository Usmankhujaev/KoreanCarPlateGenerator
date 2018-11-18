

class LicensePlate:
    def __init__(self, img_type, img_num):
        self.img_width = None
        self.img_height = None
        self.img_num = img_num
        self.data_path = None
        self.img_path = None
        self.pType = None
        self.digit_num = None
        self.location = ()
        self.city=None

    def regularPersonalAfter1(self):
        # Width 335mm - 1081 px
        self.img_width = 1081
        # Height 155mm - 500px
        self.img_height = 500
        # 45mm - 145px
        self.num_width = 145
        # 83mm - 268px
        self.num_height = 268
        # (46.2mm, 4.0mm) - (149px, 83px)
        self.start_coord = (149,83)
        # 49mm - 158px
        self.hg_width = 158
        # 83mm - 268px
        self.hg_height = 268
        self.img_path = "./image/Type2"

    def regularPersonalAfter2(self):
        # Width 520mm - 1679 px
        self.img_width = 1679
        # Height 110mm - 355px
        self.img_height = 355
        # 56mm - 181px
        self.num_width = 181
        # 83mm - 268px
        self.num_height = 268
        # (44.0mm, 13.5mm) - (142px, 44px)
        self.start_coord = (149,83)
        # 95mm - 307px
        self.hg_width = 307
        # 83mm - 268px
        self.hg_height = 268
        self.img_path = "./image/Type2"

    def regularCommercialAfter1(self):
        # Width 335mm - 1081 px
        self.img_width = 1081
        # Height 170mm - 549px
        self.img_height = 549
        # (65+17mm, 9.0mm) - (210+55px, 83px)
        self.top_start_coord = (265,83)
        # 95mm - 307px
        self.top_hg_width = 307
        # 48mm - 155px
        self.top_hg_height = 155
        # 38mm - 123px
        self.top_num_width = 123
        # 48mm - 155px
        self.top_num_height = 155

        # (11+48+9mm , 9.5mm) - (36+155+29, 31)
        self.start_coord = (265,83)
        # 60mm - 192px
        self.btn_hg_width = 192
        # 92mm - 297px
        self.btn_hg_height = 297
        # 62mm - 200px
        self.num_width = 200
        # 92mm - 297px
        self.num_height = 297

        self.img_path = "./image/Type2"
        self.city = '서울'
    
    def regularCommercialAfter2(self):
        # Width 520mm - 1679px
        self.img_width = 1679
        # Height 110mm - 355px
        self.img_height = 355
        # 55mm = 178px
        self.hg_city_width = 178
        # 83mm - 268px
        self.hg_city_height = 268
        # 55mm - 178px
        self.num_width = 178
        # 83mm - 268px
        self.num_height = 268
        # 71mm - 229px
        self.hg_width = 229
        # 83mm - 268px
        self.hg_height = 268
        # (32.0mm, 13.5mm) - (103px, 44px)
        self.start_coord = (149,83)
        self.img_path = "./image/Type2"

    def largeVehiclesPersonal(self):
        # Width 440mm - 1420px
        self.img_width = 1679
        # Height 110mm - 355px
        self.img_height = 355
        # 55mm = 178px
        self.hg_city_width = 178
        # 83mm - 268px
        self.hg_city_height = 268
        # 55mm - 178px
        self.num_width = 178
        # 83mm - 268px
        self.num_height = 268
        # 71mm - 229px
        self.hg_width = 229
        # 83mm - 268px
        self.hg_height = 268
        # (32.0mm, 13.5mm) - (103px, 44px)
        self.start_coord = (149,83)
        self.img_path = "./image/Type2"


    def typePlate(self, ptype=None):
        if ptype is None:
            print("type is None! Please select Type")
            exit()
        #Regular Personal After 2006 - 1
        if ptype is 'RPA1':
            self.pType = ptype
            self.img_w= 1081
            self.img_h = 500
        # Regular Personal After 2006 -2
        elif ptype is 'RPA2':
            self.pTyep = ptype
            self.img_w = 1679
            self.img_h = 355


    def printPlate(self):
        print("Type is ", self.pType)
        print("Width %d and Height %d" % (self.img_w, self.img_h))
        print("Img Path : ", self.img_path)
        print("Data Path :", self.data_path)



    #Regular 1, 2 is equal to width and height.
