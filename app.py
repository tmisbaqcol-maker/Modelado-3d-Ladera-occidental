import os
import glob
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")
st.title("DASHBOARD 3D – ANÁLISIS DE DESLIZAMIENTOS")

def find_html(preferred_names):
    for name in preferred_names:
        if os.path.exists(name):
            return name

    html_files = glob.glob("*.html")
    for name in preferred_names:
        base = name.replace(".html", "").lower()
        for f in html_files:
            if base in f.lower():
                return f
    return None

def load_html(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

tab1, tab2, tab3 = st.tabs([
    "Desplazamiento 2011–2023",
    "Ladera Occidental – Riesgo",
    "Modelo por Barrio"
])

file_tab1 = find_html([
    "superficie_3d_desplazamiento.html",
    "superficie_3d_desplazamiento (3).html"
])

file_tab2 = find_html([
    "modelo_3d_ladera_riesgo.html"
])

file_tab3 = find_html([
    "modelo_terreno_3d_filtrado_por_barrio_con_label_elevado.html"
])

with tab1:
    st.subheader("Superficie 3D de Desplazamiento")
    if file_tab1:
        components.html(load_html(file_tab1), height=720, scrolling=True)
    else:
        st.error("No se encontró el archivo HTML de la pestaña 1.")

with tab2:
    st.subheader("Modelo de Ladera Occidental con Riesgo")
    if file_tab2:
        components.html(load_html(file_tab2), height=720, scrolling=True)
    else:
        st.error("No se encontró el archivo HTML de la pestaña 2.")

with tab3:
    st.subheader("Modelo 3D Filtrado por Barrio")
    if file_tab3:
        components.html(load_html(file_tab3), height=720, scrolling=True)
    else:
        st.error("No se encontró el archivo HTML de la pestaña 3.")

with st.expander("Ver archivos detectados en el repositorio"):
    st.write(sorted(os.listdir(".")))
