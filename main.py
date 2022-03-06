import random

import kivy

kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from paddleocr import PaddleOCR, draw_ocr
import cv2


class MyRoot(BoxLayout):
    def __init__(self):
        super(MyRoot, self).__init__()

    def generate_number(self):
        self.random_label.text = str(random.randint(0, 2000))
        cap = cv2.VideoCapture(0)


        while True:
            success, img = cap.read()

            # Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
            # 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
            ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # need to run only once to download and load model into memory
            img_path = 'C:/OCR/ppocr_img/imgs/11.jpg'
            result = ocr.ocr(img, cls=True)
            for line in result:
                print(line)
            # if result.__sizeof__() > 2:
            #     print('测试打印日志：' + result[2][1][0].__str__())

            cv2.imshow('img', img)
            k = cv2.waitKey(1)
            if k == 27:
                break;
        cap.release()


class RandomNumber(App):
    def build(self):
        return MyRoot()


randomApp = RandomNumber()
randomApp.run()
