from image_tools import cargarImagen, guardarImagen, redimensionar, ponerFiltro, rotar, voltear

# Cargar imagen
image = cargarImagen("miau.jpg")


# Redimensionar
image_resized = redimensionar(image, 200, 200)
guardarImagen(image_resized, "imagen_redimensionada.jpg")

# Aplicar filtro sepia
image_sepia = ponerFiltro(image, "sepia")
guardarImagen(image_sepia, "imagen_sepia.jpg")

# Rotar
image_rotated = rotar(image, 45)
guardarImagen(image_rotated, "imagen_rotada.jpg")

# Voltear horizontalmente
image_flipped = voltear(image, "horizontal")
guardarImagen(image_flipped, "imagen_volteada.jpg")
