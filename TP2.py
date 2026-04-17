import scipy.io as sio
import numpy as np
import cv2
import matplotlib.pyplot as plt

def affiche(image):
    data_2405=sio.loadmat(image)
    I=data_2405['I']
    dim=I.shape
    print(dim)

    plt.figure(figsize=(12, 8))
    titres = ['450nm (Bleu)', '530nm', '560nm (Vert)', '675nm (Rouge)', '730nm', '850nm (PIR)']
    for i in range(6):
        plt.subplot(3, 2, i+1) 
        plt.imshow(I[:, :, i],cmap='gray')
        plt.title(titres[i])
    plt.show()
    return I
    
I=affiche('425aa_2405')

##############################################################

I_norm=I/np.max(I)
img_vrai=I_norm[:,:,[3,2,0]] #Vraies couleurs
img_fausse=I_norm[:,:,[5,3,2]] #Fausses couleurs (végétation en rouge)

plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.imshow(img_vrai)
plt.title('Vraies Couleurs')

plt.subplot(1,2,2)
plt.imshow(img_fausse)
plt.title('Fausses Couleurs (Végétation Rouge)')
plt.show()

##############################################################

plt.figure(figsize=(12, 8))
titres=['450nm (Bleu)','530nm','560nm (Vert)','675nm (Rouge)','730nm','850nm (PIR)']

I_float = I.astype(np.float32)
for i in range(6):
    plt.subplot(3, 2, i+1)
    hist_val = cv2.calcHist([I_float], [i], None,[256],[0, 1])
    plt.plot(hist_val, color='black')
    plt.title(titres[i])
    
plt.tight_layout()
plt.show()

##############################################################

# Repérage
plt.figure(figsize=(8,8))
plt.imshow(2*I_norm[:,:,[5,3,2]]) 
plt.title("Coordonnées X Y")
plt.grid()
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# Coordonnées
x_sol,y_sol=62,111
x_veg,y_veg=52,74

profil_sol=I[x_sol,y_sol,:]
profil_veg=I[x_veg,y_veg,:]
longueurs_onde=[450,530,560,675,730,850]

plt.figure(figsize=(10,6))
plt.plot(longueurs_onde,profil_sol,marker='o',label='Sol')
plt.plot(longueurs_onde,profil_veg,color='green',marker='o',label='Végétation')

plt.title('Profils Spectraux : Betterave vs Sol')
plt.xlabel('Longueur d\'onde (nm)')
plt.ylabel('Réflectance')
plt.legend()
plt.grid()
plt.show()

#####################NDVI#######################################


R=I[:,:,3].astype(float)
PIR=I[:,:,5].astype(float)
IV=(PIR-R)/(PIR+R)
print(IV)

plt.figure(figsize=(10,8))
img_ndvi=plt.imshow(IV,cmap='jet') 
plt.colorbar(img_ndvi, label='NDVI')
plt.title('Indice de Végétation (NDVI)')
plt.show()

###################COMPARAISON#########################################

fichiers=['425aa_2405','425aa_0706','761aa_2306']
titres = ['24/05','07/06','23/06']
p=[]

fig1=plt.figure(figsize=(15, 8))
fig1.suptitle('Vraies vs Fausses Couleurs')

fig2 = plt.figure(figsize=(15, 5))
fig2.suptitle('Indices NDVI')

for i in range(len(fichiers)):
    data = sio.loadmat(fichiers[i])
    I = data['I'].astype(float)
    I_norm = I / np.max(I)
    R=I[:,:,3]
    PIR=I[:,:,5]
    IV=(PIR-R)/(PIR+R)
    
    plt.figure(fig1.number) #figure1
    plt.subplot(2,3,i+1) 
    plt.imshow(1.5*I_norm[:,:,[3,2,0]])
    plt.title(f'{titres[i]} (Vrai)')

    plt.subplot(2,3,i+4) 
    plt.imshow(1.5*I_norm[:,:,[5,3,2]])
    plt.title(f'{titres[i]} (Fausse)')
    
    plt.figure(fig2.number) #figure2
    plt.subplot(1, 3, i+1)
    plt.imshow(IV, cmap='jet')
    plt.colorbar(img_ndvi)
    plt.title(f'{titres[i]}')
    
    #CALCUL PROPORTION
    seuil=0.4
    prop=(np.sum(IV>seuil)/IV.size)*100
    p.append(prop)
    print(f"{titres[i]} : {prop:.2f}% de culture")

plt.figure(figsize=(6, 4))
plt.plot(titres, p, 'g-o')
plt.title('Proportion de culture au cours du temps')
plt.ylabel('% Couverture')
plt.grid()
plt.show()
