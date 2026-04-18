import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Evaluación de Riesgo",
    layout="centered"
)

# =============================
# ESTILO PERSONALIZADO
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
# COLUMNAS
# =============================
col1, col2 = st.columns(2)

# =============================
# FACTORES BIOLÓGICOS
# =============================
with col1:
    st.header("🧬 Biológicos")
    edad = st.slider("Edad (>50 años)", 0.0, 1.0, 0.0)
    genetica = st.slider("Genética", 0.0, 1.0, 0.0)

# =============================
# ESTILO DE VIDA
# =============================
with col2:
    st.header("🏃 Estilo de Vida")
    dieta = st.slider("Dieta", 0.0, 1.0, 0.0)
    actividad = st.slider("Actividad física", 0.0, 1.0, 0.0)

# =============================
# MÁS FACTORES
# =============================
st.header("⚙️ Factores adicionales")

col3, col4 = st.columns(2)

with col3:
    adherencia = st.slider("Adherencia terapéutica", 0.0, 1.0, 0.0)
    estres = st.slider("Estrés", 0.0, 1.0, 0.0)
    imc = st.slider("IMC", 0.0, 1.0, 0.0)

with col4:
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
        "Base": 0.10
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
# GRÁFICA PROFESIONAL (BARRAS)
# =============================

st.subheader("📊 Distribución del riesgo")

fig, ax = plt.subplots()

categorias = ["Biológicos", "Estilo de Vida"]
valores = [pct_bio, pct_vida]

bars = ax.barh(categorias, valores)

# Estética limpia
ax.set_xlim(0, 100)
ax.set_xlabel("Porcentaje (%)")
ax.set_title("Comparación de factores de riesgo")

# Mostrar valores en la barra
for i, v in enumerate(valores):
    ax.text(v + 1, i, f"{v:.1f}%", va='center')

# Quitar bordes innecesarios
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

st.pyplot(fig)

    # =============================
    # NIVEL DE RIESGO
    # =============================
    st.subheader("Interpretación clínica")

    if pct_vida > 60:
        st.error("🔴 Riesgo alto por estilo de vida")
    elif pct_vida > 40:
        st.warning("🟠 Riesgo moderado")
    else:
        st.success("🟢 Riesgo bajo")

    st.info("Modelo educativo. No reemplaza diagnóstico médico.")
