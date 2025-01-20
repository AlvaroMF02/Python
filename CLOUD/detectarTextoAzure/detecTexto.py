from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from msrest.authentication import CognitiveServicesCredentials
import time
import os

# Configuración del cliente de Azure
subscription_key = "AxRrmt7TaJS5WSTB0VplA6IQoXmq9G3PJRBiuDU5hA5hbjcD1wLuJQQJ99BAACYeBjFXJ3w3AAAFACOGp2hv"
endpoint = "https://pruebalecturatexto.cognitiveservices.azure.com/"

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

def extract_text_from_image(image_path):
    """
    Extrae texto de una imagen local usando Azure Computer Vision Read API.
    """
    # Leer la imagen local como binario
    with open(image_path, "rb") as image_file:
        # Enviar la solicitud al servicio Read API
        read_response = computervision_client.read_in_stream(image_file, raw=True)
    
    # Obtener el ID de operación para rastrear el estado
    operation_location = read_response.headers["Operation-Location"]
    operation_id = operation_location.split("/")[-1]
    
    # Esperar hasta que la operación esté completada
    while True:
        result = computervision_client.get_read_result(operation_id)
        if result.status not in ['notStarted', 'running']:
            break
        print("Procesando la imagen...")
        time.sleep(1)
    
    # Procesar el resultado si la operación fue exitosa
    if result.status == OperationStatusCodes.succeeded:
        for page in result.analyze_result.read_results:
            for line in page.lines:
                print(line.text)  # Mostrar cada línea de texto extraída
    else:
        print("No se pudo extraer texto de la imagen.")

# Ruta de la imagen local
image_path = "C:/Users/albaro/Documents/Python/CLOUD/detectarTextoAzure/images.jpg"

# Asegurarse de que la imagen existe antes de procesarla
if os.path.exists(image_path):
    extract_text_from_image(image_path)
else:
    print(f"La imagen no se encontró en la ruta: {image_path}")
