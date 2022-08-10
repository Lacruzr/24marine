import cv2
alto= 540
ancho=900
path = "foto.jpg"
img= cv2.imread(path)
print(f"alto , ancho = {img.shape}")
imagen= cv2.resize(img,(ancho,alto))

dibujando = False
valorx = 0
valory = 0

def dibujar(event,x,y,etiquetas,parametros):
    global dibujando,valorx,valory,imagen,original,path
    if event == cv2.EVENT_LBUTTONDOWN:
        dibujando = True
        
        valorx = x
        valory = y
    elif event == cv2.EVENT_MOUSEMOVE:
        if dibujando:
            cv2.rectangle(imagen, (valorx,valory),(x,y), (255,0,0),2)
    elif event == cv2.EVENT_LBUTTONUP:
        dibujando = False
        print(f'inicio x: {valorx} inicio y: {valory} fin x:{x} fin y: {y}')
        cv2.rectangle(imagen, (valorx,valory),(x,y),(255,0,0), 2)
        original= cv2.imread(path)
        originalr= cv2.resize(original,(ancho,alto))
        cv2.imshow("original",originalr)
        imgcrop = originalr[valory:y,valorx:x]
        print(f"alto , ancho = {imgcrop.shape}")
        imgrezi= cv2.resize(imgcrop,(900,540))
        cv2.imshow("cortada",imgrezi)
        #cv2.imshow("cortada",imgcrop)
cv2.namedWindow(winname='miImagen')
cv2.setMouseCallback('miImagen',dibujar)


while True:
   
    cv2.imshow('miImagen',imagen)
    if cv2.waitKey(10) & 0xFF == 27:
        break
cv2.destroyAllWindows()

