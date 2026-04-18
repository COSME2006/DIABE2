import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Evaluación de Riesgo", layout="centered")

# =============================
# ESTILO
# =============================
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
h1, h2, h3 {
    color: #1f4e79;
}
.stButton>button {
    background-color: #1f77b4;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# =============================
# TÍTULO
# =============================
st.title("🧠 Evaluación de Factores de Riesgo")
st.subheader("Modelo educativo - Diabetes Mellitus")

st.info("Valores entre 0 (sin riesgo) y 1 (riesgo máximo)")

nombre = st.text_input("Nombre del paciente (opcional)")

# =============================
# FACTORES BIOLÓGICOS
# =============================
st.header("🧬 Factores Biológicos")

col1, col2 = st.columns(2)

with col1:
    edad = st.slider("Edad (>50 años)", 0.0, 1.0, 0.0)
    genetica = st.slider("Predisposición genética", 0.0, 1.0, 0.0)

with col2:
    base = 0.10
    st.write("Función metabólica base: constante")

# =============================
# ESTILO DE VIDA
# =============================
st.header("🏃 Estilo de Vida")

col3, col4 = st.columns(2)

with col3:
    dieta = st.slider("Dieta", 0.0, 1.0, 0.0)
    actividad = st.slider("Actividad física", 0.0, 1.0, 0.0)
    adherencia = st.slider("Adherencia terapéutica", 0.0, 1.0, 0.0)
    estres = st.slider("Estrés", 0.0, 1.0, 0.0)

with col4:
    imc = st.slider("IMC", 0.0, 1.0, 0.0)
    alcohol = st.slider("Alcohol", 0.0, 1.0, 0.0)
    tabaco = st.slider("Tabaco", 0.0, 1.0, 0.0)
    presion = st.slider("Presión arterial", 0.0, 1.0, 0.0)

# =============================
# BOTÓN
# =============================
if st.button("🔍 Calcular análisis"):

    bio = {
        "Genética": genetica,
        "Edad": edad,
        "Base": base
    }

    vida = {
        "Dieta": dieta,
        "Actividad": actividad,
        "Adherencia": adherencia,
        "Estrés": estres,
        "IMC": imc,
        "Alcohol": alcohol,
        "Tabaco": tabaco,
        "Presión": presion
    }

    total_bio = sum(bio.values())
    total_vida = sum(vida.values())
    total = total_bio + total_vida

    pct_bio = (total_bio / total) * 100
    pct_vida = (total_vida / total) * 100

    # =============================
    # RESULTADOS
    # =============================
    st.success("Resultados obtenidos")

    if nombre:
        st.write(f"👤 Paciente: {nombre}")

    col_res1, col_res2 = st.columns(2)

    col_res1.metric("🧬 Biológicos", f"{pct_bio:.1f}%")
    col_res2.metric("🏃 Estilo de vida", f"{pct_vida:.1f}%")

    # =============================
    # GRÁFICA
    # =============================
    st.subheader("📊 Distribución del riesgo")

    fig, ax = plt.subplots()

    categorias = ["Biológicos", "Estilo de Vida"]
    valores = [pct_bio, pct_vida]

    ax.barh(categorias, valores)
    ax.set_xlim(0, 100)
    ax.set_xlabel("Porcentaje (%)")
    ax.set_title("Comparación de factores de riesgo")

    for i, v in enumerate(valores):
        ax.text(v + 1, i, f"{v:.1f}%", va='center')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    st.pyplot(fig)

    # =============================
    # INTERPRETACIÓN
    # =============================
    st.subheader("Interpretación")

    if pct_vida > 60:
        nivel = "Alto"
        st.error("🔴 Riesgo alto por estilo de vida")
    elif pct_vida > 40:
        nivel = "Moderado"
        st.warning("🟠 Riesgo moderado")
    else:
        nivel = "Bajo"
        st.success("🟢 Riesgo bajo")

    st.info("Este modelo es educativo y no sustituye diagnóstico clínico.")

    # =============================
    # INFORME DE ENFERMERÍA
    # =============================
    st.subheader("📝 Informe automático de enfermería")

    informe = f"""
    **Evaluación de Riesgo para Diabetes Mellitus**

    Paciente: {nombre if nombre else "No especificado"}

    Se realizó una valoración de factores de riesgo, clasificándolos en biológicos y de estilo de vida.

    Los resultados evidencian un **{pct_bio:.1f}% de influencia de factores biológicos** y un **{pct_vida:.1f}% de factores relacionados con el estilo de vida**.

    Se identifica un nivel de riesgo **{nivel}**, con predominio de factores {'modificables' if pct_vida > pct_bio else 'no modificables'}.

    Desde el enfoque de enfermería, se recomienda:

    - Fomentar hábitos alimenticios saludables
    - Promover actividad física regular
    - Mejorar adherencia al tratamiento
    - Implementar estrategias de manejo del estrés
    - Realizar controles médicos periódicos

    Este análisis tiene carácter educativo y preventivo, orientado a la promoción de la salud y reducción de factores de riesgo.
    """

    st.write(informe)
