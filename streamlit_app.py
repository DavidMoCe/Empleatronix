import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.title("Empleatronix")
st.write("Todos los datos sobre los empleados en una aplicación.")

# Cargamos el csv con los datos
df = pd.read_csv("employees.csv")

# Mostrar el DataFrame
st.dataframe(df, use_container_width=True)

# Línea divisoria
st.divider()



# poner en columnas los tres selectores para que salgan uno al lado del otro
col1, col2, col3 = st.columns(3)
with col1:
   # Personalización del color
    color = st.color_picker("Elige un color para las barras", "#3475B3") 
with col2:
    # Botones para mostrar y ocultar el nombre y el saldo
    mostrar_nombre = st.toggle("Mostrar el nombre", value=True)
with col3:
    mostrar_sueldo = st.toggle("Mostrar sueldo en la barra", value=False)


# Crear el gráfico de barras con Plotly
fig = go.Figure()

# Añadir las barras con color
fig.add_trace(go.Bar(
    y=df['full name'],
    x=df['salary'],
    orientation = 'h',
    marker_color=color,
    text=[f"{salary}€" for salary in df['salary']] if mostrar_sueldo else [],
    textposition='outside'
))

# Configurar el diseño del gráfico
fig.update_layout(
    title="",
    xaxis_title="",
    yaxis_title="",
    showlegend=False,
    yaxis=dict(tickvals=[] if not mostrar_nombre else None),
    margin=dict(l=100, r=50, t=50, b=150),
)

# Mostrar el gráfico
st.plotly_chart(fig, use_container_width=True, config={'staticPlot': True,})

st.write("© David Moreno Cerezo - CPIFP Alan Turing")