"""
SalivAI Demo Script - Honest Literature-Based Implementation
Demonstration of the Evidence-Based Salivary Gland Malignancy Predictor

This script showcases the capabilities of the literature-based model
"""

import pandas as pd
import numpy as np
from salivary_gland_malignancy_predictor import LiteratureBasedMalignancyPredictor, create_sample_data
import matplotlib.pyplot as plt

def demo_individual_predictions():
    """Demonstrate predictions for individual patients"""
    
    print("📚 SalivAI - Literature-Based Individual Patient Predictions")
    print("=" * 65)
    
    # Initialize predictor (no training needed!)
    predictor = LiteratureBasedMalignancyPredictor()
    
    # Example patients with different risk profiles
    patients = [
        {
            'name': 'Patient A (Low Risk Profile)',
            'age': 35,
            'gender': 'female',
            'location': 'parotid',
            'size': '≤2cm',
            'margins': 'regular',
            'echo': 'iso-hyperechoic',
            'vascularity': 'normal'
        },
        {
            'name': 'Patient B (Intermediate Risk Profile)',
            'age': 55,
            'gender': 'male',
            'location': 'submandibular',
            'size': '2-4cm',
            'margins': 'irregular',
            'echo': 'hypoechoic',
            'vascularity': 'normal'
        },
        {
            'name': 'Patient C (High Risk Profile)',
            'age': 68,
            'gender': 'male',
            'location': 'minor',
            'size': '>4cm',
            'margins': 'irregular',
            'echo': 'hypoechoic',
            'vascularity': 'increased'
        }
    ]
    
    for patient in patients:
        print(f"\n📋 {patient['name']}")
        print("-" * 45)
        
        # Create patient dataframe
        patient_data = {k: v for k, v in patient.items() if k != 'name'}
        patient_df = pd.DataFrame([patient_data])
        
        # Make prediction using literature coefficients
        probability = predictor.predict_proba(patient_df)[0]
        risk_result = predictor.predict_risk_category(patient_df)[0]
        
        print(f"Age: {patient['age']}, Gender: {patient['gender']}")
        print(f"Location: {patient['location']}, Size: {patient['size']}")
        print(f"Margins: {patient['margins']}, Echo: {patient['echo']}")
        print(f"Vascularity: {patient['vascularity']}")
        print()
        print(f"🎯 Malignancy Probability: {probability:.1%}")
        print(f"📊 Risk Category: {risk_result['risk_category']}")
        print(f"💡 Recommendation: {risk_result['recommendation']}")
        print(f"📈 Expected Rate: {risk_result['expected_malignancy_rate']}")

def demo_literature_foundation():
    """Demonstrate the literature foundation of the model"""
    
    print("\n\n📚 Literature Foundation Analysis")
    print("=" * 65)
    
    # Initialize predictor
    predictor = LiteratureBasedMalignancyPredictor()
    
    # Get model explanation
    explanation = predictor.get_model_explanation()
    
    print("Model Foundation:")
    print("-" * 20)
    print(f"Model Type: {explanation['model_type']}")
    print(f"Evidence Base: {explanation['evidence_base']}")
    print(f"Validation: {explanation['validation']}")
    
    print("\nLiterature-Derived Coefficients:")
    print("-" * 40)
    for factor, coeff in explanation['coefficients'].items():
        if factor != 'intercept':
            odds_ratio = np.exp(coeff)
            print(f"{factor.replace('_', ' ').title():<25} β: {coeff:6.3f}  OR: {odds_ratio:5.2f}")
    
    print(f"\nLiterature Sources:")
    print("-" * 20)
    for factor, source in explanation['sources'].items():
        print(f"• {factor.title()}: {source}")
    
    print(f"\nExpected Performance (from literature validation):")
    print("-" * 55)
    perf = explanation['expected_performance']
    print(f"AUC:        {perf['auc'][0]:.3f} - {perf['auc'][1]:.3f}")
    print(f"Sensitivity: {perf['sensitivity'][0]:.0%} - {perf['sensitivity'][1]:.0%}")
    print(f"Specificity: {perf['specificity'][0]:.0%} - {perf['specificity'][1]:.0%}")
    print(f"PPV:        {perf['ppv'][0]:.0%} - {perf['ppv'][1]:.0%}")
    print(f"NPV:        {perf['npv'][0]:.0%} - {perf['npv'][1]:.0%}")

