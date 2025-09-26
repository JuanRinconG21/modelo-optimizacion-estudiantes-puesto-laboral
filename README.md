# Modelo de optimizacion para que los estudiantes puedan obtener un puesto laboral📊

## Descripción del Proyecto

Este proyecto analiza los factores que influyen en la colocación laboral de estudiantes universitarios utilizando técnicas de análisis de datos, visualización y optimización matemática. Se desarrolló un modelo de regresión logística para identificar la importancia de cada factor y un modelo de programación lineal para encontrar la combinación óptima de habilidades que maximice las probabilidades de obtener empleo.

## Dataset 📈

**Fuente:** [College Student Placement Factors Dataset](https://www.kaggle.com/datasets/sahilislam007/college-student-placement-factors-dataset) - Kaggle

### Variables del Dataset:

- **CGPA**: Promedio de calificaciones acumulativo
- **Internship_Experience**: Experiencia en prácticas profesionales (0/1)
- **Communication_Skills**: Puntuación de habilidades comunicativas
- **Projects_Completed**: Número de proyectos completados
- **Extra_Curricular_Score**: Puntuación en actividades extracurriculares
- **Placement**: Variable objetivo - Colocación laboral exitosa (0/1)

## Objetivos 🎯

1. **Análisis Exploratorio**: Visualizar la distribución y relaciones entre variables
2. **Modelado Predictivo**: Identificar la importancia de cada factor usando regresión logística
3. **Optimización**: Encontrar la combinación óptima de habilidades para maximizar empleabilidad

## Metodología 🔬

### 1. Análisis Exploratorio de Datos (EDA)

- Histogramas de distribución de CGPA
- Gráficos de barras para variables categóricas
- Análisis de correlación entre variables numéricas
- Gráficos de dispersión con codificación por color

### 2. Preparación de Datos

Transformación de variables continuas a binarias usando umbrales:

- **CGPA Alto**: ≥ 8.0
- **Habilidades Comunicativas Altas**: ≥ 7.0
- **Proyectos Completados Altos**: ≥ 3
- **Actividades Extracurriculares Altas**: ≥ 7.0

### 3. Modelado con Regresión Logística

- Estandarización de datos usando `StandardScaler`
- Entrenamiento del modelo de regresión logística
- Extracción de coeficientes normalizados como pesos de importancia

### 4. Optimización Lineal

- Formulación del problema usando PuLP
- **Función Objetivo**: Maximizar probabilidad de colocación laboral
- **Variables de Decisión**: Binarias (0/1) para cada habilidad
- **Restricciones**:
  - Máximo 3 atributos altos (limitación de recursos)
  - Experiencia en prácticas requiere CGPA alto
  - Al menos CGPA alto O proyectos altos (requisito mínimo académico)

## Estructura del Proyecto 📁

```
modelo-optimizacion-estudiantes-puesto-laboral/
│
├── README.md                                          # Este archivo
├── .gitignore                                         # Archivos a ignorar en Git
├── requisitos.txt                                     # Dependencias del proyecto
│
├── data/
│   └── college_student_placement_dataset_convert.csv  # Dataset principal
│
├── src/
│   ├── graficas.py                                   # Análisis exploratorio y visualizaciones
│   └── empleabilidad.py                             # Modelo de optimización
│
└── docs/
    └── ACA INVESTIGACION DE OPERACIONES.pdf          # Documentación del proyecto
```

## Instalación y Uso 🚀

### Prerrequisitos

```bash
Python 3.8+
```

### Instalación

```bash
# Clonar el repositorio
git clone https://github.com/JuanRinconG21/modelo-optimizacion-estudiantes-puesto-laboral.git
cd modelo-optimizacion-estudiantes-puesto-laboral

# Instalar dependencias
pip install -r requisitos.txt
```

### Ejecución

```bash
# Ejecutar análisis exploratorio
python src/graficas.py

# Ejecutar modelo de optimización
python src/empleabilidad.py
```

## Dependencias 📦

```txt
pandas>=1.5.0
numpy>=1.21.0
scikit-learn>=1.1.0
matplotlib>=3.5.0
seaborn>=0.11.0
pulp>=2.6.0
```

## Visualizaciones 📊

El proyecto incluye:

- Histogramas de distribución de CGPA
- Gráficos de barras para experiencia en prácticas y colocación laboral
- Gráficos de dispersión CGPA vs Habilidades Comunicativas
- Análisis de correlaciones entre variables

## Tecnologías Utilizadas 🛠️

- **Python**: Lenguaje principal
- **Pandas**: Manipulación y análisis de datos
- **NumPy**: Operaciones matemáticas
- **Scikit-learn**: Modelado de machine learning
- **Matplotlib/Seaborn**: Visualización de datos
- **PuLP**: Optimización lineal
- **Jupyter**: Ambiente de desarrollo interactivo

## Agradecimientos 🙏

- Dataset proporcionado por [Kaggle](https://www.kaggle.com/)
- Comunidad de Python y librerías de código abierto
- Recursos educativos de análisis de datos y optimización
