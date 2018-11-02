
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
#First Part
fir_pas = ['%02d'%i for i in range(1, 70)]
fir_van = ['%02d'%i for i in range(70, 80)]
fir_exp = ['%02d'%i for i in range(80,98)]
fir_spe = ['%02d'%i for i in range(98, 100)]

#Second Part
sec_per=['가', '나', '다', '라', '마', '거', '너', '더', '러', '머', 
                    '버', '서', '어', '저', '고', '노', '도', '로', '모', '보', 
                    '소', '오', '조', '구', '누', '두', '루', '무', '부', '수', '우', '주']
sec_tab=['아', '바', '사', '자']
sec_exp=['배']
sec_rent=['하','허','호']

#Third Part
thir_num = ['%04d'%i for i in range(0, 10000)]

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


if len(sys.argv) < 7:
    print("Please Command\n Example \n -d 'directory' -k 'kind', -n 'numbers' ")
    exit()

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