def demo_feature_importance():
    """Demonstrate feature importance based on literature coefficients"""
    
    print("\n\n📊 Literature-Based Risk Factor Importance")
    print("=" * 65)
    
    # Initialize predictor
    predictor = LiteratureBasedMalignancyPredictor()
    
    # Get feature importance (based on absolute coefficient values)
    importance = predictor.get_feature_importance()
    
    # Sort by importance
    sorted_features = sorted(importance.items(), key=lambda x: x[1], reverse=True)
    
    print("Risk Factors (ranked by literature evidence strength):")
    print("-" * 55)
    for i, (feature, score) in enumerate(sorted_features, 1):
        feature_name = feature.replace('_', ' ').title()
        print(f"{i:2d}. {feature_name:<25} Importance: {score:.3f}")
    
    # Create visualization
    features, scores = zip(*sorted_features)
    
    plt.figure(figsize=(10, 6))
    plt.barh(range(len(features)), scores, color='steelblue')
    plt.yticks(range(len(features)), [f.replace('_', ' ').title() for f in features])
    plt.xlabel('Relative Importance (from literature coefficients)')
    plt.title('Literature-Based Risk Factor Importance')
    plt.tight_layout()
    plt.savefig('literature_feature_importance.png', dpi=300, bbox_inches='tight')
    print(f"\n📈 Feature importance chart saved as 'literature_feature_importance.png'")

def demo_batch_analysis():
    """Demonstrate batch analysis capabilities"""
    
    print("\n\n🧪 Batch Analysis Demo")
    print("=" * 65)
    
    # Initialize predictor
    predictor = LiteratureBasedMalignancyPredictor()
    
    # Create batch of patients with diverse profiles
    batch_patients = pd.DataFrame({
        'age': [45, 62, 38, 71, 29, 55, 67, 42],
        'gender': ['female', 'male', 'female', 'male', 'female', 'male', 'female', 'male'],
        'location': ['parotid', 'submandibular', 'minor', 'parotid', 'submandibular', 'minor', 'parotid', 'submandibular'],
        'size': ['≤2cm', '2-4cm', '>4cm', '2-4cm', '≤2cm', '>4cm', '2-4cm', '≤2cm'],
        'margins': ['regular', 'irregular', 'regular', 'irregular', 'regular', 'irregular', 'irregular', 'regular'],
        'echo': ['iso-hyperechoic', 'hypoechoic', 'hypoechoic', 'hypoechoic', 'iso-hyperechoic', 'hypoechoic', 'hypoechoic', 'iso-hyperechoic'],
        'vascularity': ['normal', 'increased', 'normal', 'increased', 'normal', 'increased', 'normal', 'normal']
    })
    
    print(f"Analyzing batch of {len(batch_patients)} patients using literature coefficients...")
    print()
    
    # Make batch predictions
    probabilities = predictor.predict_proba(batch_patients)
    risk_results = predictor.predict_risk_category(batch_patients)
    
    # Add results to dataframe
    results_df = batch_patients.copy()
    results_df['malignancy_probability'] = probabilities
    results_df['risk_category'] = [r['risk_category'] for r in risk_results]
    results_df['recommendation'] = [r['recommendation'] for r in risk_results]
    
    # Display results
    print("Batch Analysis Results:")
    print("-" * 30)
    for i, row in results_df.iterrows():
        print(f"Patient {i+1}: {row['malignancy_probability']:.1%} - {row['risk_category']}")
    
    # Risk distribution
    risk_counts = results_df['risk_category'].value_counts()
    print(f"\nRisk Distribution:")
    print("-" * 20)
    for risk, count in risk_counts.items():
        percentage = count / len(results_df) * 100
        print(f"{risk}: {count} patients ({percentage:.1f}%)")
    
    # Save results
    results_df.to_csv('literature_batch_analysis_results.csv', index=False)
    print(f"\n💾 Results saved to 'literature_batch_analysis_results.csv'")

