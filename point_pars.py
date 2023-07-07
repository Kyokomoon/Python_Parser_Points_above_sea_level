from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from random import random, randrange, randint
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"

#для нахождения точек впишите ваши координаты LAT LONG
x1 = 54.848216
y1 = 82.719252
x2 = 55.146316
y2 = 83.276841

massx = []
massy = []

file_check = ' '

while(file_check != 'Y' or file_check != "yes" or file_check != "Yes" or file_check != "YES" or file_check != 'y' or file_check != 'N'or file_check != 'n' or file_check !=  "No" or file_check != "NO" or file_check != "no"):
    try:
        file_check = str(input("Файл с точками был подготовлен?(Y/N) >> "))
    except:
        print("Некорректный ответ")

if(file_check == "Y" or file_check == "y" or file_check == "YES" or file_check == "Yes" or file_check == "yes"):
    pointsx = open("pointx.txt")
    for i in pointsx:
        massx.append(float(i[:-1])) 
    pointsx.close()
    pointsy = open("pointy.txt")
    for i in pointsy:
        massy.append(float(i[:-1]))
    pointsy.close()
else:
    pointsx = open("pointx.txt", "w")
    for i in range(1000):
        massx.append(str((((x2 - x1)/1000) * i)+x1) + "\n")
        massy.append(str((((y2 - y1)/1000) * i)+y1) + "\n")
    pointsx.writelines(massx)
    pointsx.close()
    pointsy = open("pointy.txt", "w")
    pointsy.writelines(massy)
    pointsy.close()

    pointsx = open("pointx.txt")
    for i in pointsx:
        massx.append(float(i[:-1])) 
    pointsx.close()
    pointsy = open("pointy.txt")
    for i in pointsy:
        massy.append(float(i[:-1]))
    pointsy.close()

answer = int(input("Вы продолжаете парсить(1) или начали заного(2) >> "))
if answer == 1:
    filename = str(input("Введите имя файла >> "))
    maxx = int(input("Введите maxx значение(1-1000) >> "))
    point1 = int(input("Введите номер последней точки(y) >> "))
    point2 = int(input("Введите номер последней точки(x) >> "))
else:
    filename = str(input("Введите имя файла >> "))
    maxx = int(input("Введите maxx значение(1-1000) >> "))
    minn = int(input("Введите min значение(0-999) >> "))
    point1 = minn
    point2 = 0
options = webdriver.ChromeOptions()
options.add_argument("--headless")
url1 = "https://ru-ru.topographic-map.com/map-pk6jmt/Россия/?popup="
driver = webdriver.Chrome(desired_capabilities=capa, options=options)
driver.set_page_load_timeout(10)
driver.get("https://ru-ru.topographic-map.com/map-pk6jmt/Россия/?popup=55.02566%2C83.00652")
time.sleep(3)
elem = driver.find_elements(By.TAG_NAME, 'a')
elem[-1].click()
filenamelog = 'log_' + filename
z = 1
for i in range(point1, maxx+1):
    for j in range(point2, 1000):
        z = 1
        while z !=0 :
            try:
                
                stroka = str(massx[j]) + "%2C" + str(massy[i])
                url = url1 + stroka
                driver.get(url)
                time.sleep(2.5)
                elem = driver.find_element(By.XPATH, '/html/body/div/main/section[1]/div/div[1]/div[6]/div/div[1]/div').text
                elem = elem.replace(" ", '')
                elem = elem.replace("м", '')
                int(elem)
                print(i, " : ", j, " = ", elem)
                elem = elem + '\n'
                f2 = open(filenamelog, 'a')
                st = str(i)+ " " +str(j) + " " + str(massx[j]) + " : " + str(massy[i])+ "\n"
                f2.write(st)
                f2.close()
                f1 = open(filename, 'a')
                f1.write(elem)
                f1.close()
                z=0
            except:
                print("error")
                z=1
    point2=0
        
        
        
