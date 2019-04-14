import numpy as np
import cv2

def criar_linha(clique, x, y, flags, parametros):
	global x1, x2, y1, y2
	global imagem
	img = imagem


	while(clique == cv2.EVENT_LBUTTONDOWN):
		if (clique == cv2.EVENT_LBUTTONDOWN):
			x1 = x
			y1 = y
			break
	while(clique == cv2.EVENT_LBUTTONUP):
		if (clique == cv2.EVENT_LBUTTONUP):
			x2 = x
			y2 = y
			break
	if (x1 != -1 and x2 != -1):
		Distancia = ((x1-x2)**2 + (y1-y2)**2)**0.5
		print Distancia
		cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
		cv2.imshow("teste", img)
		imagem = cv2.imread("testeG.jpeg")
		x1 = -1	
		x2 = -1	
	
x1 = -1
y1 = -1
x2 = -1
y2 = -1
	
imagem = cv2.imread("testeG.jpeg")

cv2.imshow("teste", imagem)

cv2.setMouseCallback("teste", criar_linha)


cv2.waitKey(0)