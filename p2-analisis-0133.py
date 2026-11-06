import os
import numpy as np
import pandas as pd

# Datos del estudiante
# Karla Saenz NC 0133

empleados = {
    "Empleado": ["Elena", "Sergio", "Lucia", "Gonzalo", "Valeria", "Diego"],
    "Departamento": ["Ventas", "IT", "HR", "IT", "Ventas", "Finanzas"],
    "Horas_Capacitacion": [40, 80, 25, 60, 90, 15],
    "Evaluacion_Desempeno": [8.5, 9.2, 7.0, 8.8, 9.6, 6.5],
}

# 1. Creación del DataFrame
df = pd.DataFrame(empleados)

print(" DataFrame original:")
print(df)
print("\n" + "-+" * 20 + " Agrupar por una sola columna " + "-+" * 20)

# 2. Agrupación por Departamento
grupo_dept = df.groupby("Departamento")
print(grupo_dept)

print("\n" + "+-" * 20 + " Funciones de agregación " + "+-" * 20)

# Promedio de Horas de Capacitación por Departamento
print("\n Promedio de Horas de Capacitación por departamento:")
print(grupo_dept["Horas_Capacitacion"].mean())

# Evaluación de Desempeño máxima por Departamento
print("\n Máxima Evaluación de Desempeño por departamento:")
print(grupo_dept["Evaluacion_Desempeno"].max())

# 3. Resumen agregativo múltiple por departamento
print("\n Resumen estadístico por departamento:")
resumen = grupo_dept.agg(
    Promedio_Horas=("Horas_Capacitacion", "mean"),
    Max_Evaluacion=("Evaluacion_Desempeno", "max"),
)
print(resumen)