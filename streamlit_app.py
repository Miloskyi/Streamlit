import os
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Configuración de página con estilo BMW
st.set_page_config(
    page_title="BMW Global Intelligence Platform",
    page_icon="🚗",
    layout="wide"
)

# --- ESTILOS CSS PERSONALIZADOS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .bmw-header {
        background-color: #0653b6;
        padding: 2rem;
        border-radius: 10px;
        color: white;
        margin-bottom: 2rem;
    }
    
    .expert-card {
        background-color: #f1f3f6;
        border-left: 5px solid #0653b6;
        padding: 1.5rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    
    .metric-container {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        text-align: center;
        border: 1px solid #e0e0e0;
    }
    
    .stButton>button {
        background-color: #1c1c1c;
        color: white;
        border-radius: 0;
        padding: 0.5rem 2rem;
        transition: 0.3s;
    }
    
    .stButton>button:hover {
        background-color: #0653b6;
        border-color: #0653b6;
    }

    .help-text {
        font-size: 0.85rem;
        color: #666;
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)

# --- CARGA DE DATOS ---
@st.cache_data
def load_data():
    # Usando el archivo proporcionado por el usuario
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "bmw_global_sales_2018_2025.csv")
    df = pd.read_csv(file_path)
    
    # Crear una columna de fecha para series temporales
    df['Date'] = pd.to_datetime(df[['Year', 'Month']].assign(Day=1))
    return df

try:
    df = load_data()
except Exception as e:
    st.error(f"Error al cargar el dataset: {e}")
    st.stop()

# --- LÓGICA DE NAVEGACIÓN ---
if 'view' not in st.session_state:
    st.session_state.view = 'landing'

def switch_view(view_name):
    st.session_state.view = view_name

# --- VISTA 1: LANDING PAGE ---
if st.session_state.view == 'landing':
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("<div style='margin-top: 50px;'>", unsafe_allow_html=True)
        st.image("https://upload.wikimedia.org/wikipedia/commons/4/44/BMW.svg", width=80)
        st.title("BMW Global Sales Intelligence")
        st.subheader("Plataforma de Análisis Estratégico 2018-2025")
        
        st.markdown("""
        <div class='expert-card'>
            <strong>🎙️ Mensaje del Analista Senior:</strong><br>
            "Este dataset representa la transformación más profunda de BMW en la última década. 
            Analizaremos más de 7 años de datos, cubriendo la transición hacia los vehículos eléctricos (BEV), 
            el impacto del PIB global en el sector premium y el rendimiento de modelos icónicos como el 
            Serie 3, Serie 5 y la línea X."
        </div>
        """, unsafe_allow_html=True)
        
        st.write("""
        **Lo que descubrirás en este Workspace:**
        - Tendencias de adopción de movilidad eléctrica.
        - Correlación entre precios de combustible y ventas.
        - Desempeño regional comparativo (China, Europa, USA).
        """)
        
        if st.button("Acceder al Workspace Interactivo"):
            switch_view('workspace')
            st.rerun()
            
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        # Visualización rápida para la landing
        fig, ax = plt.subplots(figsize=(10, 7))
        sns.set_palette(["#0653b6", "#1c1c1c", "#757575"])
        sns.lineplot(data=df, x='Year', y='Units_Sold', hue='Region', marker='o', errorbar=None)
        plt.title("Tendencia Histórica de Ventas por Región", fontsize=14, fontweight='bold', pad=20)
        plt.ylabel("Unidades Vendidas")
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        st.pyplot(fig)

