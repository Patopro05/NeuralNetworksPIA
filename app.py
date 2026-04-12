import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

st.set_page_config(page_title="Detector de Alzheimer", page_icon="🧠", layout="centered")

st.title("Clasificador de Resonancias Magnéticas (MRI)")
st.write("""
Esta herramienta, desarrollada para el análisis de Alzheimer, utiliza una Red Neuronal Convolucional (CNN) 
para clasificar imágenes de resonancia magnética en cuatro etapas clínicas.
""")

@st.cache_resource
def load_model():
    return tf.keras.models.load_model('modelo_alzheimer.h5')

modelo = load_model()

clases = ['Demencia Leve (Mild Demented)', 
          'Demencia Moderada (Moderate Demented)', 
          'Sano (Non Demented)', 
          'Demencia Muy Leve (Very Mild Demented)']

st.markdown("---")
uploaded_file = st.file_uploader("Sube una imagen de MRI (Formato JPG o PNG)", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Imagen de Resonancia Magnética cargada', use_container_width=True)
    
    st.write("Analizando la imagen...")
        
    img_procesada = image.convert('RGB')
    img_procesada = img_procesada.resize((128, 128))
    
    img_array = np.array(img_procesada) / 255.0
    

    img_array = np.expand_dims(img_array, axis=0)
    
    
    prediccion = modelo.predict(img_array)
    indice_clase_ganadora = np.argmax(prediccion[0])
    confianza = np.max(prediccion[0]) * 100
    
    
    st.markdown("### Resultado del Análisis:")
    
    
    if indice_clase_ganadora == 2: 
        st.success(f"**Diagnóstico sugerido:** {clases[indice_clase_ganadora]}")
    else:
        st.error(f"**Diagnóstico sugerido:** {clases[indice_clase_ganadora]}")
        
    st.info(f"**Nivel de Confianza de la Red:** {confianza:.2f}%")