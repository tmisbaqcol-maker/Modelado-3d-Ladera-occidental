import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

st.title("DASHBOARD 3D – ANÁLISIS DE DESLIZAMIENTOS")

# --------------------------------------------------
# TABS
# --------------------------------------------------
tab1, tab2, tab3 = st.tabs([
    "Desplazamiento 2011–2023",
    "Ladera Occidental – Riesgo",
    "Modelo por Barrio"
])

# --------------------------------------------------
# FUNCION PARA CARGAR HTML
# --------------------------------------------------
def load_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

# --------------------------------------------------
# TAB 1
# --------------------------------------------------
with tab1:
    st.subheader("Superficie 3D de Desplazamiento")
    html = load_html("superficie_3d_desplazamiento.html")
    components.html(html, height=700, scrolling=True)

# --------------------------------------------------
# TAB 2
# --------------------------------------------------
with tab2:
    st.subheader("Modelo de Ladera Occidental con Riesgo")
    html = load_html("modelo_3d_ladera_riesgo.html")
    components.html(html, height=700, scrolling=True)

# --------------------------------------------------
# TAB 3
# --------------------------------------------------
with tab3:
    st.subheader("Modelo 3D Filtrado por Barrio")
    html = load_html("modelo_terreno_3d_filtrado_por_barrio_con_label_elevado.html")
    components.html(html, height=700, scrolling=True)
