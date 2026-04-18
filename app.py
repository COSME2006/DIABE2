import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Evaluación de Riesgo", layout="centered")

st.title("🧠 Evaluación de Factores de Riesgo")
st.subheader("Modelo educativo - Diabetes Mellitus")

st.info("Valores entre 0 (sin riesgo) y 1 (riesgo máximo)")

nombre = st.text_input("Nombre del paciente (opcional)")

# =============================
# FACTORES BIOLÓGICOS (5)
# =============================
st.header("🧬 Factores Biológicos")

col1, col2 = st.columns(2)

with col1:
    edad = st.slider("Edad (>50 años)", 0.0, 1.0, 0.0)
    genetica = st.slider("Predisposición genética", 0.0, 1.0, 0.0)
    antecedentes = st.slider("Antecedentes personales (prediabetes, etc.)", 0.0, 1.0, 0.0)

with col2:
    sexo = st.slider("Sexo biológico (riesgo relativo)", 0.0, 1.0, 0.0)
    base = 0.10
    st.write("Función metabólica base: constante")

# =============================
# ESTILO DE VIDA (10)
# =============================
st.header("🏃 Estilo de Vida")

col3, col4 = st.columns(2)

with col3:
    dieta = st.slider("Dieta", 0.0, 1.0, 0.0)
    actividad = st.slider("Actividad física", 0.0, 1.0, 0.0)
    adherencia = st.slider("Adherencia terapéutica", 0.0, 1.0, 0.0)
    estres = st.slider("Estrés", 0.0, 1.0, 0.0)
    imc = st.slider("IMC", 0.0, 1.0, 0.0)

with col4:
    alcohol = st.slider("Alcohol", 0.0, 1.0, 0.0)
    tabaco = st.slider("Tabaco", 0.0, 1.0, 0.0)
    presion = st.slider("Presión arterial", 0.0, 1.0, 0.0)
    sueno = st.slider("Calidad del sueño", 0.0, 1.0, 0.0)
    azucar = st.slider("Consumo de azúcar", 0.0, 1.0, 0.0)

# =============================
# BOTÓN
# =============================
if st.button("🔍 Calcular análisis"):

    bio = {
        "Genética": genetica,
        "Edad": edad,
        "Antecedentes": antecedentes,
        "Sexo": sexo,
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
        "Presión": presion,
        "Sueño": sueno,
        "Azúcar": azucar
    }

    total_bio = sum(bio.values())
    total_vida = sum(vida.values())
    total = total_bio + total_vida

    pct_bio = (total_bio / total) * 100
    pct_vida = (total_vida / total) * 100

    st.success("Resultados obtenidos")

    if nombre:
        st.write(f"👤 Paciente: {nombre}")

    col_res1, col_res2 = st.columns(2)
    col_res1.metric("🧬 Biológicos", f"{pct_bio:.1f}%")
    col_res2.metric("🏃 Estilo de vida", f"{pct_vida:.1f}%")

    # =============================
    # GRÁFICA GENERAL
    # =============================
    st.subheader("📊 Distribución del riesgo")

    fig, ax = plt.subplots()
    categorias = ["Biológicos", "Estilo de Vida"]
    valores = [pct_bio, pct_vida]

    ax.barh(categorias, valores)
    ax.set_xlim(0, 100)

    for i, v in enumerate(valores):
        ax.text(v + 1, i, f"{v:.1f}%", va='center')

    st.pyplot(fig)

    # =============================
    # GRÁFICA DETALLADA (15)
    # =============================
    st.subheader("📈 Desglose completo de factores")

    todos = {**bio, **vida}

    fig2, ax2 = plt.subplots()
    ax2.barh(list(todos.keys()), list(todos.values()))
    ax2.set_xlim(0, 1)

    for i, v in enumerate(todos.values()):
        ax2.text(v + 0.02, i, f"{v:.2f}", va='center')

    st.pyplot(fig2)

    # =============================
    # INTERPRETACIÓN
    # =============================
    if pct_vida > 60:
        nivel = "Alto"
        st.error("🔴 Riesgo alto")
    elif pct_vida > 40:
        nivel = "Moderado"
        st.warning("🟠 Riesgo moderado")
    else:
        nivel = "Bajo"
        st.success("🟢 Riesgo bajo")

    # =============================
    # INFORME
    # =============================
    st.subheader("📝 Informe de enfermería")

    informe = f"""
    Evaluación de riesgo en paciente {nombre if nombre else "no especificado"}.

    Factores biológicos: {pct_bio:.1f}%
    Factores de estilo de vida: {pct_vida:.1f}%

    Nivel de riesgo: {nivel}

    Se recomienda intervención en factores modificables, educación en salud,
    promoción de hábitos saludables y seguimiento clínico.
    """

    st.write(informe)
    # =============================
    # ÁRBOL COMPARATIVO
    # =============================
st.subheader("🌳 Árbol comparativo de determinantes")

st.markdown(f"""
### 🔎 Estructura del riesgo

**RIESGO TOTAL (100%)**

├── 🧬 **Factores Biológicos ({pct_bio:.1f}%)**
│   ├── Genética: {genetica:.2f}
│   ├── Edad: {edad:.2f}
│   ├── Antecedentes: {antecedentes:.2f}
│   ├── Sexo: {sexo:.2f}
│   └── Función Base: {base:.2f}

└── 🏃 **Estilo de Vida ({pct_vida:.1f}%)**
    ├── Dieta: {dieta:.2f}
    ├── Actividad Física: {actividad:.2f}
    ├── Adherencia: {adherencia:.2f}
    ├── Estrés: {estres:.2f}
    ├── IMC: {imc:.2f}
    ├── Alcohol: {alcohol:.2f}
    ├── Tabaco: {tabaco:.2f}
    ├── Presión Arterial: {presion:.2f}
    ├── Sueño: {sueno:.2f}
    └── Azúcar: {azucar:.2f}
""")
