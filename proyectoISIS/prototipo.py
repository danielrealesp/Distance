import cv2
import os

class Distance():
    def Distance(self):
        self.ANCHO_CONOCIDO_CM = 25
        self.DISTANCIA_CONOCIDA_CM = 30

    def app(self, focal, distMaxima):

        cascPath=os.path.dirname(cv2.__file__)+"/data/haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascPath)

        video_capture = cv2.VideoCapture(0)
        while True:
            # Capture frame-by-frame
            ret, frames = video_capture.read()
            gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
            )

            # Draw a rectangle around the faces

            for (x, y, w, h) in faces:
                distancia = self.calcularDistancia(self.ANCHO_CONOCIDO_CM, focal, w) 
                color = (0,0,255) if distancia < distMaxima else (0,255,0)
                cv2.putText( frames ,str(distancia) , (x, y),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0,0), 2)
                cv2.rectangle(frames, (x, y), (x+w, y+h), color  , 2)

        # Display the resulting frame

            cv2.imshow('Video', frames)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        video_capture.release()
        cv2.destroyAllWindows()

    def calcularDistancia(knownWidth, focalLength, perWidth):
        return (knownWidth * focalLength) / perWidth


    def calibrarFocal(self ,imagePath):
        respuesta = 0
        #Constantes conocidas
        image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cascPath=os.path.dirname(cv2.__file__)+"/data/haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascPath)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=3,
            minSize=(30, 30)
        )

        #Verificar que sólo exista 1 cara para calibrar
        if (len(faces) == 0):
            print("No se encontraron caras")
    
        elif(len(faces) == 1):
            #Iterar sobre las tuplas
            for (x, y, w, h) in faces:
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                respuesta =  (w * self.DISTANCIA_CONOCIDA_CM)/self.ANCHO_CONOCIDO_CM

        else:
            print("Repita la calibración, se encontró más de 1 cara")

        print("Se encontraron: " +  str(len(faces)))

        status = cv2.imwrite('faces_detected.jpg', image)

        return respuesta

####### Prueba Preeliminar






