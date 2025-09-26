# Importar librerías necesarias
import pandas as pd #Para manipular los datos
import numpy as np #Para operaciones matematicas
from sklearn.linear_model import LogisticRegression #Para encontrar los patrones en los datos
from sklearn.preprocessing import StandardScaler #Para estandarizar los datos y que estén en la misma escala
import pulp #Para poder encontrar la solución óptima

# Cargar los datos del archivo CSV
data = pd.read_csv('college_student_placement_dataset_convert.csv')  

#Establecer limites para considerar un atributo como alto
cgpa_limite = 8.0 # CGPA minimo para considerarse dentro del rango 
comms_limite = 7.0 # Puntuacion minima en habilidades comunicativas para considerarse dentro del rango
projects_limite = 3  # Numero mínimo de proyectos que se puede considerar alto
extracurricular_limite = 7  # Puntuacion minima en actividades extracurriculares para considerarse dentro del rango

# Por medio de esto creamos nuevas columnas para cada uno de los atributos 
# que nos dicen si el atributo es alto 1 o no 0
data['CGPA_Alto'] = (data['CGPA'] >= cgpa_limite).astype(int)
data['Habilidades_Comunicativas_Altas'] = (data['Communication_Skills'] >= cgpa_limite).astype(int)
data['Proyectos_Completados_Altos'] = (data['Projects_Completed'] >= projects_limite).astype(int)
data['Actividades_Extracurriculares_Altas'] = (data['Extra_Curricular_Score'] >= extracurricular_limite).astype(int)

# Definimos las variables sobre las cuales vamos a realizar la comparacion
#para encontrar la mejor combinacion de atributos
# X son las cualidades de los estudiantes 1 si la tienen y 0 si no
# Y es si consiguieron un puesto laboral 1 si y 0 no
X = data[['CGPA_Alto', 'Internship_Experience', 'Habilidades_Comunicativas_Altas', 'Proyectos_Completados_Altos', 'Actividades_Extracurriculares_Altas']]
y = data['Placement']

# Por medio de esto estandarizamos los datos 
# para que esten en la misma sintonia y se puedan comparar
scaler = StandardScaler()
X_escala = scaler.fit_transform(X)

# Por medio de esta funcion se realiza la regresion logistica o la importancia de cada factor
# y se obtienen los resultados
modelo = LogisticRegression()
modelo.fit(X_escala, y)
coeficientes = modelo.coef_[0]

# Por medio de esto se convierten los resultados anteriores a porcentajes
# para saber que tanto importancia tienen para la obtencion de un puesto laboral
# y se asignan los resultados a cada variable
coeficientesNormalizados = np.abs(coeficientes) / np.sum(np.abs(coeficientes))
c1, c2, c3, c4, c5 = coeficientesNormalizados

# Por medio de de la libreria pulp se crea el modelo de optimizacion
# se le da un nombre y se define que es de maximizar
prob = pulp.LpProblem("Maximize_Placement_Probability", pulp.LpMaximize)

# Definimos las variables de decision 
# Como 0 y 1 para decir si el atributo es importante o no
x1 = pulp.LpVariable('CGPA_Alto', cat='Binary')
x2 = pulp.LpVariable('Experiencia_Practicas', cat='Binary')
x3 = pulp.LpVariable('Habilidades_Comunicativas_Altas', cat='Binary')
x4 = pulp.LpVariable('Proyectos_Completados_Altos', cat='Binary')
x5 = pulp.LpVariable('Actividades_Extracurriculares_Altas', cat='Binary')

# Se le indica al problema cual es la funcion que queremos maximizar
# que en este caso es la probabilidad de obtener un puesto laboral
prob += c1*x1 + c2*x2 + c3*x3 + c4*x4 + c5*x5, "Puntuacion_Empleabilidad"

# Se añaden todas las restricciones para que el modelo sea realista
# Carga académica menor o igual a 3: No más de 3 atributos altos
prob += x1 + x2 + x3 + x4 + x5 <= 3, "Restriccion_Recursos"
# Practicas respecto a CGPA: para realizar practicas requiere un CGPA alto
prob += x2 <= x1, "Experiencia_requiere_CGPA_Alto"
# Restricción mínima respecto a CGPA o Puntuación de Proyectos: Que el CGPA o proyectos sean altos
prob += x1 + x4 >= 1, "Minimo_Academico"

# Por medio de la funcion solve se resuelve el problema
prob.solve()

# Imprimimos el estado de la solucion es decir si pudo encontrar una solucion optima
print("Estado de la solucion:", pulp.LpStatus[prob.status])
# Se imprimen los valores que el modelo encontro para cada variable 1 si es importante 0 si no
print("\nHabilidades para maximizar la obtencion de un puesto laboral:")
for variable in prob.variables():
    print(f"{variable.name} = {variable.varValue}")

# Se imprime el valor de la funcion objetivo 
# es decir la probabilidad de obtener un puesto laboral en porcentaje
print(f"\nZ =: {pulp.value(prob.objective):.4f}")
print(f"Porcentaje de obtencion de un puesto laboral: {pulp.value(prob.objective) * 100:.2f}%")

# Interpretación de los resultados
print("\nRecomendacion para obtener un puesto laboral")
if x1.varValue == 1:
    print("- Debe mantener un CGPA >= 8.0.")
if x2.varValue == 1:
    print("- Debes buscar experiencia en practicas profesionales.")
if x3.varValue == 1:
    print("- Debe desarrollar habilidades comunicativas >= 7.0.")
if x4.varValue == 1:
    print("- Debes completar >= 3 proyectos academicos.")
if x5.varValue == 1:
    print("- Debes participar en actividades extracurriculares y dar una puntuacion >= 7.")

