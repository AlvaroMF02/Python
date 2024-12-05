from PIL import Image, ImageOps

def resize_image(input_path, output_path, size):
    """Redimensiona la imagen al tamaño especificado."""
    with Image.open(input_path) as img:
        img_resized = img.resize(size)
        img_resized.save(output_path)

def apply_grayscale(input_path, output_path):
    """Convierte la imagen a escala de grises."""
    with Image.open(input_path) as img:
        grayscale_img = img.convert("L")
        grayscale_img.save(output_path)

def apply_sepia(input_path, output_path):
    """Aplica un filtro sepia a la imagen."""
    with Image.open(input_path) as img:
        sepia_img = ImageOps.colorize(img.convert("L"), black="black", white="brown")
        sepia_img.save(output_path)

def rotate_image(input_path, output_path, angle):
    """Rota la imagen en el ángulo especificado."""
    with Image.open(input_path) as img:
        rotated_img = img.rotate(angle, expand=True)
        rotated_img.save(output_path)

def flip_image(input_path, output_path, mode="horizontal"):
    """Voltea la imagen horizontal o verticalmente."""
    with Image.open(input_path) as img:
        if mode == "horizontal":
            flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
        elif mode == "vertical":
            flipped_img = img.transpose(Image.FLIP_TOP_BOTTOM)
        else:
            raise ValueError("El modo debe ser 'horizontal' o 'vertical'.")
        flipped_img.save(output_path)
