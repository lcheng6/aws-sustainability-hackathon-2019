import numpy as np
from matplotlib import colors
from scipy.spatial import cKDTree as KDTree
from scipy import misc
import cv2
import matplotlib.pyplot as plt
# from matplotlib.pyplot import imread
# from scipy.misc import imread



def apply_mask(img1,cloud_cover):
    thresh = 100
    cloud_cover = cv2.threshold(cloud_cover, thresh,255, cv2.THRESH_BINARY)[1]
    cloud_cover = cv2.bitwise_not(cloud_cover)
    cloud_cover = cv2.resize(cloud_cover, img1.shape[1::-1])
    dst = cv2.bitwise_and(img1,img1,mask = cloud_cover)
    return dst

def count_greens(img):
    REDUCED_COLOR_SPACE = True

    # borrow a list of named colors from matplotlib
    if REDUCED_COLOR_SPACE:
        use_colors = {k: colors.cnames[k] for k in ['red', 'green', 'blue', 'black', 'yellow', 'purple']}
    else:
        use_colors = colors.cnames
    # translate hexstring to RGB tuple
    named_colors = {k: tuple(map(int, (v[1:3], v[3:5], v[5:7]), 3*(16,)))
                for k, v in use_colors.items()}
    ncol = len(named_colors)

    if REDUCED_COLOR_SPACE:
        ncol -= 1
        no_match = named_colors.pop('purple')
    else:
        no_match = named_colors['purple']

    # make an array containing the RGB values 
    color_tuples = list(named_colors.values())
    color_tuples.append(no_match)
    color_tuples = np.array(color_tuples)

    color_names = list(named_colors)
    color_names.append('no match')
    # build tree
    tree = KDTree(color_tuples[:-1])
    # tolerance for color match `inf` means use best match no matter how
    # bad it may be
    tolerance = np.inf
    # find closest color in tree for each pixel in picture
    dist, idx = tree.query(img, distance_upper_bound=tolerance)
    # count and reattach names
    counts = dict(zip(color_names, np.bincount(idx.ravel(), None, ncol+1)))
    return counts['green']

def compare_greens(img1,img2):
    print('Green Pixels on Day1 : ' + str(count_greens(img1)))
    print('Green Pixels on Day2 : ' + str(count_greens(img2)))
    #Do the required calculations
    return

def main():
    img1 = misc.imread('../sample-data/nvdi-customized-1.png',mode = 'RGB') #RGB image on Day1
    img2 = misc.imread('../sample-data/nvdi-customized-5.png',mode = 'RGB') #RGB image on Day2
    img1_1 = cv2.imread('../sample-data/cloud-1.jpeg',cv2.IMREAD_GRAYSCALE) #Cloud Image on Day1
    img2_2 = cv2.imread('../sample-data/cloud-5.jpeg',cv2.IMREAD_GRAYSCALE) #Cloud image on Day2
    masked_img1 = apply_mask(img1,img1_1)
    masked_img2 = apply_mask(img2,img2_2)
    compare_greens(masked_img1,masked_img2) 
if __name__ == '__main__':
    main()
    
    
