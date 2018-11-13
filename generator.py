'''
Example
'32' '가' '0000'
The Korean Car plate is consist of three part.
---First Part is Consist of Two Byte
승용차(Passengers Car)  01 - 69
승합차(Vans) 70 - 79
화물차(Express Car) 80-97
특수차(Special Car) 98-99
------------------------------
---Second part is consist of Korean Character
*Personal or Non-Commercial (Total 32)
{가, 나, 다, 라, 마, 거, 너, 더, 러, 머, 버, 서, 어, 저, 고, 노, 도, 로, 모, 보, 소, 오, 조, 구, 누, 
두, 루, 무, 부, 수, 우, 주}

*Commercial (Taxi and Bus)
{아, 바, 사, 자}
*Commercial Express
{배}
*Commercial Renter Car
{하, 허, 호}
*Military
{국: Department of Defense,
합: Joint Chiefs of Staff,
육: Army,
해: Navy,
공: Air Force}
*Diplomatic
{외교: diplomat,
영사: consulate,
준외: Semi-diplomat,
준영: Quasi consulate,
국기: International Organization,
협정/대표: etc.}
-----------------------------------------
---Last part is Number of 4 decimal.
{0000,0001,....9999}
'''



from PIL import Image
import pytesseract
import argparse
import cv2
import os
import random
import csv
import sys

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dir", required=True,
	help="path to Output image to be folder")
ap.add_argument("-k", "--kind", type=str, default=None,
	help="type of specification to be done")
ap.add_argument("-n", "--num", type=int, default=1,
	help="Number of Car plate Data")
ap.add_argument("-t", "--type", type=str, default='RPA',
	help="Number of Car plate Data")

args = vars(ap.parse_args())
folder = args["dir"]
num = args['num']

#First Part
fir_pas = ['%02d'%i for i in range(1, 70)]
fir_van = ['%02d'%i for i in range(70, 80)]
fir_exp = ['%02d'%i for i in range(80,98)]
fir_spe = ['%02d'%i for i in range(98, 100)]
fir_list=[fir_pas,fir_van, fir_exp, fir_spe]

def return_image(number):
    digits_path = 'image/Number/'+number+'.jpg'
    return cv2.imread(digits_path)

def return_2image(number):
    i_str = '{:02}'.format(number)
    i_str=number
    return (return_image(i_str[0]), return_image(i_str[1]))

# fir_pas_dic = [return_2image(i) for i in range(1, 70)]    
# fir_van_dic = [return_2image(i) for i in range(70, 80)]
# fir_exp_dic = [return_2image(i) for i in range(80,98)]
# fir_spe_dic = [return_2image(i) for i in range(98, 100)]

diploma_dic = {'국기':cv2.imread('image/Diploma/gukgi.png'),
                        '협정/대표':cv2.imread('image/Diploma/hyeopjeong_datepyeo.png'),
                        '준외':cv2.imread('image/Diploma/junoe.png'),
                        '준영':cv2.imread('image/Diploma/junyeong.png'),
                        '외교':cv2.imread('image/Diploma/oegyeo.png'),
                        '영사':cv2.imread('image/Diploma/yeongsa.png')}
military_dic={'공':cv2.imread('image/Military/gong.png'),
                        '국':cv2.imread('image/Military/guk.png'),
                        '해':cv2.imread('image/Military/hae.png'),
                        '합':cv2.imread('image/Military/hap.png'),
                        '육':cv2.imread('image/Military/yuk.png')}

#Second Part
sec_per=['Ga', 'Na', 'Da', 'La', 'Ma', 'Geo', 'Neo', 'Deo', 'Leo', 'Meo', 
                    'Beo', 'Seo', 'Eo', 'Jeo', 'Go', 'No', 'Do', 'Lo', 'Mo', 'Bo', 
                    'So', 'O', 'Jo', 'Gu', 'Nu', 'Du', 'Lu', 'Mu', 'Bu', 'Su', 'U', 'Ju']
