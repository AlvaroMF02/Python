from PIL import Image

def validate_image(image_path):
    try:
        with Image.open(image_path) as img:
            img.verify()  # Verifica la integridad del archivo
            print("Imagen válida.")
    except Exception as e:
        print(f"Error: La imagen no es válida. {e}")

# Ruta de la imagen
image_path = "C:/Users/albaro/Documents/Python/CLOUD/detectarSentimientosAzure/pringaoLLorando.jpg"
validate_image(image_path)
