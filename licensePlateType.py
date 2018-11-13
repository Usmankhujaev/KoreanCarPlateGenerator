

class LicensePlate:
    def __init__(self, img_type, img_num):
        self.img_w = None
        self.img_h = None
        self.img_num = img_num
        self.data_path = None



    def typePlate(self, w, h):
        self.img_w=w
        self.img_h = h

    
