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

def arrondi_bonbons(nbbb):
    nbbb_arrondi = int(nbbb+0.5)
    print("Nombre de bonbons :",nbbb_arrondi)
    return nbbb_arrondi
    
image = cv2.imread("test_7bb_blancs.png")
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

####### Nombre de Pixels dans l'image ##########
pixel=3800 #nb pixel par bb
nbbb=h2[255]/pixel
print("Nombre de bonbons (arrondi) :",nbbb)
nbbb_exact=arrondi_bonbons(nbbb)

####### Nombre de Pixels dans 1 bonbon ##########
# nbbb=3 #nb de bb
# nb=h2[255]/nbbb #nb pixels par bb
# print(nb)

plt.close("all")
cv2.destroyAllWindows()