
 import streamlit as st
 
 st.set_page_config(page_title="Evaluación de Riesgo - Diabetes", layout="centered")
 
+st.markdown(
+    """
+    <style>
+        .stApp {
+            background: linear-gradient(180deg, #f7fbff 0%, #edf6ff 100%);
+        }
+        h1, h2, h3 {
+            color: #0f4c81;
+        }
+        .stButton > button {
+            background-color: #0f4c81;
+            color: white;
+            border: 1px solid #0f4c81;
+            border-radius: 10px;
+            font-weight: 600;
+        }
+        .stButton > button:hover {
+            background-color: #1363a8;
+            border-color: #1363a8;
+            color: white;
+        }
+        [data-testid="stSlider"] {
+            padding: 0.2rem 0.5rem 0.6rem 0.5rem;
+            border-radius: 10px;
+            background: rgba(255, 255, 255, 0.65);
+            border: 1px solid #d9e8f8;
+        }
+    </style>
+    """,
+    unsafe_allow_html=True,
+)
+
 st.title("🧠 Evaluación de Factores de Riesgo")
 st.subheader("Modelo educativo - Diabetes Mellitus (Tipo 1 y 2)")
 
 st.write("Ingresa valores entre 0 y 1:")
 st.write("0 = Sin riesgo | 1 = Riesgo máximo")
 
 # Nombre
 nombre = st.text_input("Nombre del paciente (opcional)")
 
 # ==============================
 # FACTORES BIOLÓGICOS
 # ==============================
 st.header("Factores Biológicos")
 
 edad_risk = st.slider("Edad (>50 años)", 0.0, 1.0, 0.0)
 genetic_risk = st.slider("Predisposición genética (antecedentes familiares)", 0.0, 1.0, 0.0)
 base_metabolic = 0.10
 
 # ==============================
 # ESTILO DE VIDA
 # ==============================
 st.header("Estilo de Vida")
 
 dieta = st.slider("Dieta (alto en azúcar/grasas)", 0.0, 1.0, 0.0)
 actividad = st.slider("Actividad física (sedentarismo)", 0.0, 1.0, 0.0)
