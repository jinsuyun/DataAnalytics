from practice import numpy as np
import cv2 as cv
from skimage import io
from matplotlib import pyplot as plt
red = np.array([[0, 80, 80], [10, 255, 255]])
orange = np.array([[13, 80, 80], [23, 255, 255]])
yellow = np.array([[25, 80, 80], [35, 255, 255]])
green = np.array([[40, 80, 80], [80, 255, 255]])
blue = np.array([[80, 80, 80], [140, 255, 255]])
pink = np.array([[145, 80, 80], [160, 255, 255]])
red_high = np.array([[170, 80, 80], [180, 255, 255]])
color_names = ["red", "orange", "yellow", "green", "blue", "pink"]
colors = [red, orange, yellow, green, blue, pink, red_high]
url = "https://lh3.googleusercontent.com/0ov1-rv3uTpw4KQphQUemyHPslZ4a8q-5C3c89lbXUKjbo9RzVaYH4F8_sMJBm4dsR0"
url = "https://lh6.ggpht.com/hIY78puIGVb26VFsWexvVe5T00nfLK9IKbg8uHKK9MwyAO0aPySjopPh1NUSMJYM2UWX"
image = io.imread(url) # Load image from url
image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV) # Converts images from BGR to HSV
ratios_dic = {}
for i in range(len(colors)):
    mask = cv.inRange(hsv, colors[i][0], colors[i][1])
    io.imshow(mask)
    plt.show()
    if i != len(colors) - 1:
        ratios_dic[color_names[i]] = np.count_nonzero(mask) / float(np.prod(mask.shape)) * 100
    else:
        ratios_dic[color_names[0]] = ratios_dic[color_names[0]] + np.count_nonzero(mask) / float(np.prod(mask.shape)) * 100
print(ratios_dic)