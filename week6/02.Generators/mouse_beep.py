import pyautogui
from pygame import mixer  # Load the popular external library


def main():
    print(pyautogui.position())
    while True:
        x = pyautogui.position().x
        y = pyautogui.position().y

        if x == y == 0:
            mixer.init()
            mixer.music.load('/home/emoto13/Downloads/CAPITAL BRA, KC REBELL & SUMMER CEM - ROLEX (prod. by Beatzarre '
                             '& Djorkaeff).mp3')
            mixer.music.play()


if __name__ == '__main__':
    main()
