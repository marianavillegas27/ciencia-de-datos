# Parcial 1 - Ciencia de Datos

**Estudiante:** Mariana Villegas Alzate
**Curso:** Ciencia de Datos 2026-1 (Universidad Icesi)

## Descripción del Proyecto

Este repositorio contiene el "Parcial 1" de la materia Ciencia de Datos. El informe realiza un análisis exploratorio que compara la percepción de bienestar individual frente al entorno social y político en **Colombia y Argentina** utilizando la base de datos de **Latinobarómetro 2023**.

A través de cuatro variables clave (satisfacción vital, tipos de violencia, satisfacción democrática y espacios de expresión), el proyecto busca entender la desconexión existente entre la esfera privada y la pública de los ciudadanos en ambos países.

## Estructura de Archivos

- `Parcial 1- Villegas Alzate Mariana.Rmd`: Archivo fuente en R Markdown que contiene todo el proceso de carga de datos, manipulación con `dplyr`, y visualización con `ggplot2`.
- `Parcial-1--Villegas-Alzate-Mariana.html`: El reporte final compilado y exportado en formato HTML.
- `test.py`: Código de Python (usando `pandas` y `seaborn`) que reproduce de manera interactiva el gráfico de "Satisfacción con la Democracia", leyendo los datos directamente de un `.csv` convertido.
- `Latinobarometro_2023_Esp.pdf`: Documentación de la base de datos.
- `Parcial_1_2026-1.pdf`: Archivo con las instrucciones o formato del parcial.

> **Nota:** Los archivos de datos pesados (`baselatin.rdata` y `baselatin.csv`) se han omitido de este repositorio mediante `.gitignore` por cuestiones de optimización de espacio.

## Requisitos para Ejecución

### R
Para ejecutar el informe `.Rmd` se necesitan las librerías:
- `dplyr`
- `ggplot2`
- `scales`
- `kableExtra`

### Python
Para reproducir el gráfico exportado a Python se debe crear un ambiente virtual e instalar las dependencias:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pandas matplotlib seaborn pyreadr numpy
```

Luego ejecutar el script con:
```bash
python3 test.py
```
