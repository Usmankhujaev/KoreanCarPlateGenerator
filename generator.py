
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

args = vars(ap.parse_args())
folder = args["dir"]
num = args['num']

#First Part
fir_pas = ['%02d'%i for i in range(1, 70)]
fir_van = ['%02d'%i for i in range(70, 80)]
fir_exp = ['%02d'%i for i in range(80,98)]
fir_spe = ['%02d'%i for i in range(98, 100)]

def return_2image(number):
    # i_str = '{:02}'.format(number)
    i_str=number
    return (return_image(i_str[0]), return_image(i_str[1]))

fir_pas_dic = [return_2image(i) for i in range(1, 70)]    
fir_van_dic = [return_2image(i) for i in range(70, 80)]
fir_exp_dic = [return_2image(i) for i in range(80,98)]
fir_spe_dic = [return_2image(i) for i in range(98, 100)]

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
def return_image(number):
    digits_path = 'image/Number/'+str(number)+'.png'
    return cv2.imread(digits_path)

#License Plate Type.
plate_type={'type1':cv2.imread('image/license_plates_template/type_1.gif'),
                    'type2':cv2.imread('image/license_plates_template/type_2.gif'),
                    'type3':cv2.imread('image/license_plates_template/type_3.jpg'),
                    'type4':cv2.imread('image/license_plates_template/type_4.jpg'),
                    'type5':cv2.imread('image/license_plates_template/type_5.jpg')}

def combine(first, second, thrid):
    print('Combine')
    if first ==None or second==None or thrid==None:
        print("None Value Exists...")
        exit()
    
    


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
        if args['kind'] =='personal':
            print('personal')
            print(random.choice(fir_pas), random.choice(sec_per), random.choice(thir_num))
        elif args['kind'] =='Taxi' or args['kind']=='bus':
            print('Taxi or Bus')
            print(random.choice(fir_pas),random.choice(sec_tab),random.choice(thir_num))
        elif args['kind']=='Express':
            print('Express')
            print(random.choice(fir_pas),random.choice(sec_exp),random.choice(thir_num))
        elif args['kind'] == 'Rent':
            print('Rent')
            print(random.choice(fir_pas),random.choice(sec_rent),random.choice(thir_num))

if __name__ == '__main__':
    if len(sys.argv) < 7:
        print("Please Command\n Example \n -d 'directory' -k 'kind', -n 'numbers' ")
    exit()
    main()