from PIL import Image, ImageOps

def cargarImagen(ruta):
    """
    Carga una imagen desde una ruta q se pasa
    """
    return Image.open(ruta)

def guardarImagen(image, rutaGuard):
    """
    guarda la ruta
    """
    image.save(rutaGuard)

def redimensionar(image, ancho, alto):
    """
    redimensiona la imagen
    """
    return image.resize((ancho, alto))

def ponerFiltro(image, filtro):
    """
    aplicar filtro a la imagen
    """
    if filtro == 'grayscale':
        return ImageOps.grayscale(image)
    elif filtro == 'sepia':
        return ImageOps.colorize(ImageOps.grayscale(image), '#704214', '#C0A080')
    else:
        raise ValueError("Filtro no soportado. Usa 'grayscale' o 'sepia'.")

def rotar(image, angulo):
    """
    gira la imagen en x angulo
    """
    return image.rotate(angulo, expand=True)

def voltear(image, direcc):
    """
    Voltea la imagen
    """
    if direcc == 'horizontal':
        return ImageOps.mirror(image)
    elif direcc == 'vertical':
        return ImageOps.flip(image)
    else:
        raise ValueError("Dirección no soportada. Usa 'horizontal' o 'vertical'.")
