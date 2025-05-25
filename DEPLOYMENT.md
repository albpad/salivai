# SalivAI Deployment Guide

## Quick Deployment to Streamlit Cloud

### 1. GitHub Repository
- Create a new public repository on GitHub
- Name: `salivai` or `salivary-gland-predictor`
- Push this code to the repository

### 2. Streamlit Cloud Deployment
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Click "New app"
4. Configure:
   - Repository: `your-username/salivai`
   - Branch: `main`
   - Main file: `app.py`
   - App URL: `salivai-predictor` (or your choice)

### 3. Automatic Deployment
Streamlit will automatically:
- Install dependencies from `requirements.txt`
- Deploy your app
- Provide a public URL

### 4. App Features
- Literature-based malignancy risk prediction
- Interactive dashboard interface
- No clinical recommendations (research tool only)
- Evidence-based on 25+ peer-reviewed studies

### 5. Updates
Any push to the main branch will automatically redeploy the app.

## Local Development
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Notes
- App is for research/educational purposes only
- Not intended for clinical decision making
- Based on published literature coefficients 