sec_per_dic={'Ga':cv2.imread('image/personal/Ga.jpg'), 'Na':cv2.imread('image/personal/na.jpg'), 
                    'Da':cv2.imread('image/personal/da.jpg'),'La':cv2.imread('image/personal/la.jpg'), 
                    'Ma':cv2.imread('image/personal/ma.jpg'), 'Geo':cv2.imread('image/personal/geo.jpg'),
                    'Neo':cv2.imread('image/personal/neo.jpg'), 'Deo':cv2.imread('image/personal/deo.jpg'),
                    'Leo':cv2.imread('image/personal/leo.jpg'), 'Meo':cv2.imread('image/personal/meo.jpg'), 
                    'Beo':cv2.imread('image/personal/beo.jpg'), 'Seo':cv2.imread('image/personal/seo.jpg'),
                    'Eo':cv2.imread('image/personal/eo.jpg'), 'Jeo':cv2.imread('image/personal/jeo.jpg'),
                    'Go':cv2.imread('image/personal/go.jpg'), 'No':cv2.imread('image/personal/no.jpg'),
                    'Do':cv2.imread('image/personal/do.jpg'), 'Lo':cv2.imread('image/personal/lo.jpg'),
                    'Mo':cv2.imread('image/personal/mo.jpg'), 'Bo':cv2.imread('image/personal/bo.jpg'),
                    'So':cv2.imread('image/personal/so.jpg'), 'O':cv2.imread('image/personal/o.jpg'), 
                    'Jo':cv2.imread('image/personal/jo.jpg'), 'Gu':cv2.imread('image/personal/gu.jpg'),
                    'Nu':cv2.imread('image/personal/nu.jpg'), 'Du':cv2.imread('image/personal/du.jpg'), 
                    'Lu':cv2.imread('image/personal/lu.jpg'), 'Mu':cv2.imread('image/personal/mu.jpg'), 
                    'Bu':cv2.imread('image/personal/bu.jpg'), 'Su':cv2.imread('image/personal/su.jpg'), 
                    'U':cv2.imread('image/personal/u.jpg'), 'Ju':cv2.imread('image/personal/ju.jpg')}

sec_tab=['A', 'Ba', 'Sa', 'Ja']
sec_tab_dic={'A':cv2.imread('image/Tax_Bus/a.png'), 
                'Ba':cv2.imread('image/Tax_Bus/ba.png'), 
                'Sa':cv2.imread('image/Tax_Bus/sa.png'), 
                'Ja':cv2.imread('image/Tax_Bus/ja.png')}

sec_exp=['배']
sec_exp_dic={'배':cv2.imread('image/Express/bae.png')}

sec_rent=['하','허','호']
sec_rent_dic={'하':cv2.imread('image/Rent/ha.png'),
                        '허':cv2.imread('image/Rent/heo.png'),
                        '호':cv2.imread('image/Rent/ho.png')}
#Third Part
thir_num = ['%04d'%i for i in range(0, 10000)]


#License Plate Type.
plate_type={'type1':cv2.imread('image/license_plates_template/type1.jpg'),
                    'type2':cv2.imread('image/license_plates_template/type2.jpg'),
                    'type3':cv2.imread('image/license_plates_template/type3.jpg'),
                    'type4':cv2.imread('image/license_plates_template/type4.jpg'),
                    'type5':cv2.imread('image/license_plates_template/type5.jpg')}
#Plate type consis of 335x115, 520x110, 440x220, 335x170, 335x155
"""*Personal or Non-Commercial (Total 32)
Type                                    Before 2006             After 2006
Regular : Personal             335x170(type5)     335x155(type2), 520x110(type1)
                Commercial          335x170(type3)      335x170(type3), 520x110(type3)
Large        : Personal         440x220(type5)      440x220(type2)
Vehicles  : Commercial       440x220(type3)     440x220(type3)
Rental Cars :                       335x170(type5)      335x155(type2), type1(520x110)
"""
#type be Combination of  R(Regular) + P(personal) or Commercial + Before or After , 
#                                      L(Large)+P(Personal) or C(Commercial) + Before or After,
#                                      R(Rental) +Before or After
#RPB is mean Regular Personal Before(2006)
plate_size_color = { 'RPB':[[(335,170), 'type5',(327,83)]],
                                  'RPA':[[(335,155), 'type2', (327,83)],[(520,110),'type1',(418,105)]],
                                  'RCB':[[(335,170), 'type3',(308, 92)]], 
                                  'RCA':[[(335,170), 'type3',(308, 92)], [(520,110), 'type3', (456,83)]],
                                  'LPB':[[(440,220), 'type5',(418,105)]], 
                                  'LPA':[[(440,220), 'type2',(418,105)]],
                                  'LCB':[[(440,220), 'type3', (401,116)]], 
                                  'LCA':[[(440,220), 'type3',(401,116)]],
                                  'RB':[[(335,170), 'type5',(308, 92)]],
                                  'RA':[[(355,155), 'type2',(364,83)],[(520,110), 'type1',(418,105)]]}

