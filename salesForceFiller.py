#! python3
# salesForceFiller.py - プロジェクト工数を自動で埋める

import pyautogui as pag #pyautoguiモジュールを入れる
import time
from PIL import Image
import webbrowser as wb

url = "https://teamspirit-6742.cloudforce.com/home/home.jsp"
imgPath = r"C:\Users\nishio\Dropbox\Scripts\salesForce_plusButton.png" #文字列の前にrをつけることで、バックスラッシュも文字として扱える
login_button_loc = (525, 722) #SalesForceのログインボタンの位置（縮尺率＝100％）
login_button_color = (232, 240, 254) #SalesForceのログインボタンのRGBカラー
top_header_loc = (320, 1031) #TOP画面のヘッダーの位置（縮尺率＝100％）
top_header_color = (37, 100, 152) #TOP画面のヘッダーのカラー
top_header_loc2 = (500, 284) #工数実績画面のヘッダーの位置（縮尺率＝67％）
top_header_color2 = (37, 100, 153) #工数実績画面のヘッダーのカラー

#SalesForceを開き、ログインする
wb.open(url, new=1)
print("SalesForceを開いています。少々お待ち下さい。")
while not pag.pixelMatchesColor(login_button_loc[0], login_button_loc[1], login_button_color):
    time.sleep(0.5)
print("SalesForceが開きました。")
time.sleep(1)
pag.press("enter") #Enterを押せばログイン出来る状態になっているのでEnterする

#SalesForceの工数実績のタブを選択する
while not pag.pixelMatchesColor(top_header_loc[0], top_header_loc[1], top_header_color):
    time.sleep(0.5)
print("SalesForceにログインしました。")
time.sleep(2)
pag.press("tab", presses=9, interval=0.05) #0.5秒間隔で9回タブボタンを押す
time.sleep(0.5)
pag.press("enter")
print("工数実績ページを開きました。")

#プラスボタンの数を取得して、順番に開いては、工数を入力していく
while not pag.pixelMatchesColor(top_header_loc2[0], top_header_loc2[1], top_header_color2):
    time.sleep(0.5)

print("プラスボタンの画像を取得しています。")
image_list = list(pag.locateAllOnScreen(imgPath))
print("image_listに、{}個のプラスボタンの位置が格納されました。".format(len(image_list)))
print(image_list)

for i, loc in enumerate(image_list): #インデックスと要素を同時に取得するため
    print("今、{}番目の日付の工数を登録しています。".format(i+1))
    pag.press("tab", presses=21+i, interval=0.05)
    time.sleep(1)
    pag.press("enter") #プラスボタンを押す
    time.sleep(1)
    pag.press("right") #工数バーを右に1回倒す
    time.sleep(1)
    pag.press("tab", presses=2, interval=0.05) #登録ボタンに移動する
    time.sleep(1)
    pag.press("enter") #登録ボタンを押す
    time.sleep(5) #登録反映を待つので少し長めにする
    pag.press("tab", presses=2, interval=0.05) #登録ボタンに移動する
    #pag.press("pageup", presses=2, interval=0.05)
