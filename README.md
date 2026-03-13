BMW Global Sales Intelligence Platform (2018-2025)

📋 Descripción del Proyecto

Este proyecto es una aplicación analítica de alto nivel desarrollada en Python y Streamlit para explorar el dataset de ventas globales de BMW desde 2018 hasta 2025. La plataforma está diseñada bajo un enfoque de "Consultoría Experta", proporcionando no solo visualizaciones de datos, sino también interpretaciones estratégicas sobre la transición eléctrica y el posicionamiento de mercado de la marca.

🚀 Características Principales

Landing Page Corporativa: Una introducción profesional con un mensaje editorial del analista senior.

Workspace Interactivo: Panel de control con filtros dinámicos (Año, Región, Modelo).

KPIs Estratégicos: Monitoreo en tiempo real de unidades vendidas, ingresos en euros, cuota de vehículos eléctricos (BEV) y cuota premium.

Análisis Visual con Seaborn: - Evolución de ventas mensuales.

Cuota de ingresos por región.

Correlación entre precio y volumen.

Impacto del índice de combustible en las ventas globales.

Expert Context: Iconos de ayuda y tarjetas informativas que explican la metodología de cada sección.

🛠️ Requisitos Técnicos

Para ejecutar este proyecto, necesitas instalar las siguientes librerías de Python:

pip install streamlit pandas seaborn matplotlib numpy


📂 Estructura del Dataset

El archivo bmw_global_sales_2018_2025.csv incluye las siguientes dimensiones clave:

Geografía: Región (Europa, China, USA, etc.).

Producto: Modelo (Serie 3, Serie 5, X5, i4, iX, etc.).

Ventas: Units_Sold, Avg_Price_EUR, Revenue_EUR.

Métricas de Transición: BEV_Share (Vehículos eléctricos), Premium_Share.

Macroeconomía: GDP_Growth (Crecimiento del PIB), Fuel_Price_Index (Precio combustible).

🚦 Instrucciones de Uso

Clona el repositorio:

git clone [https://github.com/tu-usuario/bmw-sales-analytics.git](https://github.com/tu-usuario/bmw-sales-analytics.git)


Navega al directorio:

cd bmw-sales-analytics


Ejecuta la aplicación:

streamlit run bmw_expert_analysis.py


🎨 Diseño y Estética

La aplicación sigue la guía de estilo de BMW, utilizando una paleta de colores sobria:

Azul Corporativo: #0653B6

Gris Oscuro: #1C1C1C

Fondo: #F8F9FA

Nota: Este proyecto ha sido desarrollado con fines de análisis de inteligencia de negocios para el dataset de BMW disponible en Kaggle.
