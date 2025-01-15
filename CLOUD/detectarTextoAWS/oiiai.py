import boto3

def extract_text_from_image(file_path):
    """
    Extrae texto de una imagen usando Amazon Textract.

    Args:
        file_path (str): Ruta al archivo de imagen.
    Returns:
        list: Lista de líneas de texto extraídas.
    """
    # Crear cliente de Textract
    textract_client = boto3.client('textract')

    # Leer la imagen como bytes
    with open(file_path, 'rb') as image_file:
        image_bytes = image_file.read()

    # Llamar a Textract para detectar texto
    response = textract_client.detect_document_text(
        Document={'Bytes': image_bytes}
    )

    # Extraer texto de las líneas detectadas
    lines = []
    for block in response['Blocks']:
        if block['BlockType'] == 'LINE':
            lines.append(block['Text'])

    return lines

# Ruta de tu archivo de imagen
image_path = "C:/Users/albaro/Documents/Python/CLOUD/detectarTextoAWS/documento.jpg"

# Ejecutar función y mostrar resultados
extracted_text = extract_text_from_image(image_path)
print("Texto extraído:")
for line in extracted_text:
    print(line)
