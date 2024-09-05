import streamlit as st

@st.cache_resource

def intro():
    import streamlit as st

    st.write("# Modelos predictivos para geminacion de plantas 👋")
    st.sidebar.success("Seleccionar un modelo")

    st.markdown(
        """
        Este es un trabajo hecho por el grupo plantas 🌱❤️

        Para utilizar el modelo haga click en la flecha a su izquierda 👈🏻

        Para ver más contenido de Bioclubs, pueden mirar nuestro 
        
    """
    )

def svm():
  import streamlit as st
  import numpy as np
  import joblib
  import pandas as pd
  #from sklearn.svm import SVC

  
  def modelo(var,m):
    #pred = ovr.predict(var)
    pred= m.predict(var)
    return pred
  

  #ovr = joblib.load("modelos/Regresion_logistica_modif.pkl") #Modificar aca la ruta para el modelo
  m = joblib.load("modelos/Regresion_logistica_modif.pkl")

  st.title('Modelo de Predicción') #Agregar titulo
  st.markdown("""Complete los datos indicados para estimar el tiempo en que tardará su planta en germinar""")# Agregar texto

  st.subheader('Subtitulo')


  lav = st.number_input('Tiempo en miutos dejado en lavandina', max_value=20 ,help="Como maximo 20 min.")
  esp = st.selectbox('Especie de la semilla',["Soja Blanca","Arveja","Zapallo"])
  porAga = st.selectbox('Porcentaje de agar', ["1.5%","1.35%"])
  med = st.selectbox('Tipo de medio', ["Normal","Suplementado"])
  
  if st.button("Calcular"):
    if(lav<12):
      lav="1"
    else:
      lav="2"

    if(esp=="Soja Blanca"):
      esp="1"
    elif(esp=="Arveja"):
      esp="0"
    else:
      esp="2"

    if(porAga=="1.5%"):
      porAga=0.015
    else:
      porAga=0.0135

    if(med=="Normal"):
      med="0"
    else:
      med="1"

    #variables={
    #  "especie_n": esp,
    #  "medio_n": med,
    #  "Minutos en Lavandina": lav,
    #  "porcentaje del Agar": porAga}
    
    #variables = pd.DataFrame([variables])

    variables = pd.DataFrame({
        "especie_n": esp,
        "medio_n": med,
        "Minutos en Lavandina": lav,
        "porcentaje del Agar": porAga}, index = [1])
    
    st.write(variables)

    pred = modelo(variables, m)
    
    st.write(pred)

    if pred == 1:
        st.write("Su planta germinará en menos de 3 días!")
    elif pred == 2:
        st.write("Su planta tardará entre 4 y 6 días en germinar")
    else:
        st.write("Su planta tardará 1 semana o más en germinar!")

  st.button("Reset", type="primary")

page_names_to_funcs = {
    "Inicio": intro,
    "Modelo": svm
}

st.set_page_config(
    page_title="Modelo para plantas",
    page_icon="🌱",
)
demo_name = st.sidebar.selectbox("", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
