from skimage.filters import threshold_yen,threshold_otsu,threshold_mean,threshold_triangle,threshold_isodata,threshold_local
import numpy as np
import cv2
from skimage.morphology import skeletonize


def RemoveShadow(img_gray,debug=False):
    #remove noise and writting on paper to leave out onlu the illumination
    dilated_img = cv2.dilate(img_gray, np.ones((7,7), np.uint8)) 
    blurred_img = cv2.medianBlur(dilated_img, 21)
    #remove any dark lighning aka shadow
    diff_img = 255 - cv2.absdiff(img_gray, blurred_img)
    norm_img = diff_img.copy()
    #normalization and word sharpening
    cv2.normalize(diff_img, norm_img, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
    _, thr_img = cv2.threshold(norm_img, 230, 0, cv2.THRESH_TRUNC)
    cv2.normalize(thr_img, thr_img, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
    if(debug):
        cv2.imwrite("shadowOut.png",norm_img)
        cv2.imwrite("thres.png",thr_img)
    return thr_img

def Binarize(img_gray,debug=False,name=""):
    thres_yen = threshold_yen(img_gray)
    thres_otsu = threshold_otsu(img_gray)
    thres_mean,thres_triangle,thres_isodata = threshold_mean(img_gray),threshold_triangle(img_gray),threshold_isodata(img_gray)
    final_yen = (img_gray > thres_yen)*255
    final_otsu = (img_gray >thres_otsu)*255
    final_mean = (img_gray >thres_mean)*255
    final_triangle = (img_gray >thres_triangle)*255
    final_isodata = (img_gray >thres_isodata)*255
    #final_local = (img_gray >thres_local)*255
    if(debug):
        cv2.imwrite(f"output/{name}_final_otsu.png",final_otsu)
        cv2.imwrite(f"output/{name}_final_yen.png",final_yen)
        cv2.imwrite(f"output/{name}_final_mean.png",final_mean)
        cv2.imwrite(f"output/{name}_final_triangle.png",final_triangle)
        cv2.imwrite(f"output/{name}_final_isodata.png",final_isodata)
        #cv2.imwrite(f"output/{name}_final_local.png",final_local)
    return final_yen,final_otsu

def Binarize_Histogram(img_gray,name=""):
    #thres_otsu = threshold_otsu(img_gray)
    ret2,thresholded_image = cv2.threshold(img_gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    hist = cv2.calcHist([thresholded_image],[0],None,[256],[0,256])
    if hist[255]< hist[0]:
        thresholded_image = 255-thresholded_image
    #cv2.imwrite(f"output/{name}_final_otsu.png",thresholded_image)
    
    return thresholded_image

def Skeletonization(img_binary,name=""):
    img_skeletonized = skeletonize((255-img_binary)/255)
    img_skeletonized = 255-(img_skeletonized*255)
    #cv2.imwrite(f"output/{name}_final_otsu.png",img_skeletonized)
    return img_skeletonized

def LaplacianEdge(img_binary,name=""):
    kernel_size = 3
    ddepth = cv2.CV_16S
    img_edge = cv2.Laplacian(img_binary, ddepth, ksize=kernel_size)
    img_edge = 255 - img_edge
    #cv2.imwrite(f"output/{name}_final_otsu.png",img_edge)
    return img_edge

def cropToText(img_binary,name=""):
    #horizontal dilation
    img = cv2.dilate(255 - img_binary, np.ones((1,int(img_binary.shape[1]*0.3)), np.uint8))
    #find the contours
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #find the biggest contour
    areas = [cv2.contourArea(c) for c in contours]
    max_index = np.argmax(areas)
    cnt = contours[max_index]
    x,y,w,h = cv2.boundingRect(cnt)
    #draw the bounding box
    #rect_img = cv2.rectangle(img_binary,(x,y),(x+w,y+h),(0,255,0),2)
    #cv2.imwrite(f"output/{name}_cropped.png",rect_img)
    #crop the image
    img_cropped = img_binary[y:y+h,x:x+w].copy()
    return img_cropped
