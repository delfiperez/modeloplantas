import streamlit as st

@st.cache_resource

def intro():
    import streamlit as st

    st.write("# Desarrollo de un Modelo para Predecir el Tiempo de Germinación")
    st.sidebar.success("Seleccionar un modelo")

    st.markdown(
        """
        ### ¿Cuánto tardará una semilla en germinar?

        A través de la realización de técnicas como la micropropagación, se observó que la germinación es un proceso 
        influenciado por multiples factores. Para la construcción de este modelo, se utilizaron 4 variables explicativas
        que resultaron ser significativas:
        - Especie
        - Tiempo de esterilización de la semilla (en lavandina, calculado en minutos)
        - Porcentaje de Agar del medio de cultivo 
        - Tipo de medio de cultivo (Suplementado si/no)

        El objetivo de este modelo es predecir el tiempo de germinación, en función de las condiciones específicas de tratamiento 
        y cultivo, utilizando para ello un clasificador. 

        Los datos recolectados para la realización del modelo se obtuvieron de los laboratorios llevados a cabo por el grupo de plantas. Además, para entrenar el modelo, se sometió a los 
        mismos a una preparación, que implicó la limpieza y normalización de estos, así como la conversión de variables 
        categóricas, como la especie y el tipo de medio, a formatos adecuados para el análisis.

        Actualmente, se sabe que muchas áreas se benefician enormemente del poder predictivo y analítico de la IA. A través de este
        trabajo se pretende hacer una demostración de ello y de su aplicación en las ciencias biológicas.

        ❤️🌱 Este es un trabajo hecho por el grupo de bioinformática, plantas 🌱❤️

        Para utilizar el modelo **haga click en la flecha a su izquierda 👈** e ingrese a la sección **Modelo**

        ### ¿Querés saber más de nosotros?
        Para ver más contenido de Bioclubs:
        
        - Visitá nuestro Instagram [bioclubs.uade](https://www.instagram.com/bioclubs.uade/)
        - Revisá nuestro Tik Tok [biotokers](https://www.tiktok.com/@biotokers)
        
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
  m = joblib.load("modelos/SVM.pkl")

  st.title('¿Cuánto tardará mi semilla en germinar?') #Agregar titulo
  st.markdown("""Complete los datos indicados para estimar el tiempo de germinación de su semilla""")# Agregar texto

  lav = st.number_input('Tiempo de desinfección en lavandina (en minutos)', min_value = 0, max_value=20 ,help="Como maximo 20 min.")
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
      porAga=0.0150
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
        "Porcetaje del Agar": porAga}, index = [1])

   # st.write(variables.dtypes)
   # st.write(variables)

    pred = modelo(variables, m)
    
    #st.write(pred)

    if pred == "1":
        st.write("Su planta germinará en menos de 3 días! 💚")
    elif pred == "2":
        st.write("Su planta tardará entre 4 y 6 días en germinar 🩵")
    else:
        st.write("Su planta tardará 1 semana o más en germinar 💙")

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
