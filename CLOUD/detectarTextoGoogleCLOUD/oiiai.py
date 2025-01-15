from google.cloud import vision
import os
 
def recognize_text_from_image(image_path):
    """
    Recognize and extract text from an image using Google Cloud Vision API.
 
    Args:
        image_path (str): Path to the image file.
 
    Returns:
        str: Extracted text from the image.
    """
    # Initialize a Vision API client
    client = vision.ImageAnnotatorClient()
 
    # Read the image file
    with open(image_path, "rb") as image_file:
        content = image_file.read()
 
    # Construct an Image object for the API
    image = vision.Image(content=content)
 
    # Perform text detection
    response = client.text_detection(image=image)
    texts = response.text_annotations
 
    if response.error.message:
        raise Exception(f"API Error: {response.error.message}")
 
    # Return the full text detected (first element in the annotations list)
    if texts:
        return texts[0].description
    else:
        return "No text detected."
 
if __name__ == "__main__":
    # Configurar credenciales
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:/Users/albaro/Documents/Python/CLOUD/detectarTextoGoogleCLOUD/credenciales/google-cloud-credentials.json'
 
    # Path to the image file
    image_path = "C:/Users/albaro/Documents/Python/CLOUD/detectarTextoGoogleCLOUD/documento.jpg"
 
    try:
        # Call the function and print the result
        extracted_text = recognize_text_from_image(image_path)
        print("Extracted Text:")
        print(extracted_text)
    except Exception as e:
        print(f"Error: {e}")
 
 