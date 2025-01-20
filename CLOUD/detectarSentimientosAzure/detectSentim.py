from azure.cognitiveservices.vision.face import FaceClient
from azure.cognitiveservices.vision.face.models import FaceAttributeType
from msrest.authentication import CognitiveServicesCredentials
import os

# Configuración del cliente Face API
subscription_key = "95vLuV7cIMAwDdkmzOVJWtD9HB47z18E64WHyQXePgpFexyKS8VsJQQJ99BAACYeBjFXJ3w3AAAKACOGZLMD"  # Reemplaza con tu clave
endpoint = "https://detectarsentimient.cognitiveservices.azure.com/"  # Reemplaza con tu endpoint

# Crear el cliente de Face API
face_client = FaceClient(endpoint, CognitiveServicesCredentials(subscription_key))

def detect_emotions_in_image(image_path):
    """
    Detecta emociones en una imagen utilizando Azure Face API con manejo de errores.
    """
    try:
        # Verificar si el archivo de imagen existe
        if not os.path.exists(image_path):
            print(f"Error: La imagen no se encontró en la ruta {image_path}")
            return

        # Verificar que la imagen sea válida
        from PIL import Image
        try:
            image = Image.open(image_path)
            image.verify()
        except Exception as e:
            print(f"Error: La imagen no es válida. {e}")
            return

        # Leer la imagen como binario
        with open(image_path, "rb") as image_file:
            # Detectar caras en la imagen
            detected_faces = face_client.face.detect_with_stream(
                image=image_file,
                return_face_attributes=[FaceAttributeType.emotion]
            )
        
        if not detected_faces:
            print("No se detectaron caras en la imagen.")
            return

        # Mostrar emociones detectadas
        for idx, face in enumerate(detected_faces):
            emotions = face.face_attributes.emotion
            print(f"Rostro {idx + 1}:")
            print(f" - Alegría: {emotions.happiness}")
            print(f" - Tristeza: {emotions.sadness}")
            print(f" - Sorpresa: {emotions.surprise}")
            print(f" - Ira: {emotions.anger}")
            print(f" - Neutral: {emotions.neutral}")
            print("")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ruta a la imagen local
image_path = "C:/Users/albaro/Documents/Python/CLOUD/detectarSentimientosAzure/pringaoLLorando.jpg"

# Llamar a la función para analizar emociones 
detect_emotions_in_image(image_path)
