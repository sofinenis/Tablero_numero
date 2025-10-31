import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Función para predecir el dígito
def predictDigit(image):
    model = tf.keras.models.load_model("model/handwritten.h5")
    image = ImageOps.grayscale(image)
    img = image.resize((28, 28))
    img = np.array(img, dtype='float32')
    img = img / 255
    plt.imshow(img, cmap='gray')
    plt.axis('off')
    plt.show()
    img = img.reshape((1, 28, 28, 1))
    pred = model.predict(img)
    result = np.argmax(pred[0])
    return result

# Configuración de la app
st.set_page_config(page_title='Reconocimiento de Dígitos escritos a mano', layout='wide')
st.title('🖊️ Reconocimiento de Dígitos escritos a mano')
st.subheader("Dibuja el dígito en el panel y presiona **'Predecir'**")

# --- Sidebar para propiedades del tablero ---
with st.sidebar:
    st.subheader("🧩 Propiedades del Tablero")

    # Dimensiones del canvas
    st.write("**Dimensiones del Tablero**")
    canvas_width = st.slider("Ancho del tablero", 300, 700, 400, 50)
    canvas_height = st.slider("Alto del tablero", 200, 600, 300, 50)

    # Herramienta de dibujo
    drawing_mode = st.selectbox(
        "Herramienta de dibujo",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point")
    )

    # Ancho del trazo
    stroke_width = st.slider("Ancho de línea", 1, 30, 15)

    # Color del trazo y fondo
    stroke_color = st.color_picker("Color del trazo", "#FFFFFF")
    bg_color = st.color_picker("Color de fondo", "#000000")

    st.markdown("---")
    st.info("💡 Consejo: Usa fondo negro y trazo blanco para mejores resultados.")

# --- Canvas principal ---
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=canvas_height,
    width=canvas_width,
    drawing_mode=drawing_mode,
    key=f"canvas_{canvas_width}_{canvas_height}",
)

# --- Botón para predecir ---
if st.button('🔍 Predecir'):
    if canvas_result.image_data is not None:
        input_numpy_array = np.array(canvas_result.image_data)
        input_image = Image.fromarray(input_numpy_array.astype('uint8'), 'RGBA')
        input_image.save('prediction/img.png')
        img = Image.open("prediction/img.png")
        res = predictDigit(img)
        st.success(f' El dígito predicho es: **{res}**')
    else:
        st.warning('Por favor dibuja en el tablero antes de predecir.')


st.sidebar.markdown("---")
st.sidebar.title("ℹ️ Acerca de:")
st.sidebar.write("""
Esta aplicación evalúa la capacidad de una red neuronal artificial
para reconocer dígitos escritos a mano.

Basado en el desarrollo de Vinay Uniyal, 
adaptado con una interfaz personalizada de Streamlit.
""")

