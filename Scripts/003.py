import cv2
import matplotlib.pyplot as plt
import numpy as np
import requests

# Baixar a imagem
ImgBytes = requests.get("https://raw.githubusercontent.com/AngeloDev-New/IC_Milho_Acompanhamento/refs/heads/main/img.png").content

# Converter bytes em array NumPy e decodificar para imagem
img_array = np.asarray(bytearray(ImgBytes), dtype=np.uint8)
img = cv2.imdecode(img_array, cv2.IMREAD_UNCHANGED)

# Converter para escala de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
limiar =170 #@param {type: "slider",min:0,max:255,steo:1}
# val,tresh = cv2.threshold(gray,limiar,255,cv2.THRESH_BINARY)
# val,tresh = cv2.threshold(gray,limiar,255,cv2.THRESH_BINARY_INV)
# val,tresh = cv2.threshold(gray,limiar,255,cv2.THRESH_TRUNK)
# val,tresh = cv2.threshold(gray,limiar,255,cv2.THRESH_TOZERO)
val,tresh = cv2.threshold(gray,limiar,255,cv2.THRESH_TOZERO_INV)
gray = tresh

# Configurar o Matplotlib para tela cheia
plt.figure(figsize=(12, 8))  # Configura o tamanho da figura
plt.imshow(gray, cmap='gray')
plt.axis('off')  # Remove os eixos
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)  # Remove margens/bordas
plt.show()
