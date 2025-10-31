import streamlit as st
from streamlit_drawable_canvas import st_canvas

# --- TABLERO PRINCIPAL ---
st.title("Tablero para dibujo")

with st.sidebar:
    st.subheader("Propiedades del Tablero")

    # Canvas dimensions (moved to the top)
    st.subheader("Dimensiones del Tablero")
    canvas_width = st.slider("Ancho del tablero", 300, 700, 500, 50)
    canvas_height = st.slider("Alto del tablero", 200, 600, 300, 50)

    # Drawing mode selector
    drawing_mode = st.selectbox(
        "Herramienta de Dibujo:",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
    )

    # Stroke width slider
    stroke_width = st.slider("Selecciona el ancho de línea", 1, 30, 15)

    # Stroke color picker
    stroke_color = st.color_picker("Color de trazo", "#FFFFFF")

    # Background color
    bg_color = st.color_picker("Color de fondo", "#000000")

# Create a canvas component with dynamic key
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=canvas_height,
    width=canvas_width,
    drawing_mode=drawing_mode,
    key=f"canvas_{canvas_width}_{canvas_height}",  # Dynamic key based on dimensions
)

# --- SEGUNDO TABLERO (Código de la imagen) ---
st.markdown("---")
st.header("Tablero adicional para dibujo")

with st.sidebar:
    st.subheader("Propiedades del Tablero Secundario")

    # Canvas dimensions (moved to the top)
    st.subheader("Dimensiones del Tablero Secundario")
    canvas_width_2 = st.slider("Ancho del tablero 2", 300, 700, 500, 50)
    canvas_height_2 = st.slider("Alto del tablero 2", 200, 600, 300, 50)

    # Drawing mode selector
    drawing_mode_2 = st.selectbox(
        "Herramienta de Dibujo 2:",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
    )

    # Stroke width slider
    stroke_width_2 = st.slider("Selecciona el ancho de línea (tablero 2)", 1, 30, 15)

    # Stroke color picker
    stroke_color_2 = st.color_picker("Color de trazo (tablero 2)", "#FFFFFF")

    # Background color
    bg_color_2 = st.color_picker("Color de fondo (tablero 2)", "#000000")

# Create a canvas component with dynamic key
canvas_result_2 = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",
    stroke_width=stroke_width_2,
    stroke_color=stroke_color_2,
    background_color=bg_color_2,
    height=canvas_height_2,
    width=canvas_width_2,
    drawing_mode=drawing_mode_2,
    key=f"canvas2_{canvas_width_2}_{canvas_height_2}",  # Dynamic key based on dimensions
)