def demo_model_transparency():
    """Demonstrate model transparency and interpretability"""
    
    print("\n\n🔍 Model Transparency Demo")
    print("=" * 65)
    
    # Initialize predictor
    predictor = LiteratureBasedMalignancyPredictor()
    
    # Example patient for step-by-step calculation
    patient_data = pd.DataFrame({
        'age': [60],
        'gender': ['male'],
        'location': ['submandibular'],
        'size': ['2-4cm'],
        'margins': ['irregular'],
        'echo': ['hypoechoic'],
        'vascularity': ['increased']
    })
    
    print("Step-by-Step Risk Calculation Example:")
    print("-" * 45)
    print("Patient: 60-year-old male, submandibular, 2-4cm, irregular margins, hypoechoic, increased vascularity")
    print()
    
    # Show the calculation breakdown
    coeffs = predictor.literature_coefficients
    
    print("Literature-Based Logistic Regression Calculation:")
    print("-" * 50)
    print(f"Intercept:                    {coeffs['intercept']:6.3f}")
    print(f"Age (normalized):             {coeffs['age']:6.3f} × {(60-50)/20:5.2f} = {coeffs['age'] * (60-50)/20:6.3f}")
    print(f"Location (submandibular):     {coeffs['location_submandibular']:6.3f} × 1     = {coeffs['location_submandibular']:6.3f}")
    print(f"Size (2-4cm):                 {coeffs['size_2_4cm']:6.3f} × 1     = {coeffs['size_2_4cm']:6.3f}")
    print(f"Gender (male):                {coeffs['gender_male']:6.3f} × 1     = {coeffs['gender_male']:6.3f}")
    print(f"Margins (irregular):          {coeffs['margins_irregular']:6.3f} × 1     = {coeffs['margins_irregular']:6.3f}")
    print(f"Echo (hypoechoic):            {coeffs['echo_hypoechoic']:6.3f} × 1     = {coeffs['echo_hypoechoic']:6.3f}")
    print(f"Vascularity (increased):      {coeffs['vascularity_increased']:6.3f} × 1     = {coeffs['vascularity_increased']:6.3f}")
    
    # Calculate linear predictor
    linear_pred = (coeffs['intercept'] + 
                   coeffs['age'] * (60-50)/20 + 
                   coeffs['location_submandibular'] + 
                   coeffs['size_2_4cm'] + 
                   coeffs['gender_male'] + 
                   coeffs['margins_irregular'] + 
                   coeffs['echo_hypoechoic'] + 
                   coeffs['vascularity_increased'])
    
    probability = 1 / (1 + np.exp(-linear_pred))
    
    print("-" * 50)
    print(f"Linear Predictor (sum):       {linear_pred:6.3f}")
    print(f"Probability = 1/(1+e^(-{linear_pred:.3f})) = {probability:.3f} = {probability:.1%}")
    
    # Verify with actual prediction
    actual_prob = predictor.predict_proba(patient_data)[0]
    print(f"Verified with model:          {actual_prob:.3f} = {actual_prob:.1%}")

def demo_honest_limitations():
    """Demonstrate honest discussion of model limitations"""
    
    print("\n\n⚠️  Model Limitations and Honest Assessment")
    print("=" * 65)
    
    predictor = LiteratureBasedMalignancyPredictor()
    explanation = predictor.get_model_explanation()
    
    print("What This Model DOES:")
    print("-" * 25)
    for strength in explanation['strengths']:
        print(f"✅ {strength}")
    
    print("\nWhat This Model DOES NOT Do:")
    print("-" * 30)
    for limitation in explanation['limitations']:
        print(f"❌ {limitation}")
    
    print("\nHonest Assessment:")
    print("-" * 20)
    print("• This is a literature-based calculator, NOT a machine learning model")
    print("• No synthetic training data or artificial neural networks")
    print("• Coefficients come directly from peer-reviewed studies")
    print("• Transparent and interpretable by design")
    print("• Requires validation on local institutional data before clinical use")
    print("• Should be used as decision support, not replacement for clinical judgment")

def main():
    """Run complete honest demonstration"""
    
    print("📚 SalivAI - Literature-Based Salivary Gland Malignancy Predictor")
    print("Evidence-Based Clinical Decision Support Tool")
    print("Honest implementation using only validated literature coefficients")
    print("=" * 75)
    
    # Run all demonstrations
    demo_individual_predictions()
    demo_literature_foundation()
    demo_feature_importance()
    demo_batch_analysis()
    demo_model_transparency()
    demo_honest_limitations()
    
    print("\n\n🎉 Honest Demo Complete!")
    print("=" * 75)
    print("Key outputs generated:")
    print("- literature_feature_importance.png: Risk factor importance visualization")
    print("- literature_batch_analysis_results.csv: Batch analysis results")
    print()
    print("To run the web application:")
    print("streamlit run app.py")
    print()
    print("This tool provides:")
    print("✅ Evidence-based risk assessment using validated literature")
    print("✅ Transparent calculations with full interpretability")
    print("✅ Immediate clinical utility without requiring training data")
    print("✅ Honest limitations and appropriate clinical context")

if __name__ == "__main__":
    main() 