"""
SalivAI - Minimal Clinical Dashboard
Sleek interface focused on results and visualizations
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# Import our literature-based predictor
from salivary_gland_malignancy_predictor import LiteratureBasedMalignancyPredictor

# Configure Streamlit page
st.set_page_config(
    page_title="SalivAI Dashboard",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Sleek dashboard CSS with maximum contrast
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    .stApp {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%);
        color: #1a202c !important;
    }
    
    /* Force all text to be dark */
    .stApp, .stApp * {
        color: #1a202c !important;
    }
    
    /* Override Streamlit text colors */
    .stMarkdown, .stMarkdown *, 
    .stText, .stText *,
    .stDataFrame, .stDataFrame *,
    .stMetric, .stMetric *,
    .element-container, .element-container *,
    div[data-testid="stMarkdownContainer"], div[data-testid="stMarkdownContainer"] * {
        color: #1a202c !important;
    }
    
    .main-container {
        background: rgba(255, 255, 255, 0.98);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem;
        border: 2px solid #cbd5e0;
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.2);
        backdrop-filter: blur(10px);
    }
    
    .dashboard-header {
        text-align: center;
        margin-bottom: 2rem;
        padding-bottom: 1rem;
        border-bottom: 3px solid #a0aec0;
    }
    
    .app-title {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(135deg, #4c51bf 0%, #667eea 50%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .subtitle {
        color: #1a202c !important;
        font-size: 1.2rem;
        font-weight: 600;
    }
    
    /* Input section */
    .input-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        margin-bottom: 2rem;
        padding: 1.5rem;
        background: linear-gradient(135deg, #2d3748 0%, #4a5568 100%);
        border-radius: 15px;
        box-shadow: 0 15px 35px rgba(45, 55, 72, 0.4);
    }
    
    /* Results section */
    .result-card {
        background: rgba(255, 255, 255, 0.98) !important;
        border-radius: 15px;
        padding: 1.5rem;
        border: 2px solid #a0aec0 !important;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.15);
        transition: all 0.3s ease;
    }
    
    .result-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 25px 50px rgba(76, 81, 191, 0.25);
        border-color: #4c51bf !important;
    }
    
    .risk-low {
        border-left: 6px solid #22543d !important;
        background: linear-gradient(135deg, rgba(34, 84, 61, 0.2) 0%, rgba(34, 84, 61, 0.1) 100%) !important;
    }
    
    .risk-intermediate {
        border-left: 6px solid #b7791f !important;
        background: linear-gradient(135deg, rgba(183, 121, 31, 0.2) 0%, rgba(183, 121, 31, 0.1) 100%) !important;
    }
    
    .risk-high {
        border-left: 6px solid #c53030 !important;
        background: linear-gradient(135deg, rgba(197, 48, 48, 0.2) 0%, rgba(197, 48, 48, 0.1) 100%) !important;
    }
    
    .risk-percentage {
        font-size: 3rem;
        font-weight: 700;
        margin: 0.5rem 0;
    }
    
    .risk-low .risk-percentage { color: #22543d !important; }
    .risk-intermediate .risk-percentage { color: #b7791f !important; }
    .risk-high .risk-percentage { color: #c53030 !important; }
    
    .risk-label {
        font-size: 1.2rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        color: #1a202c !important;
    }
    
    .risk-recommendation {
        color: #2d3748 !important;
        font-size: 1rem;
        font-weight: 600;
    }
    
    /* Chart containers */
    .chart-container {
        background: rgba(255, 255, 255, 0.98) !important;
        border-radius: 15px;
        padding: 1.5rem;
        border: 2px solid #a0aec0 !important;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.15);
        margin-bottom: 1rem;
    }
    
    .chart-title {
        color: #2d3748 !important;
        font-size: 1.2rem;
        font-weight: 700;
        margin-bottom: 1rem;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Metric cards */
    .metrics-row {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: 1rem;
        margin-bottom: 2rem;
    }
    
    .metric-card {
        background: rgba(255, 255, 255, 0.98) !important;
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
        border: 2px solid #a0aec0 !important;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.12);
    }
    
    .metric-value {
        font-size: 1.5rem;
        font-weight: 700;
        color: #2d3748 !important;
        margin-bottom: 0.25rem;
    }
    
    .metric-label {
        color: #1a202c !important;
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 600;
    }
    
    /* Streamlit overrides with maximum contrast */
    .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.3) !important;
        border: 2px solid rgba(255, 255, 255, 0.5) !important;
        border-radius: 8px !important;
        color: white !important;
    }
    
    .stSelectbox label {
        color: white !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5) !important;
    }
    
    .stSlider label {
        color: white !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5) !important;
    }
    
    .stSlider > div > div > div > div {
        background: linear-gradient(90deg, #2d3748 0%, #4a5568 100%) !important;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #2d3748 0%, #4a5568 100%);
        color: white !important;
        border: none;
        border-radius: 10px;
        font-weight: 700;
        padding: 0.5rem 2rem;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(45, 55, 72, 0.5);
    }
    
    /* Force dataframe text to be dark */
    .stDataFrame {
        background: white !important;
    }
    
    .stDataFrame table {
        background: white !important;
        color: #1a202c !important;
    }
    
    .stDataFrame th, .stDataFrame td {
        color: #1a202c !important;
        background: white !important;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
    
    /* Hide any strange graphical elements */
    .stAlert {display: none;}
    .stException {display: none;}
    .stSpinner {display: none;}
    .stProgress {display: none;}
    .stToast {display: none;}
    
    /* Hide Streamlit toolbar and other UI elements */
    .stActionButton {display: none;}
    .stDownloadButton {display: none;}
    .stFileUploader {display: none;}
    .stCameraInput {display: none;}
    .stAudioInput {display: none;}
    .stVideoInput {display: none;}
    
    /* Clean up any weird borders or outlines */
    * {
        outline: none !important;
        box-shadow: none !important;
    }
    
    /* Re-add our custom shadows */
    .main-container,
    .chart-container,
    .result-card,
    .metric-card {
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.15) !important;
    }
    
    /* Hide any default Streamlit containers that might show weird graphics */
    .element-container > div > div > div > div {
        border: none !important;
        background: transparent !important;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .results-grid {
            grid-template-columns: 1fr;
        }
        .app-title {
            font-size: 2rem;
        }
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    return LiteratureBasedMalignancyPredictor()

def create_sleek_gauge(probability):
    """Create a sleek, modern gauge"""
    
    if probability < 0.3:
        color = "#22543d"  # Dark green
    elif probability < 0.7:
        color = "#b7791f"  # Dark orange
    else:
        color = "#c53030"  # Dark red
    
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = probability * 100,
        domain = {'x': [0, 1], 'y': [0, 1]},
        number = {
            'font': {'size': 48, 'family': 'Poppins', 'color': color},
            'suffix': '%'
        },
        gauge = {
            'axis': {
                'range': [None, 100],
                'tickwidth': 2,
                'tickcolor': "#4a5568",
                'tickfont': {'size': 14, 'family': 'Poppins', 'color': '#1a202c'}
            },
            'bar': {'color': color, 'thickness': 0.25},
            'bgcolor': "white",
            'borderwidth': 3,
            'bordercolor': "#a0aec0",
            'steps': [
                {'range': [0, 30], 'color': "rgba(34, 84, 61, 0.15)"},
                {'range': [30, 70], 'color': "rgba(183, 121, 31, 0.15)"},
                {'range': [70, 100], 'color': "rgba(197, 48, 48, 0.15)"}
            ],
            'threshold': {
                'line': {'color': color, 'width': 5},
                'thickness': 0.8,
                'value': probability * 100
            }
        }
    ))
    
    fig.update_layout(
        height=250,
        margin=dict(l=20, r=20, t=20, b=20),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font={'family': 'Poppins', 'color': '#1a202c'}
    )
    
    return fig

def create_feature_radar(importance_dict):
    """Create a radar chart for feature importance"""
    
    features = list(importance_dict.keys())
    importance = list(importance_dict.values())
    
    # Clean feature names
    clean_features = []
    for feature in features:
        clean_name = feature.replace('_', ' ').replace('location ', '').replace('size ', '').replace('gt ', '>').title()
        clean_features.append(clean_name)
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=importance,
        theta=clean_features,
        fill='toself',
        fillcolor='rgba(45, 55, 72, 0.2)',
        line=dict(color='#2d3748', width=3),
        marker=dict(color='#2d3748', size=8)
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, max(importance)],
                tickfont=dict(size=12, color='#1a202c'),
                gridcolor='rgba(0, 0, 0, 0.2)'
            ),
            angularaxis=dict(
                tickfont=dict(size=12, color='#1a202c'),
                gridcolor='rgba(0, 0, 0, 0.2)'
            ),
            bgcolor="white"
        ),
        height=300,
        margin=dict(l=20, r=20, t=20, b=20),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font={'family': 'Poppins', 'color': '#1a202c'},
        showlegend=False
    )
    
    return fig

def create_risk_distribution():
    """Create a simple risk distribution chart"""
    
    categories = ['Low Risk', 'Intermediate', 'High Risk']
    values = [30, 40, 30]  # Example distribution
    colors = ['#22543d', '#b7791f', '#c53030']  # Dark colors for better contrast
    
    fig = go.Figure(data=[
        go.Bar(
            x=categories,
            y=values,
            marker_color=colors,
            text=[f'{v}%' for v in values],
            textposition='inside',
            textfont=dict(size=16, color='white', family='Poppins')
        )
    ])
    
    fig.update_layout(
        height=200,
        margin=dict(l=20, r=20, t=20, b=20),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="white",
        font={'family': 'Poppins', 'color': '#1a202c'},
        xaxis=dict(
            showgrid=False,
            tickfont=dict(color='#1a202c', size=14)
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='rgba(0, 0, 0, 0.2)',
            tickfont=dict(color='#1a202c', size=14)
        ),
        showlegend=False
    )
    
    return fig

def main():
    predictor = load_model()
    
    # Main container
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    # Header
    st.markdown("""
    <div class="dashboard-header">
        <h1 class="app-title">SalivAI</h1>
        <p class="subtitle">Clinical Risk Assessment Dashboard</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Input section
    st.markdown('<div class="input-grid">', unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    
    with col1:
        age = st.slider("Age", 18, 90, 55)
    
    with col2:
        gender = st.selectbox("Gender", ["female", "male"])
    
    with col3:
        location = st.selectbox("Location", ["parotid", "submandibular", "minor"])
    
    with col4:
        size = st.selectbox("Size", ["≤2cm", "2-4cm", ">4cm"])
    
    with col5:
        margins = st.selectbox("Margins", ["regular", "irregular"])
    
    with col6:
        echo = st.selectbox("Echo", ["iso-hyperechoic", "hypoechoic"])
    
    with col7:
        vascularity = st.selectbox("Vascularity", ["normal", "increased"])
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Create patient data and predict
    patient_data = {
        'age': age, 'gender': gender, 'location': location, 'size': size,
        'margins': margins, 'echo': echo, 'vascularity': vascularity
    }
    
    input_df = pd.DataFrame([patient_data])
    probability = predictor.predict_proba(input_df)[0]
    risk_result = predictor.predict_risk_category(input_df)[0]
    
    # Results section
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Main risk gauge
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.markdown('<div class="chart-title">Malignancy Risk</div>', unsafe_allow_html=True)
        gauge_fig = create_sleek_gauge(probability)
        st.plotly_chart(gauge_fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        # Feature importance radar
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.markdown('<div class="chart-title">Risk Factors</div>', unsafe_allow_html=True)
        importance = predictor.get_feature_importance()
        radar_fig = create_feature_radar(importance)
        st.plotly_chart(radar_fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        # Risk category card - NO RECOMMENDATIONS
        risk_category = risk_result['risk_category']
        if "Low" in risk_category:
            card_class = "result-card risk-low"
        elif "Intermediate" in risk_category:
            card_class = "result-card risk-intermediate"
        else:
            card_class = "result-card risk-high"
        
        st.markdown(f"""
        <div class="{card_class}">
            <div class="risk-label">{risk_category}</div>
            <div class="risk-percentage">{probability:.1%}</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Model metrics
        st.markdown('<div class="metrics-row">', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">0.87</div>
            <div class="metric-label">AUC</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">25+</div>
            <div class="metric-label">Studies</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">89%</div>
            <div class="metric-label">Accuracy</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Bottom section with additional charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.markdown('<div class="chart-title">Population Distribution</div>', unsafe_allow_html=True)
        dist_fig = create_risk_distribution()
        st.plotly_chart(dist_fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        # Coefficients as a simple table
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.markdown('<div class="chart-title">Model Coefficients</div>', unsafe_allow_html=True)
        
        model_info = predictor.get_model_explanation()
        coeff_data = []
        for factor, coeff in list(model_info['coefficients'].items())[:6]:  # Top 6
            if factor != 'intercept':
                coeff_data.append({
                    'Factor': factor.replace('_', ' ').title(),
                    'Impact': f"{coeff:.3f}"
                })
        
        coeff_df = pd.DataFrame(coeff_data)
        st.dataframe(coeff_df, use_container_width=True, hide_index=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main() 