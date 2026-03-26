import os
import glob
import html
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Dashboard 3D - Deslizamientos", layout="wide")

# -------------------------------------------------------
# CONFIG
# -------------------------------------------------------
TAB_FILES = {
    "Desplazamiento 2011–2023": [
        "superficie_3d_desplazamiento.html",
        "superficie_3d_desplazamiento (3).html",
    ],
    "Ladera Occidental – Riesgo": [
        "modelo_3d_ladera_riesgo.html",
    ],
    "Modelo por Barrio": [
        "modelo_terreno_3d_filtrado_por_barrio_con_label_elevado.html",
    ],
}

TAB_HEIGHT = 820

# -------------------------------------------------------
# HELPERS
# -------------------------------------------------------
def find_html(candidates):
    for name in candidates:
        if os.path.exists(name):
            return name

    html_files = glob.glob("*.html")
    candidate_bases = [c.replace(".html", "").lower() for c in candidates]

    for f in html_files:
        fl = f.lower()
        for base in candidate_bases:
            if base in fl:
                return f
    return None

def load_html(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def render_html_file(path, height=820):
    if not path:
        st.error("No se encontró el archivo HTML correspondiente.")
        return

    raw_html = load_html(path)
    escaped_html = html.escape(raw_html, quote=True)

    iframe = f"""
    <iframe
        srcdoc="{escaped_html}"
        width="100%"
        height="{height}"
        style="border:none; overflow:hidden;"
        sandbox="allow-scripts allow-same-origin allow-downloads allow-popups"
    ></iframe>
    """
    components.html(iframe, height=height, scrolling=False)

# -------------------------------------------------------
# UI
# -------------------------------------------------------
st.title("Ladera occidental – Análisis de Deslizamientos - Localidad Suroccidente")

tab_names = list(TAB_FILES.keys())
tabs = st.tabs(tab_names)

for tab, tab_name in zip(tabs, tab_names):
    with tab:
        file_path = find_html(TAB_FILES[tab_name])
        st.subheader(tab_name)
        render_html_file(file_path, height=TAB_HEIGHT)

with st.expander("Ver archivos detectados"):
    st.write(sorted(os.listdir(".")))
