document.getElementById('uploadForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const imageInput = document.getElementById('imageInput');
    const preview = document.getElementById('preview');
    const loading = document.getElementById('loading');
    const results = document.getElementById('results');
    
    if (!imageInput.files[0]) {
        alert('Por favor selecciona una imagen');
        return;
    }

    // Mostrar vista previa
    const reader = new FileReader();
    reader.onload = function(e) {
        preview.src = e.target.result;
        preview.style.display = 'block';
    }
    reader.readAsDataURL(imageInput.files[0]);

    // Preparar datos para enviar
    const formData = new FormData();
    formData.append('image', imageInput.files[0]);

    // Mostrar loading
    loading.style.display = 'block';
    results.innerHTML = '';

    try {
        const response = await fetch('/analyze', {
            method: 'POST',
            body: formData
        });
        
        const data = await response.json();
        
        if (data.error) {
            results.innerHTML = `<p class="error">Error: ${data.error}</p>`;
            return;
        }

        // Mostrar resultados
        let resultsHTML = '<h2>Análisis Emocional:</h2>';
        if (data.faces.length === 0) {
            resultsHTML += '<p>No se detectaron rostros en la imagen.</p>';
        } else {
            data.faces.forEach((face, index) => {
                resultsHTML += `
                    <div class="face-analysis">
                        <h3>Rostro ${index + 1}</h3>
                        <div class="emotion-summary">
                            <h4>Sentimiento Predominante: 
                                <span class="emotion-highlight">${face.sentimiento_predominante}</span>
                            </h4>
                            <p>Confianza de detección: ${face.confianza}%</p>
                        </div>
                        
                        <div class="emotion-details">
                            <h4>Análisis Detallado de Emociones:</h4>
                            <div class="emotion-bars">
                                <div class="emotion-bar">
                                    <span>Alegría:</span>
                                    <div class="bar-container">
                                        <div class="bar" style="width: ${face.emociones.alegria}%"></div>
                                        <span>${face.emociones.alegria}%</span>
                                    </div>
                                </div>
                                <div class="emotion-bar">
                                    <span>Tristeza:</span>
                                    <div class="bar-container">
                                        <div class="bar" style="width: ${face.emociones.tristeza}%"></div>
                                        <span>${face.emociones.tristeza}%</span>
                                    </div>
                                </div>
                                <div class="emotion-bar">
                                    <span>Enojo:</span>
                                    <div class="bar-container">
                                        <div class="bar" style="width: ${face.emociones.enojo}%"></div>
                                        <span>${face.emociones.enojo}%</span>
                                    </div>
                                </div>
                                <div class="emotion-bar">
                                    <span>Sorpresa:</span>
                                    <div class="bar-container">
                                        <div class="bar" style="width: ${face.emociones.sorpresa}%"></div>
                                        <span>${face.emociones.sorpresa}%</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                `;
            });
        }
        results.innerHTML = resultsHTML;

    } catch (error) {
        results.innerHTML = `<p class="error">Error en el procesamiento: ${error.message}</p>`;
    } finally {
        loading.style.display = 'none';
    }
});