def write_img(name, image):
    print("Saved..\n %s\\%s\\%s.jpg" % (os.getcwd(), folder, name))
    saveFolder = os.getcwd()+'\\'+folder +'\\'
    #존재하면 다른이름.
    cnt =0
    while os.path.isfile(saveFolder+str(cnt)+name+'.jpg'):
        print('Files Exist')
        cnt+=1
    print("Image Writting..")
    cv2.imwrite(saveFolder+str(cnt)+name+'.jpg', image)
    # cv2.imwrite(name+'.jpg', image)

def image_merge(numImg, plImg):
    #Number = Img1, #Plate = Img2
    nh, nw, nc = numImg.shape
    ph, pw, pc = plImg.shape
    ## Image Addtion with Alpha
    x_offset = (pw-nw)/2
    y_offset = (ph-nh)/2
    
    # Load two images
    img1 = plImg
    img2 = numImg
    # I want to put logo on top-left corner, So I create a ROI
    rows,cols,channels = img2.shape
    roi = img1[0:rows, 0:cols ]
    # Now create a mask of logo and create its inverse mask also
    img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    # Now black-out the area of logo in ROI
    img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
    # Take only region of logo from logo image.
    img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
    # Put logo in ROI and modify the main image
    dst = cv2.add(img1_bg,img2_fg)
    img1[0:rows, 0:cols ] = dst
    
    return dst

def selectPlateType(name, ptype, firstImg, secondImg, thirdImg):
    print("ptype is :", ptype)
    psc = plate_size_color[ptype]
    for i in psc:
        img = plate_type[i[1]]  #type Select (BackGround)
        img = cv2.resize(img, i[0]) #Resizing Image
        # cv2.imshow('test', img) 
        f = cv2.hconcat(firstImg)   #Fore Ground
        t = cv2.hconcat(thirdImg)
        res = cv2.hconcat([f,secondImg, t])
        res = cv2.resize(res, i[2])
        print("Plate Size is ", img.shape)
        #Number = Img1, #Plate = Img2
        print("Number Size is :" , res.shape)
        # res = image_merge(res, img)
        # cv2.imshow('test', res)
        # while cv2.waitKey()==ord('q'):
        #     continue
        # Write Image
        write_img(name, res)

def combine(first, second, third, ptype):
    print('Combine')
    name = first+second+third
    print(name)
    if first ==None or second==None or third==None:
        print("None Value Exists...")
        exit()
    #Two List
    firstImg = [return_image(i) for i in first]
    #One Image
    secondImg = sec_per_dic[second]
    #Four List
    thirdImg = [return_image(i) for i in third]
    selectPlateType(name, ptype, firstImg, secondImg, thirdImg)
    print (first, second, third)
    
def main():
    if os.path.isdir(folder):
        if os.path.exists(os.getcwd()+folder):
            print('File',folder, 'is Exist')
            exit()
        print(folder, 'is saving...')
    else:
        print(folder,'has been maded')
        os.mkdir(folder)

    for i in range(0,num):
        first = None
        second=None
        third=None
        if args['kind'] =='personal':
            print('personal')
            first = random.choice(random.choice(fir_list))
            second = random.choice(sec_per)
            third = random.choice(thir_num)
            print (first, second, third)
        elif args['kind'] =='Taxi' or args['kind']=='bus':
            print('Taxi or Bus')
            first = random.choice(random.choice(fir_list))
            second = random.choice(sec_per)
            third = random.choice(thir_num)
            print (first, second, third)
        elif args['kind']=='Express':
            print('Express')
            first = random.choice(random.choice(fir_list))
            second = random.choice(sec_per)
            third = random.choice(thir_num)
            print (first, second, third)
        elif args['kind'] == 'Rent':
            print('Rent')
            first = random.choice(random.choice(fir_list))
            second = random.choice(sec_per)
            third = random.choice(thir_num)
            print (first, second, third)
        combine(first, second, third, args['type'])

if __name__ == '__main__':
    if len(sys.argv) < 7:
        print("Please Command\n Example \n -d 'directory' -k 'kind', -n 'numbers' ")
        exit()
    main()