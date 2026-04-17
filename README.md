# 👁️ Computer Vision & Image Analysis

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV" />
  <img src="https://img.shields.io/badge/Image_Processing-FF6F00?style=for-the-badge&logo=image&logoColor=white" alt="Computer Vision" />
  <img src="https://img.shields.io/badge/Data_Analysis-0052CC?style=for-the-badge&logo=data&logoColor=white" alt="Data Analysis" />
</div>

---

## 🇬🇧 English Version

### 📖 Overview
* 🎯 **Challenge:** Extract actionable data from various visual inputs, addressing specific challenges in industrial automation, agriculture, and oceanography.
* 🛠️ **Solution:** Developed a suite of Python pipelines utilizing OpenCV and NumPy. Techniques applied include histogram-based binarization for object counting, multispectral image analysis (NDVI) for crop monitoring, and supervised classification algorithms (Spectral Angle Mapper vs. Euclidean Distance) for seabed mapping.
* 📈 **Impact:** Demonstrated versatility in applied computer vision. Successfully automated object counting, quantified crop growth over time, and proved that the Spectral Angle Mapper algorithm significantly outperforms standard Euclidean distance by mitigating shadow and depth artifacts in underwater environments.

### 🧠 Core Methodologies

The project is divided into three distinct real-world applications:

#### 1. Industrial Vision: Automated Object Counting
* **Method:** Processed grayscale images using histogram analysis to identify optimal binarization thresholds.
* **Process:** Isolated the objects (candies) from the background, calculated the average number of pixels per object via a calibration step, and developed an algorithm to estimate the total count in new, unknown images based on the total active pixel area.

#### 2. Remote Sensing: Agricultural Monitoring
* **Method:** Analyzed multispectral imagery captured by a drone over a beetroot field across different dates.
* **Process:** Generated true and false-color composites. Calculated the Normalized Difference Vegetation Index (NDVI) using the Red and Near-Infrared (NIR) bands. Applied thresholding to the NDVI maps to calculate and visualize the precise percentage of crop coverage over time, providing actionable data on plant growth.

#### 3. Underwater Mapping: Seabed Classification
* **Method:** Addressed the complex lighting challenges of underwater photography to map sand, *Posidonia* seagrass, and *Caulerpa* algae.
* **Process:** Extracted Regions of Interest (ROI) to establish the spectral signatures (mean RGB values) for each class. Compared two supervised classification methods:
  * **Euclidean Distance:** Often misclassified dark areas or shadows as *Posidonia*.
  * **Spectral Angle Mapper (SAM):** Evaluated the "angle" (color profile) rather than the magnitude (brightness). This method successfully ignored lighting variations and shadows, producing a much more accurate and robust seabed map.

### 💻 Code Structure
The repository contains modular Python scripts for each application:
* `TP1_trouver_nb_de_bb_dans_img.py` & `TP1_trouver_nb_de_pixel_dans_un_bb.py`: Scripts for histogram generation, binarization, and object counting calibration.
* `TP2.py`: Pipeline for loading `.mat` multispectral data, generating NDVI heatmaps, and calculating coverage percentages.
* `TP3.py`: Implementation of ROI extraction and the Euclidean Distance classification algorithm.

### 📂 Documentation & Media
* **Media:** A video overview (`vision.mp4`) and various input/output images are included.
* **Technical Report:** A comprehensive PDF report (`Traitement_d_images.pdf`) details the algorithms, mathematical formulas (like NDVI and SAM), and a comparative analysis of the classification results.

### ⚖️ Copyright & License
This project was developed during the Computer Vision module at SeaTech Engineering School. The code and reports are intended for educational demonstration within this portfolio.

---
---

## 🇫🇷 Version Française

