#! python3
# mouseNow.py

import pyautogui
print('中断するには、Ctrl-Cを押して下さい。')

try:
    while True:
        x, y = pyautogui.position()
        position_str = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        pixel_color = pyautogui.screenshot().getpixel((x, y))
        position_str += ' RGB: (' + str(pixel_color[0]).rjust(3)
        position_str += ', ' + str(pixel_color[1]).rjust(3)
        position_str += ', ' + str(pixel_color[2]).rjust(3) + ')'
        print(position_str, end='') #引数endをとることでデフォルト改行表示をやめる
        print('\b' * len(position_str), end='', flush=True) #\b*len()で文字数分バックスペースする

except KeyboardInterrupt:
    print('\n終了。')
