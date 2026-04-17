import scipy.io as sio
import numpy as np
import cv2
import matplotlib.pyplot as plt

###################################

def histogramme(img):
    h=np.zeros(256,dtype=int)
    dim=img.shape 
    for i in range(dim[0]):
        for j in range(dim[1]):
            val=img[i,j]
            h[val]+=1
    return h

def classif_ED(img,sable,posi,caulerpa):
    img=img.astype(float)
    d_sable=np.linalg.norm(img-sable,axis=2)
    d_posi=np.linalg.norm(img-posi,axis=2)
    d_caulerpa=np.linalg.norm(img-caulerpa,axis=2)
    
    resultat=np.zeros_like(img)
    
    mask_sable=(d_sable<d_posi)&(d_sable<d_caulerpa)
    resultat[mask_sable]=[0,255,255]
    
    mask_posi=(d_posi<d_sable)&(d_posi<d_caulerpa)
    resultat[mask_posi]=[255,0,0]
    
    mask_caulerpa=(d_caulerpa<d_posi)&(d_caulerpa<d_sable)
    resultat[mask_caulerpa]=[0,255,0]
    
    return resultat

def classif_SAM(img,sable,posi,caulerpa):
    img=img.astype(float)
    norm_img=np.linalg.norm(img,axis=2)
    
    def angle(img,moyenne):
        top=np.sum(img*moyenne,axis=2)
        norm_classe=np.linalg.norm(moyenne)
        cos=top/(norm_img*norm_classe)
        return np.arccos(cos)
    
    angle_sable=angle(img,sable)
    angle_posi=angle(img,posi)
    angle_caul=angle(img,caulerpa)
    
    resultat=np.zeros_like(img)
    
    mask_sable=(angle_sable<angle_posi)&(angle_sable<angle_caul)
    resultat[mask_sable]=[0,255,255]

    mask_posi=(angle_posi<angle_sable)&(angle_posi<angle_caul)
    resultat[mask_posi]=[255,0,0]

    mask_caul=(angle_caul<angle_sable)&(angle_caul<angle_posi)
    resultat[mask_caul]=[0,255,0] 
    
    return resultat
    
    

###################################

image = cv2.imread("image fond ifremer.tif")
print(image.shape)

cv2.imshow("image",image)
cv2.waitKey(0)

################################

R=image[:,:,0]
V=image[:,:,1]
B=image[:,:,2]
bandes=[R,V,B]
noms=['Rouge','Vert','Bleu']
    
plt.figure(figsize=(12,8))
for i in range(3):
    plt.subplot(2,3,i+1)
    plt.imshow(bandes[i],cmap='gray')
    plt.title(noms[i])
    h =histogramme(bandes[i])
        
    plt.subplot(2,3,i+4)
    plt.bar(range(256),h)
    plt.title(f"Histo{noms[i]}")
    plt.xlim([0,255])
plt.tight_layout()
plt.show()

##########################"######

classes=["Sable","Posidonie","Caulerpa"]
couleurs = {"Sable":"yellow","Posidonie":"blue","Caulerpa":"lime"}
moyennes={}

for n in classes:
    r=cv2.selectROI(image)
    x,y,w,h=r
    roi=image[y:y+h,x:x+w]
    moyenne=np.mean(roi,axis=(0,1))
    moyennes[n]=moyenne
    print(f"Moyenne: R={moyenne[0]:},V={moyenne[1]:},B={moyenne[2]:}")

plt.figure(figsize=(12,8))

for nom, vals in moyennes.items():
    plt.plot(noms,vals,label=nom,color=couleurs[nom])

plt.title("Profils Spectraux")
plt.ylabel("Valeur (0-255)")
plt.legend()
plt.grid()
plt.show()

#################################

img_classif_ED=classif_ED(image,moyennes["Sable"],moyennes["Posidonie"],moyennes["Caulerpa"])

cv2.imshow("Classification Euclidienne",img_classif_ED)
cv2.waitKey(0)

#############################"###

img_classif_SAM=classif_SAM(image,moyennes["Sable"],moyennes["Posidonie"],moyennes["Caulerpa"])

cv2.imshow("Classification Spectral Angle Mapper",img_classif_SAM)
cv2.waitKey(0)























plt.close("all")
cv2.destroyAllWindows() 