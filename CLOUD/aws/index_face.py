import boto3
import json

def format_confidence(confidence):
    return f"{confidence:.2f}%"

def print_face_analysis(response):
    print("\n=== ANÁLISIS FACIAL ===\n")
    
    for face_record in response['FaceRecords']:
        face = face_record['Face']
        detail = face_record['FaceDetail']
        
        print("🆔 INFORMACIÓN BÁSICA")
        print(f"├── ID del Rostro: {face['FaceId']}")
        print(f"├── ID Externo: {face['ExternalImageId']}")
        print(f"└── Confianza de detección: {format_confidence(face['Confidence'])}\n")
        
        print("👤 CARACTERÍSTICAS DEMOGRÁFICAS")
        print(f"├── Rango de edad: {detail['AgeRange']['Low']} - {detail['AgeRange']['High']} años")
        print(f"└── Género: {('Masculino' if detail['Gender']['Value'] == 'Male' else 'Femenino')} "
              f"({format_confidence(detail['Gender']['Confidence'])})\n")
        
        print("😀 EXPRESIONES Y CARACTERÍSTICAS")
        print(f"├── Sonriendo: {'Sí' if detail['Smile']['Value'] else 'No'} "
              f"({format_confidence(detail['Smile']['Confidence'])})")
        print(f"├── Ojos abiertos: {'Sí' if detail['EyesOpen']['Value'] else 'No'} "
              f"({format_confidence(detail['EyesOpen']['Confidence'])})")
        print(f"├── Boca abierta: {'Sí' if detail['MouthOpen']['Value'] else 'No'} "
              f"({format_confidence(detail['MouthOpen']['Confidence'])})")
        print(f"├── Barba: {'Sí' if detail['Beard']['Value'] else 'No'} "
              f"({format_confidence(detail['Beard']['Confidence'])})")
        print(f"└── Bigote: {'Sí' if detail['Mustache']['Value'] else 'No'} "
              f"({format_confidence(detail['Mustache']['Confidence'])})\n")
        
        print("👓 ACCESORIOS")
        print(f"├── Lentes: {'Sí' if detail['Eyeglasses']['Value'] else 'No'} "
              f"({format_confidence(detail['Eyeglasses']['Confidence'])})")
        print(f"└── Lentes de sol: {'Sí' if detail['Sunglasses']['Value'] else 'No'} "
              f"({format_confidence(detail['Sunglasses']['Confidence'])})\n")
        
        print("😊 EMOCIONES DETECTADAS")
        emotions = sorted(detail['Emotions'], key=lambda x: x['Confidence'], reverse=True)
        emotion_translate = {
            'HAPPY': 'Feliz',
            'SAD': 'Triste',
            'ANGRY': 'Enojado',
            'CONFUSED': 'Confundido',
            'DISGUSTED': 'Disgustado',
            'SURPRISED': 'Sorprendido',
            'CALM': 'Calmado',
            'FEAR': 'Asustado'
        }
        for emotion in emotions[:3]:  # Mostrar solo las 3 emociones principales
            if emotion['Confidence'] > 1:  # Mostrar solo si la confianza es mayor al 1%
                print(f"├── {emotion_translate[emotion['Type']]}: {format_confidence(emotion['Confidence'])}")
        print()
        
        print("📊 CALIDAD DE LA IMAGEN")
        print(f"├── Brillo: {format_confidence(detail['Quality']['Brightness'])}")
        print(f"└── Nitidez: {format_confidence(detail['Quality']['Sharpness'])}\n")
        
        print("📐 POSE DE LA CARA")
        print(f"├── Rotación: {detail['Pose']['Roll']:.1f}°")
        print(f"├── Giro lateral: {detail['Pose']['Yaw']:.1f}°")
        print(f"└── Inclinación: {detail['Pose']['Pitch']:.1f}°\n")

def index_face():
    client = boto3.client('rekognition', region_name='us-east-1')
    
    try:
        with open('C:/Users/albaro/Downloads/aws-20250115T172320Z-001/aws/imagen.jpg', 'rb') as image: # cambiar la ruta
            response = client.index_faces(
                CollectionId='mi-coleccion-rostros',
                Image={'Bytes': image.read()},
                ExternalImageId='persona1',
                DetectionAttributes=['ALL']
            )
        
        print_face_analysis(response)
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    index_face()