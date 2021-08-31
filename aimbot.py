import pyautogui
import win32api
import win32con
import time
import keyboard


class Aimbot(object):
    def __init__(self) -> None:
        super().__init__()
        self.x = self.y = -5
        time.sleep(2)
        self.acha_alvo()

    def click(self, y, x):
        win32api.SetCursorPos((y, x))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    def acha_alvo(self):
        while keyboard.is_pressed('c') is False:
            if pyautogui.locateOnScreen('aimboot/time.png') or pyautogui.locateOnScreen('aimboot/accuracy.png'):
                imagem = pyautogui.screenshot(region=(929, 642, 275, 100))
                imagem.save('pontuacao.png')
                break
            imagem = pyautogui.screenshot(region=(676, 336, 604, 424))
            y, x = imagem.size
            for i in range(0, y, 4):
                for j in range(0, x, 4):
                    r, g, b = imagem.getpixel((i, j))
                    if r == 255 and b == 195:
                        # if not (676+i in range(self.x-5, self.x+5)) or not (336+j in range(self.y-5, self.y+5)):
                        #     self.click(676+i, 336+j)
                        #     self.x = 676+i
                        #     self.y = 336+j
                        #     break
                        self.click(676+i, 336+j)
                        time.sleep(0.01)
                        break


Aimbot()
