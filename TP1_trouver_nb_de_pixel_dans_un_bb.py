import numpy as np
import cv2
import matplotlib.pyplot as plt

def rgb2grey(img):
    img=img.astype('float')
    imagegrey=(img[:,:,0]+img[:,:,1]+img[:,:,2])/3
    imagegrey=imagegrey.astype('uint8')
    return imagegrey
    

def histogramme(img):
    h=np.zeros(256,dtype=int)
    dim=img.shape 
    for i in range(dim[0]):
        for j in range(dim[1]):
            val=img[i,j]
            h[val]+=1
    return h

def binarisation(img,seuil):
    dim=img.shape 
    for i in range(dim[0]):
        for j in range(dim[1]):
            if img[i,j]>=seuil:
                img[i,j]=255
            else:
                img[i,j]=0
    return img
    
image = cv2.imread("test_3bb_blancs.png")
print(image.shape)

cv2.imshow("imagergb",image)
cv2.waitKey(0) 

imgg=rgb2grey(image)
cv2.imshow("imagegrey",imgg)
cv2.waitKey(0)

h=histogramme(imgg)
plt.plot(h)
plt.show()


seuil=110
imgb=binarisation(imgg,seuil)
cv2.imshow("imagebinarisation",imgb)
cv2.waitKey(0)

h2=histogramme(imgb)
plt.plot(h2)
plt.show()

#nb de bb
nbbb=3
#nb pixels par bb
nb=h2[255]/nbbb
print(nb)

plt.close("all")
cv2.destroyAllWindows()