# --- VISTA 2: WORKSPACE ---
elif st.session_state.view == 'workspace':
    # Barra lateral con filtros
    with st.sidebar:
        st.image("https://upload.wikimedia.org/wikipedia/commons/4/44/BMW.svg", width=50)
        st.title("Filtros del Experto")
        
        years = st.multiselect("Seleccionar Años", options=sorted(df['Year'].unique()), default=df['Year'].unique())
        regions = st.multiselect("Regiones Geográficas", options=df['Region'].unique(), default=df['Region'].unique())
        models = st.multiselect("Modelos", options=df['Model'].unique(), default=['3 Series', '5 Series', 'X5', 'i4'])
        
        st.markdown("---")
        if st.button("Volver al Inicio"):
            switch_view('landing')
            st.rerun()

    # Filtrado de datos
    mask = (df['Year'].isin(years)) & (df['Region'].isin(regions)) & (df['Model'].isin(models))
    fdf = df[mask]

    # Header de Análisis
    st.markdown("<div class='bmw-header'><h1>📊 Panel de Control: Análisis de Mercado Global</h1></div>", unsafe_allow_html=True)

    # KPIs Principales
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    
    with kpi1:
        total_units = fdf['Units_Sold'].sum()
        st.markdown(f"<div class='metric-container'><h3>📦 Unidades</h3><h2>{total_units:,.0f}</h2><p class='help-text'>Volumen total vendido</p></div>", unsafe_allow_html=True)
    
    with kpi2:
        total_rev = fdf['Revenue_EUR'].sum()
        st.markdown(f"<div class='metric-container'><h3>💰 Ingresos</h3><h2>€{total_rev/1e9:.2f}B</h2><p class='help-text'>Facturación bruta acumulada</p></div>", unsafe_allow_html=True)
        
    with kpi3:
        avg_bev = fdf['BEV_Share'].mean() * 100
        st.markdown(f"<div class='metric-container'><h3>🔌 Cuota BEV</h3><h2>{avg_bev:.1f}%</h2><p class='help-text'>Mix de vehículos eléctricos</p></div>", unsafe_allow_html=True)
        
    with kpi4:
        premium_avg = fdf['Premium_Share'].mean() * 100
        st.markdown(f"<div class='metric-container'><h3>💎 Cuota Premium</h3><h2>{premium_avg:.1f}%</h2><p class='help-text'>Dominio en mercado de lujo</p></div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # FILA 1: Tendencia y Distribución
    col_a, col_b = st.columns([1.5, 1])
    
    with col_a:
        st.markdown("### 📈 Evolución Temporal de Ventas ℹ️", help="Visualización de la tendencia de ventas mensuales agregada por modelo.")
        fig1, ax1 = plt.subplots(figsize=(12, 6))
        sns.set_style("whitegrid")
        # Agrupamos por fecha y modelo
        trend_data = fdf.groupby(['Date', 'Model'])['Units_Sold'].sum().reset_index()
        sns.lineplot(data=trend_data, x='Date', y='Units_Sold', hue='Model', ax=ax1, palette="tab10", linewidth=2)
        ax1.set_title("Ventas Mensuales por Modelo", fontsize=12)
        plt.xticks(rotation=45)
        st.pyplot(fig1)

    with col_b:
        st.markdown("### 🌍 Ingresos por Región ℹ️", help="Proporción de ingresos (EUR) generados por cada región seleccionada.")
        fig2, ax2 = plt.subplots(figsize=(8, 8))
        reg_data = fdf.groupby('Region')['Revenue_EUR'].sum()
        colors = ["#0653b6", "#1c1c1c", "#757575", "#e6e6e6"]
        plt.pie(reg_data, labels=reg_data.index, autopct='%1.1f%%', startangle=140, colors=colors, wedgeprops={'edgecolor': 'white'})
        plt.title("Revenue Share %", fontweight='bold')
        st.pyplot(fig2)

    st.markdown("---")

    # FILA 2: Análisis Avanzado (Seaborn Expert)
    st.markdown("### 🔍 Correlaciones y Segmentación Estratégica")
    col_c, col_d = st.columns(2)

    with col_c:
        st.markdown("**💰 Precio Promedio vs. Volumen por Modelo** ℹ️", help="Relación entre el precio de venta (EUR) y la cantidad de unidades vendidas.")
        fig3, ax3 = plt.subplots(figsize=(10, 6))
        sns.scatterplot(data=fdf, x='Avg_Price_EUR', y='Units_Sold', hue='Model', size='BEV_Share', alpha=0.6, sizes=(40, 400), ax=ax3)
        plt.title("Estrategia de Pricing y Volumen")
        st.pyplot(fig3)

    with col_d:
        st.markdown("**📉 Impacto del Precio del Combustible** ℹ️", help="Análisis de cómo la fluctuación del precio del combustible afecta a las unidades vendidas.")
        fig4, ax4 = plt.subplots(figsize=(10, 6))
        sns.regplot(data=fdf, x='Fuel_Price_Index', y='Units_Sold', scatter_kws={'alpha':0.3, 'color':'#0653b6'}, line_kws={'color':'#1c1c1c'}, ax=ax4)
        plt.title("Regresión: Fuel Index vs Units Sold")
        st.pyplot(fig4)

    # Conclusiones del Experto
    st.markdown("""
    <div class='expert-card'>
        <strong>📌 Conclusiones del Análisis de Datos:</strong><br>
        1. <strong>Transición Eléctrica:</strong> Se observa un crecimiento sostenido en la cuota <i>BEV Share</i> a partir de 2021, impulsado por modelos como el i4 e iX.<br>
        2. <strong>Resiliencia Regional:</strong> China sigue siendo el mercado con mayor crecimiento de ingresos a pesar de la volatilidad económica global.<br>
        3. <strong>Sensibilidad de Precios:</strong> El índice de precios de combustible muestra una correlación inversa con las ventas de modelos de combustión de alto volumen.
    </div>
    """, unsafe_allow_html=True)

    # Datos brutos
    with st.expander("📂 Explorar Dataset Crudo"):
        st.write(fdf)

# Footer
st.markdown("<p style='text-align: center; color: #999; margin-top: 50px;'>BMW Global Sales Analysis v2.5 | Diseñado para Analistas de Negocios</p>", unsafe_allow_html=True)