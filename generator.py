
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
    digits_path = 'image/Number/'+number+'.png'
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
sec_per=['가', '나', '다', '라', '마', '거', '너', '더', '러', '머', 
                    '버', '서', '어', '저', '고', '노', '도', '로', '모', '보', 
                    '소', '오', '조', '구', '누', '두', '루', '무', '부', '수', '우', '주']
sec_per_dic={'가':cv2.imread('image/personal/Ga.png'), '나':cv2.imread('image/personal/na.png'), 
                    '다':cv2.imread('image/personal/da.png'),'라':cv2.imread('image/personal/la.png'), 
                    '마':cv2.imread('image/personal/ma.png'), '거':cv2.imread('image/personal/geo.png'),
                    '너':cv2.imread('image/personal/neo.png'), '더':cv2.imread('image/personal/deo.png'),
                    '러':cv2.imread('image/personal/leo.png'), '머':cv2.imread('image/personal/meo.png'), 
                    '버':cv2.imread('image/personal/beo.png'), '서':cv2.imread('image/personal/seo.png'),
                    '어':cv2.imread('image/personal/eo.png'), '저':cv2.imread('image/personal/jeo.png'),
                    '고':cv2.imread('image/personal/go.png'), '노':cv2.imread('image/personal/no.png'),
                    '도':cv2.imread('image/personal/do.png'), '로':cv2.imread('image/personal/lo.png'),
                    '모':cv2.imread('image/personal/mop.png'), '보':cv2.imread('image/personal/bo.png'),
                    '소':cv2.imread('image/personal/so.png'), '오':cv2.imread('image/personal/o.png'), 
                    '조':cv2.imread('image/personal/jo.png'), '구':cv2.imread('image/personal/gu.png'),
                    '누':cv2.imread('image/personal/nu.png'), '두':cv2.imread('image/personal/du.png'), 
                    '루':cv2.imread('image/personal/lu.png'), '무':cv2.imread('image/personal/mu.png'), 
                    '부':cv2.imread('image/personal/bu.png'), '수':cv2.imread('image/personal/su.png'), 
                    '우':cv2.imread('image/personal/u.png'), '주':cv2.imread('image/personal/ju.png')}

sec_tab=['아', '바', '사', '자']
sec_tab_dic={'아':cv2.imread('image/Tax_Bus/a.png'), 
                '바':cv2.imread('image/Tax_Bus/ba.png'), 
                '사':cv2.imread('image/Tax_Bus/sa.png'), 
                '자':cv2.imread('image/Tax_Bus/ja.png')}

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
plate_size_color = { 'RPB':[[(335,170), 'type5']],'RPA':[[(335,155), 'type2'],[(520,110),'type1']],
                                  'RCB':[[(335,170), 'type3']], 'RCA':[[(335,170), 'type3'], [(520,110), 'type3']],
                                  'LPB':[[(440,220), 'type5']], 'LPA':[[(440,220), 'type2']],
                                  'LCB':[[(440,220), 'type3']], 'LCA':[[(440,220), 'type3']],
                                  'RB':[[(335,170), 'type5']],'RA':[[(355,155), 'type2'],[(520,110), 'type1']]}

def write_img(name, image):
    print("Saved..\n %s%s.jpg" % folder, name)
    #존재하면 다른이름.
    cv2.imwrite(folder+name+'.jpg', image)

def selectPlateType(name, ptype, firstImg, secondImg, thirdImg):
    print(ptype)
    psc = plate_size_color[ptype]
    for i in psc:
        img = plate_type[i[1]]  #type Select
        img = cv2.resize(img, i[0]) #Resizing Image
        # cv2.imshow('test', img) 
        f = cv2.hconcat(firstImg)
        t = cv2.hconcat(thirdImg)
        res = cv2.hconcat([f,secondImg, t])
        res = cv2.resize(res, (319,83))
        #46.4에서 시작
        # cv2.imshow('test', res)
        # while cv2.waitKey(10)==ord('q'):
        #     continue
        # Write Image
        cv2.imwrite("example.png", res)
        # write_img(name, res)

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