### 📖 Vue d'ensemble
* 🎯 **Défi :** Extraire des données exploitables à partir de diverses entrées visuelles, en répondant à des problématiques spécifiques dans l'automatisation industrielle, l'agriculture et l'océanographie.
* 🛠️ **Solution :** Développement d'une suite de pipelines en Python utilisant OpenCV et NumPy. Les techniques appliquées incluent la binarisation par histogramme pour le comptage d'objets, l'analyse d'images multispectrales (NDVI) pour le suivi des cultures, et des algorithmes de classification supervisée (Spectral Angle Mapper vs Distance Euclidienne) pour la cartographie des fonds marins.
* 📈 **Impact :** Démonstration d'une grande polyvalence en vision par ordinateur appliquée. Automatisation réussie du comptage d'objets, quantification de la croissance des cultures au fil du temps, et preuve que l'algorithme SAM surpasse nettement la distance Euclidienne classique en atténuant les artefacts d'ombre et de profondeur en milieu sous-marin.

### 🧠 Méthodologies Principales

Le projet est divisé en trois applications concrètes :

#### 1. Vision Industrielle : Comptage Automatisé d'Objets
* **Méthode :** Traitement d'images en niveaux de gris via l'analyse d'histogrammes pour identifier les seuils de binarisation optimaux.
* **Processus :** Isolement des objets (bonbons) par rapport au fond, calcul du nombre moyen de pixels par objet via une étape de calibration, et développement d'un algorithme pour estimer le nombre total dans de nouvelles images en fonction de la surface totale des pixels actifs.

#### 2. Télédétection : Suivi Agricole
* **Méthode :** Analyse d'images multispectrales capturées par un drone au-dessus d'un champ de betteraves à différentes dates.
* **Processus :** Génération de compositions en vraies et fausses couleurs. Calcul de l'Indice de Végétation par Différence Normalisée (NDVI) en utilisant les bandes Rouge et Proche Infrarouge (PIR). Application d'un seuillage sur les cartes NDVI pour calculer et visualiser le pourcentage précis de couverture végétale au fil du temps.

#### 3. Cartographie Sous-marine : Classification des Fonds
* **Méthode :** Résolution des défis complexes d'éclairage de la photographie sous-marine pour cartographier le sable, la *Posidonie* et l'algue *Caulerpa*.
* **Processus :** Extraction de Régions d'Intérêt (ROI) pour établir les signatures spectrales (valeurs RVB moyennes) de chaque classe. Comparaison de deux méthodes de classification supervisée :
  * **Distance Euclidienne :** Tendance à classer à tort les zones sombres ou les ombres comme de la *Posidonie*.
  * **Spectral Angle Mapper (SAM) :** Évaluation de l'"angle" (profil de couleur) plutôt que de la magnitude (luminosité). Cette méthode a ignoré avec succès les variations d'éclairage, produisant une carte des fonds marins beaucoup plus précise et robuste.

### 💻 Structure du Code
Le dépôt contient des scripts Python modulaires pour chaque application :
* `TP1_trouver_nb_de_bb_dans_img.py` & `TP1_trouver_nb_de_pixel_dans_un_bb.py` : Scripts pour la génération d'histogrammes, la binarisation et la calibration du comptage.
* `TP2.py` : Pipeline pour charger les données multispectrales (`.mat`), générer des cartes de chaleur NDVI et calculer les pourcentages de couverture.
* `TP3.py` : Implémentation de l'extraction de ROI et de l'algorithme de classification par Distance Euclidienne.

### 📂 Documentation & Médias
* **Médias :** Une vidéo de présentation (`vision.mp4`) et diverses images d'entrée/sortie sont incluses.
* **Rapport Technique :** Un rapport PDF complet (`Traitement_d_images.pdf`) détaille les algorithmes, les formules mathématiques (NDVI, SAM) et une analyse comparative des résultats de classification.

### ⚖️ Droits d'auteur & Licence
Ce projet a été développé dans le cadre du module Capteurs-Vision à l'école d'ingénieurs SeaTech. Le code et les rapports sont destinés à une démonstration éducative au sein de ce portfolio.
