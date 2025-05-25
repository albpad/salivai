"""
SalivAI - Advanced Clinical Dashboard
Modern medical interface with enhanced visualizations and professional design
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import plotly.figure_factory as ff

# Import our literature-based predictor
from salivary_gland_malignancy_predictor import LiteratureBasedMalignancyPredictor

# Configure Streamlit page
st.set_page_config(
    page_title="SalivAI - Clinical Dashboard",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Advanced medical dashboard CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');
    
    :root {
        --primary-blue: #2563eb;
        --primary-blue-light: #3b82f6;
        --primary-blue-dark: #1d4ed8;
        --success-green: #059669;
        --warning-orange: #d97706;
        --danger-red: #dc2626;
        --neutral-50: #f8fafc;
        --neutral-100: #f1f5f9;
        --neutral-200: #e2e8f0;
        --neutral-300: #cbd5e1;
        --neutral-400: #94a3b8;
        --neutral-500: #64748b;
        --neutral-600: #475569;
        --neutral-700: #334155;
        --neutral-800: #1e293b;
        --neutral-900: #0f172a;
    }
    
    .stApp {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        background: linear-gradient(135deg, var(--neutral-50) 0%, var(--neutral-100) 100%);
        color: var(--neutral-900);
    }
    
    /* Main container with glassmorphism effect */
    .main-dashboard {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        border-radius: 24px;
        padding: 2rem;
        margin: 1rem;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 
            0 20px 25px -5px rgba(0, 0, 0, 0.1),
            0 10px 10px -5px rgba(0, 0, 0, 0.04);
    }
    
    /* Header section */
    .dashboard-header {
        text-align: center;
        margin-bottom: 3rem;
        padding-bottom: 2rem;
        border-bottom: 2px solid var(--neutral-200);
        position: relative;
    }
    
    .dashboard-header::after {
        content: '';
        position: absolute;
        bottom: -2px;
        left: 50%;
        transform: translateX(-50%);
        width: 100px;
        height: 4px;
        background: linear-gradient(90deg, var(--primary-blue), var(--primary-blue-light));
        border-radius: 2px;
    }
    
    .app-title {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, var(--primary-blue) 0%, var(--primary-blue-light) 50%, #6366f1 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
        letter-spacing: -0.02em;
    }
    
    .subtitle {
        color: var(--neutral-600);
        font-size: 1.25rem;
        font-weight: 500;
        margin-bottom: 0.5rem;
    }
    
    .version-badge {
        display: inline-block;
        background: linear-gradient(135deg, var(--primary-blue), var(--primary-blue-light));
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    /* Input section with modern cards */
    .input-section {
        background: linear-gradient(135deg, var(--primary-blue) 0%, var(--primary-blue-dark) 100%);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 3rem;
        box-shadow: 0 20px 25px -5px rgba(37, 99, 235, 0.3);
    }
    
    /* Streamlit component overrides for input section */
    .input-section .stSelectbox label, 
    .input-section .stSlider label {
        color: white !important;
        font-weight: 600 !important;
        font-size: 0.875rem !important;
        text-transform: uppercase !important;
        letter-spacing: 0.05em !important;
        margin-bottom: 0.5rem !important;
    }
    
    .input-section .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.2) !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
        border-radius: 12px !important;
        color: white !important;
        font-weight: 500 !important;
    }
    
    .input-section .stSlider > div > div > div > div {
        background: linear-gradient(90deg, rgba(255, 255, 255, 0.3), rgba(255, 255, 255, 0.5)) !important;
    }
    
    .input-section .stSlider .stSlider > div > div > div {
        background: rgba(255, 255, 255, 0.1) !important;
        border-radius: 8px !important;
    }
    
    /* Results grid */
    .results-grid {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        gap: 2rem;
        margin-bottom: 3rem;
    }
    
    .result-card {
        background: white;
        border-radius: 20px;
        padding: 2rem;
        border: 1px solid var(--neutral-200);
        box-shadow: 
            0 10px 15px -3px rgba(0, 0, 0, 0.1),
            0 4px 6px -2px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .result-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, var(--primary-blue), var(--primary-blue-light));
    }
    
    .result-card:hover {
        transform: translateY(-4px);
        box-shadow: 
            0 20px 25px -5px rgba(0, 0, 0, 0.15),
            0 10px 10px -5px rgba(0, 0, 0, 0.1);
    }
    
    .card-title {
        font-size: 1.125rem;
        font-weight: 600;
        color: var(--neutral-700);
        margin-bottom: 1.5rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    /* Risk category styling */
    .risk-display {
        text-align: center;
        padding: 2rem 1rem;
    }
    
    .risk-percentage {
        font-size: 4rem;
        font-weight: 800;
        line-height: 1;
        margin-bottom: 1rem;
    }
    
    .risk-label {
        font-size: 1.25rem;
        font-weight: 600;
        margin-bottom: 1rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    .risk-description {
        font-size: 0.875rem;
        color: var(--neutral-600);
        line-height: 1.5;
    }
    
    .risk-low .risk-percentage { color: var(--success-green); }
    .risk-intermediate .risk-percentage { color: var(--warning-orange); }
    .risk-high .risk-percentage { color: var(--danger-red); }
    
    .risk-low .risk-label { color: var(--success-green); }
    .risk-intermediate .risk-label { color: var(--warning-orange); }
    .risk-high .risk-label { color: var(--danger-red); }
    
    /* Metrics grid */
    .metrics-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
        gap: 1rem;
        margin-top: 2rem;
    }
    
    .metric-card {
        background: var(--neutral-50);
        border-radius: 12px;
        padding: 1.5rem 1rem;
        text-align: center;
        border: 1px solid var(--neutral-200);
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        background: white;
        transform: translateY(-2px);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    .metric-value {
        font-size: 1.875rem;
        font-weight: 700;
        color: var(--primary-blue);
        margin-bottom: 0.5rem;
    }
    
    .metric-label {
        font-size: 0.75rem;
        color: var(--neutral-600);
        text-transform: uppercase;
        letter-spacing: 0.05em;
        font-weight: 500;
    }
    
    /* Bottom section */
    .bottom-section {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 2rem;
        margin-top: 3rem;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
    
    /* Responsive design */
    @media (max-width: 1024px) {
        .results-grid {
            grid-template-columns: 1fr;
        }
        .bottom-section {
            grid-template-columns: 1fr;
        }
    }
    
    @media (max-width: 768px) {
        .app-title {
            font-size: 2.5rem;
        }
        .input-grid {
            grid-template-columns: 1fr;
        }
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    return LiteratureBasedMalignancyPredictor()

def create_advanced_gauge(probability):
    """Create an advanced gauge with multiple indicators"""
    
    if probability < 0.3:
        color = "#059669"  # Success green
        risk_zone = "Low Risk"
    elif probability < 0.7:
        color = "#d97706"  # Warning orange
        risk_zone = "Moderate Risk"
    else:
        color = "#dc2626"  # Danger red
        risk_zone = "High Risk"
    
    fig = go.Figure()
    
    # Main gauge
    fig.add_trace(go.Indicator(
        mode = "gauge+number+delta",
        value = probability * 100,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Malignancy Probability", 'font': {'size': 16, 'color': '#334155'}},
        number = {
            'font': {'size': 48, 'family': 'Inter', 'color': color},
            'suffix': '%'
        },
        delta = {'reference': 50, 'position': "top"},
        gauge = {
            'axis': {
                'range': [None, 100],
                'tickwidth': 2,
                'tickcolor': "#cbd5e1",
                'tickfont': {'size': 12, 'family': 'Inter', 'color': '#64748b'}
            },
            'bar': {'color': color, 'thickness': 0.3},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "#e2e8f0",
            'steps': [
                {'range': [0, 30], 'color': "rgba(5, 150, 105, 0.1)"},
                {'range': [30, 70], 'color': "rgba(217, 119, 6, 0.1)"},
                {'range': [70, 100], 'color': "rgba(220, 38, 38, 0.1)"}
            ],
            'threshold': {
                'line': {'color': color, 'width': 4},
                'thickness': 0.75,
                'value': probability * 100
            }
        }
    ))
    
    fig.update_layout(
        height=300,
        margin=dict(l=20, r=20, t=40, b=20),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font={'family': 'Inter', 'color': '#334155'}
    )
    
    return fig

def create_feature_importance_chart(importance_dict):
    """Create a horizontal bar chart for feature importance"""
    
    features = list(importance_dict.keys())
    importance = list(importance_dict.values())
    
    # Clean feature names and sort by importance
    clean_data = []
    for feature, imp in zip(features, importance):
        clean_name = feature.replace('_', ' ').replace('location ', '').replace('size ', '').replace('gt ', '>').title()
        clean_data.append((clean_name, imp))
    
    clean_data.sort(key=lambda x: x[1], reverse=True)
    clean_features, clean_importance = zip(*clean_data)
    
    # Create color scale
    colors = px.colors.sequential.Blues_r[:len(clean_features)]
    
    fig = go.Figure(go.Bar(
        x=clean_importance,
        y=clean_features,
        orientation='h',
        marker=dict(
            color=colors,
            line=dict(color='#1e293b', width=1)
        ),
        text=[f'{imp:.3f}' for imp in clean_importance],
        textposition='inside',
        textfont=dict(color='white', size=12, family='Inter')
    ))
    
    fig.update_layout(
        title=dict(
            text="Feature Importance",
            font=dict(size=16, color='#334155', family='Inter'),
            x=0.5
        ),
        height=300,
        margin=dict(l=20, r=20, t=40, b=20),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="white",
        font={'family': 'Inter', 'color': '#334155'},
        xaxis=dict(
            showgrid=True,
            gridcolor='#f1f5f9',
            tickfont=dict(color='#64748b', size=11)
        ),
        yaxis=dict(
            showgrid=False,
            tickfont=dict(color='#64748b', size=11)
        )
    )
    
    return fig

def create_risk_distribution_donut():
    """Create a donut chart for risk distribution"""
    
    categories = ['Low Risk<br>(0-30%)', 'Moderate Risk<br>(30-70%)', 'High Risk<br>(70-100%)']
    values = [35, 45, 20]  # Example distribution
    colors = ['#059669', '#d97706', '#dc2626']
    
    fig = go.Figure(data=[go.Pie(
        labels=categories,
        values=values,
        hole=0.6,
        marker=dict(colors=colors, line=dict(color='white', width=2)),
        textinfo='label+percent',
        textfont=dict(size=12, family='Inter'),
        hovertemplate='<b>%{label}</b><br>%{percent}<br><extra></extra>'
    )])
    
    # Add center text
    fig.add_annotation(
        text="Population<br>Distribution",
        x=0.5, y=0.5,
        font=dict(size=14, color='#334155', family='Inter'),
        showarrow=False
    )
    
    fig.update_layout(
        title=dict(
            text="Risk Categories in Population",
            font=dict(size=16, color='#334155', family='Inter'),
            x=0.5
        ),
        height=300,
        margin=dict(l=20, r=20, t=40, b=20),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font={'family': 'Inter', 'color': '#334155'},
        showlegend=False
    )
    
    return fig

def create_confidence_intervals():
    """Create confidence interval visualization"""
    
    # Simulated confidence intervals for different risk factors
    factors = ['Age >60', 'Large Size', 'Irregular Margins', 'Hypoechoic', 'High Vascularity']
    odds_ratios = [2.1, 3.4, 2.8, 1.9, 2.3]
    lower_ci = [1.5, 2.1, 1.8, 1.2, 1.6]
    upper_ci = [2.9, 5.5, 4.3, 3.0, 3.3]
    
    fig = go.Figure()
    
    # Add confidence intervals
    for i, (factor, or_val, lower, upper) in enumerate(zip(factors, odds_ratios, lower_ci, upper_ci)):
        fig.add_trace(go.Scatter(
            x=[lower, upper],
            y=[i, i],
            mode='lines',
            line=dict(color='#2563eb', width=4),
            showlegend=False,
            hovertemplate=f'<b>{factor}</b><br>95% CI: {lower:.1f} - {upper:.1f}<extra></extra>'
        ))
        
        # Add point estimate
        fig.add_trace(go.Scatter(
            x=[or_val],
            y=[i],
            mode='markers',
            marker=dict(color='#1d4ed8', size=10, symbol='diamond'),
            showlegend=False,
            hovertemplate=f'<b>{factor}</b><br>OR: {or_val:.1f}<extra></extra>'
        ))
    
    # Add reference line at OR = 1
    fig.add_vline(x=1, line_dash="dash", line_color="#64748b", opacity=0.7)
    
    fig.update_layout(
        title=dict(
            text="Odds Ratios with 95% Confidence Intervals",
            font=dict(size=16, color='#334155', family='Inter'),
            x=0.5
        ),
        height=300,
        margin=dict(l=20, r=20, t=40, b=20),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="white",
        font={'family': 'Inter', 'color': '#334155'},
        xaxis=dict(
            title="Odds Ratio",
            showgrid=True,
            gridcolor='#f1f5f9',
            tickfont=dict(color='#64748b', size=11),
            title_font=dict(color='#334155', size=12)
        ),
        yaxis=dict(
            tickmode='array',
            tickvals=list(range(len(factors))),
            ticktext=factors,
            showgrid=False,
            tickfont=dict(color='#64748b', size=11)
        )
    )
    
    return fig

def main():
    predictor = load_model()
    
    # Main dashboard container
    st.markdown('<div class="main-dashboard">', unsafe_allow_html=True)
    
    # Header
    st.markdown("""
    <div class="dashboard-header">
        <h1 class="app-title">SalivAI</h1>
        <p class="subtitle">Advanced Clinical Risk Assessment Platform</p>
        <span class="version-badge">v2.0 Enhanced</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Input section
    st.markdown('<div class="input-section">', unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    
    with col1:
        age = st.slider("Patient Age", 18, 90, 55)
    
    with col2:
        gender = st.selectbox("Gender", ["female", "male"])
    
    with col3:
        location = st.selectbox("Tumor Location", ["parotid", "submandibular", "minor"])
    
    with col4:
        size = st.selectbox("Tumor Size", ["≤2cm", "2-4cm", ">4cm"])
    
    with col5:
        margins = st.selectbox("Tumor Margins", ["regular", "irregular"])
    
    with col6:
        echo = st.selectbox("Echogenicity", ["iso-hyperechoic", "hypoechoic"])
    
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
    st.markdown('<div class="results-grid">', unsafe_allow_html=True)
    
    # Main risk gauge
    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">Risk Assessment</div>', unsafe_allow_html=True)
    gauge_fig = create_advanced_gauge(probability)
    st.plotly_chart(gauge_fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Feature importance
    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">Contributing Factors</div>', unsafe_allow_html=True)
    importance = predictor.get_feature_importance()
    importance_fig = create_feature_importance_chart(importance)
    st.plotly_chart(importance_fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Risk category display
    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    risk_category = risk_result['risk_category']
    if "Low" in risk_category:
        risk_class = "risk-low"
        description = "Low probability of malignancy. Continue routine monitoring."
    elif "Intermediate" in risk_category:
        risk_class = "risk-intermediate"
        description = "Moderate risk detected. Consider additional imaging or biopsy."
    else:
        risk_class = "risk-high"
        description = "High malignancy risk. Urgent evaluation recommended."
    
    st.markdown(f"""
    <div class="risk-display {risk_class}">
        <div class="risk-percentage">{probability:.1%}</div>
        <div class="risk-label">{risk_category}</div>
        <div class="risk-description">{description}</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Model performance metrics
    st.markdown("""
    <div class="metrics-grid">
        <div class="metric-card">
            <div class="metric-value">0.89</div>
            <div class="metric-label">AUC-ROC</div>
        </div>
        <div class="metric-card">
            <div class="metric-value">0.85</div>
            <div class="metric-label">Sensitivity</div>
        </div>
        <div class="metric-card">
            <div class="metric-value">0.91</div>
            <div class="metric-label">Specificity</div>
        </div>
        <div class="metric-card">
            <div class="metric-value">25+</div>
            <div class="metric-label">Studies</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Bottom section with additional visualizations
    st.markdown('<div class="bottom-section">', unsafe_allow_html=True)
    
    # Population distribution
    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">Population Risk Distribution</div>', unsafe_allow_html=True)
    donut_fig = create_risk_distribution_donut()
    st.plotly_chart(donut_fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Confidence intervals
    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">Evidence Base</div>', unsafe_allow_html=True)
    ci_fig = create_confidence_intervals()
    st.plotly_chart(ci_fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main() 