import cv2
import pygame
from matplotlib import pyplot as plt
def fun(c):
    landslide_region_before = cv2.imread('img1.jpg',0)
    landslide_region_after = cv2.imread('img2.jpg',0)
    if(c==1):
        landslide_region_before = cv2.imread('img2.jpg',0)
        landslide_region_after = cv2.imread('img1.jpg',0)
    y_range = [75,175]
    x_range = [75,175]

    crop_landslide_region_before =landslide_region_before[y_range[0]:y_range[1], x_range[0]:x_range[1]]

    # compute the center of the before
    M_before = cv2.moments(crop_landslide_region_before)
    bf_cX = int(M_before["m10"] / M_before["m00"])
    bf_cY = int(M_before["m01"] / M_before["m00"])

    plt.imshow(crop_landslide_region_before, origin='lower', cmap='Greys')
    plt.title('Non zero points number: ' + str(cv2.countNonZero(crop_landslide_region_before)) + ' ; center point: ' + str(bf_cX) + ' : ' + str(bf_cY))
    plt.plot(bf_cY, bf_cX, 'go')
    plt.show()

    crop_landslide_region_after = landslide_region_after[y_range[0]:y_range[1], x_range[0]:x_range[1]]
    # compute the center of the after
    M_after = cv2.moments(crop_landslide_region_after)
    at_cX = int(M_after["m10"] / M_after["m00"])
    at_cY = int(M_after["m01"] / M_after["m00"])
    if abs((bf_cX-at_cX)*2-(bf_cY-at_cY)*2)>=5:
        print("playing")
        pygame.mixer.init()
        sound=pygame.mixer.Sound('1.mp3')
        playing=sound.play()

        while playing.get_busy():
            pygame.time.delay(100)
    plt.imshow(crop_landslide_region_after, origin='lower', cmap='Greys')
    plt.title('Non zero points number: ' + str(cv2.countNonZero(crop_landslide_region_after))+ ' ; center point: ' + str(at_cX) + ' : ' + str(at_cY))
    plt.plot(at_cY, at_cX, 'ro')
    plt.show()
