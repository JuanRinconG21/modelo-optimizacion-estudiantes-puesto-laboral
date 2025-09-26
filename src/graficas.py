# Importar librerías necesarias
import pandas as pd              # Para manipular  y analizar los datos
import matplotlib.pyplot as plt  # Para crear graficos basicos
import seaborn as sns            # Para una mejor visualizacion de los graficos

# Cargar y leer los datos del archivo CSV
df = pd.read_csv("college_student_placement_dataset_convert.csv")  

# Convertir las columnas de 0/1 a 'Si' y 'No' 
# para que se entiendan mejor en las gráficas
df['Placement'] = df['Placement'].map({0: 'No', 1: 'Sí'})
df['Internship_Experience'] = df['Internship_Experience'].map({0: 'No', 1: 'Sí'})  


# Configurar el estilos de los graficos
sns.set_theme(style="whitegrid")  


# Histograma de CGPA
# Le da un tamaño a la grafica
plt.figure(figsize=(6,4)) 
#La funcion histplot crea un histograma de los datos en CGPA
#El parametro bins=20 divide los resultados en 20 intervalos 
# y KDE=True añade la curva de densidad 
sns.histplot(df['CGPA'], bins=20, kde=True, color='skyblue')  
#Se le da un titulo a la grafica y a los ejes 
# y un tamaño de letra por medio de fontsize
plt.title('Distribución del CGPA', fontsize=14)
plt.xlabel('CGPA')
plt.ylabel('Cantidad de estudiantes')
# Muestra la grafica
plt.show()


# Gráfico de barras experiencia en prácticas
# Le da un tamaño a la grafica
plt.figure(figsize=(5,4))
# La funcion countplot crea un grafico de barras y 
# cuenta cuántos registros hay por cada similitud en la columna Internship_Experience
# El parametro x cual es la columna que se quiere graficar
# El parametro data dice de donde se sacan los datos
# El parametro palette define los colores que se van a usar
sns.countplot(x='Internship_Experience', data=df, palette='pastel') 
#Se le da un titulo a la grafica y a los ejes 
# y un tamaño de letra por medio de fontsize
plt.title('Distribución de experiencia en prácticas', fontsize=14)
plt.xlabel('Experiencia en prácticas')
plt.ylabel('Cantidad de estudiantes')
# Muestra la grafica
plt.show()


# Cantidad de estudiantes con un puesto laboral
# Le da un tamaño a la grafica
plt.figure(figsize=(5,4)) 
# La funcion countplot crea un grafico de barras y 
# cuenta cuántos registros hay por cada similitud en la columna Placement
# El parametro x cual es la columna que se quiere graficar
# El parametro data dice de donde se sacan los datos
# El parametro palette define los colores que se van a usar
sns.countplot(x='Placement', data=df, palette='pastel')   
#Se le da un titulo a la grafica y a los ejes 
# y un tamaño de letra por medio de fontsize
plt.title('Cantidad de estudiantes con un puesto laboral', fontsize=14)
plt.xlabel('Colocación laboral')
plt.ylabel('Cantidad de estudiantes')
# Muestra la grafica
plt.show()


# Dispersión CGPA contra Habilidades comunicativas 
# y colores por colocación laboral
# Le da un tamaño a la grafica
plt.figure(figsize=(6,4))
# La funcion scatterplot crea un grafico de dispersion
# El parametro x cual es la columna que se quiere graficar en el eje x
# El parametro y cual es la columna que se quiere graficar en el eje y
# El parametro data dice de donde se sacan los datos
# El parametro hue dice de donde se sacan los datos para colorear en datos similares
# El parametro palette define los colores que se van a usar
sns.scatterplot(
    x='CGPA',
    y='Communication_Skills',
    data=df,
    hue='Placement', 
    palette='coolwarm'
)
#Se le da un titulo a la grafica y a los ejes 
# y un tamaño de letra por medio de fontsize
plt.title('Relación entre CGPA y habilidades comunicativas', fontsize=14)
plt.xlabel('CGPA')
plt.ylabel('Habilidades comunicativas')
plt.legend(title='Colocación')
# Muestra la grafica
plt.show()