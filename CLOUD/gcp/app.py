
from flask import Flask, request, jsonify, render_template
from google.cloud import vision
import os

app = Flask(__name__)

# Configurar credenciales
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'credenciales/google-cloud-credentials.json'

def get_likelihood_score(likelihood):
    # Convertir el enum de likelihood a un valor numérico
    likelihood_dict = {
        vision.Likelihood.UNKNOWN: 0,
        vision.Likelihood.VERY_UNLIKELY: 1,
        vision.Likelihood.UNLIKELY: 2,
        vision.Likelihood.POSSIBLE: 3,
        vision.Likelihood.LIKELY: 4,
        vision.Likelihood.VERY_LIKELY: 5
    }
    return likelihood_dict.get(likelihood, 0)

def get_dominant_emotion(face):
    emotions = {
        'Alegría': get_likelihood_score(face.joy_likelihood),
        'Tristeza': get_likelihood_score(face.sorrow_likelihood),
        'Enojo': get_likelihood_score(face.anger_likelihood),
        'Sorpresa': get_likelihood_score(face.surprise_likelihood)
    }
    
    # Obtener la emoción con el puntaje más alto
    dominant_emotion = max(emotions.items(), key=lambda x: x[1])
    
    # Si todas las emociones tienen puntaje bajo, considerar neutral
    if dominant_emotion[1] <= 2:
        return "Neutral"
    return dominant_emotion[0]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No se proporcionó imagen'}), 400
    
    file = request.files['image']
    
    if file.filename == '':
        return jsonify({'error': 'No se seleccionó archivo'}), 400

    try:
        temp_path = 'temp_image.jpg'
        file.save(temp_path)
        
        client = vision.ImageAnnotatorClient()
        
        with open(temp_path, 'rb') as image_file:
            content = image_file.read()
        
        image = vision.Image(content=content)
        response = client.face_detection(image=image)
        faces = response.face_annotations

        results = []
        for face in faces:
            # Calcular porcentajes de cada emoción
            emotions_percentages = {
                'alegria': (get_likelihood_score(face.joy_likelihood) / 5) * 100,
                'tristeza': (get_likelihood_score(face.sorrow_likelihood) / 5) * 100,
                'enojo': (get_likelihood_score(face.anger_likelihood) / 5) * 100,
                'sorpresa': (get_likelihood_score(face.surprise_likelihood) / 5) * 100
            }

            face_data = {
                'confianza': round(face.detection_confidence * 100, 2),
                'sentimiento_predominante': get_dominant_emotion(face),
                'emociones': {
                    'alegria': round(emotions_percentages['alegria'], 2),
                    'tristeza': round(emotions_percentages['tristeza'], 2),
                    'enojo': round(emotions_percentages['enojo'], 2),
                    'sorpresa': round(emotions_percentages['sorpresa'], 2)
                },
                'rasgos_faciales': {
                    'ojos_abiertos': round((get_likelihood_score(face.under_exposed_likelihood) / 5) * 100, 2),
                    'boca_abierta': round((get_likelihood_score(face.blurred_likelihood) / 5) * 100, 2)
                }
            }
            results.append(face_data)
        
        os.remove(temp_path)
        
        return jsonify({'success': True, 'faces': results})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)