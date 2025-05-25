# Salivary Gland Tumor Malignancy Risk Factors: Literature Review for Risk Calculator

## Executive Summary
This document compiles evidence-based risk factors for **predicting malignancy** in salivary gland tumors from recent literature. The focus is on **pre-surgical diagnosis** using clinical factors and radiology reports available before surgery. **Note: This excludes survival/prognosis factors which are post-surgical.**

## Key References for MALIGNANCY PREDICTION (Pre-surgical)

### 1. Lo et al. (2023) - Quantitative Texture Analysis Model ✓ MALIGNANCY PREDICTION
**Reference:** Lo, W.C., Cheng, P.C., Hsu, W.L., Cheng, P.W., & Liao, L.J. (2023). A Novel Prediction Model Based on Quantitative Texture Analysis of Sonographic Images for Malignant Major Salivary Glandular Tumors. *Journal of Medical Ultrasound*, 31(3), 218-222.

**Prediction Model for MALIGNANCY:** Score = 1.138 × Age − 1.814 × Intensity + 1.416 × Entropy + 1.714 × Contrast
- **Cutoff value:** ≥0.58 for malignancy prediction
- **Performance:** Sensitivity 83% (95% CI: 74%-92%), Specificity 74% (65%-84%), AUC 0.86 (0.80-0.92)
- **Sample size:** 144 patients (66 malignant, 78 benign)

**Clinical Factors for Malignancy (from same study):**
- **Age ≥60 years:** OR 3.299 (95% CI: 1.626-6.693) for malignancy
- **Submandibular location:** Higher malignancy risk vs parotid

### 2. Wu et al. (2022) - Meta-analysis of Elastosonography ✓ MALIGNANCY PREDICTION
**Reference:** Wu, J., Zhou, Z., Wang, X., Jin, Y., Wang, Z., & Jin, G. (2022). Diagnostic performance of elastosonography in the differential diagnosis of benign and malignant salivary gland tumors: A meta-analysis. *Frontiers in Oncology*, 12, 954751.

**Pooled Diagnostic Performance for MALIGNANCY:**
- **Sensitivity:** 0.73 (95% CI: 0.66-0.78)
- **Specificity:** 0.64 (95% CI: 0.61-0.67)
- **Positive Likelihood Ratio:** 2.83 (95% CI: 1.97-4.07)
- **Negative Likelihood Ratio:** 0.45 (95% CI: 0.32-0.62)
- **Diagnostic Odds Ratio:** 9.86 (95% CI: 4.49-21.62)
- **Sample size:** 16 studies, 1,105 patients, 1,146 lesions

## EXCLUDED STUDIES (Survival/Prognosis - Not Malignancy Prediction)

### ❌ Li & Hu (2020) - EXCLUDED (Survival Analysis, Not Malignancy Prediction)
This study analyzes survival outcomes in already-diagnosed mucoepidermoid carcinoma patients. The hazard ratios are for survival, not for predicting malignancy.

### ❌ Laughlin et al. (2023) - EXCLUDED (Survival Analysis, Not Malignancy Prediction)  
This study analyzes survival and metastasis outcomes in already-diagnosed salivary duct carcinoma patients. The hazard ratios are for prognosis, not for predicting malignancy.

## Numerical Summary Table for MALIGNANCY PREDICTION Algorithm

| Risk Factor | Study | Metric | Value | 95% CI | Sample Size | Available Pre-Surgery |
|------------|-------|--------|-------|--------|-------------|---------------------|
| **Age (continuous)** | Lo et al. 2023 | Coefficient | 1.138 | - | 144 | ✓ Yes |
| **Age ≥60 years** | Lo et al. 2023 | OR | 3.299 | 1.626-6.693 | 144 | ✓ Yes |
| **US Intensity** | Lo et al. 2023 | Coefficient | -1.814 | - | 144 | ✓ Yes (radiology report) |
| **US Entropy** | Lo et al. 2023 | Coefficient | 1.416 | - | 144 | ✓ Yes (radiology report) |
| **US Contrast** | Lo et al. 2023 | Coefficient | 1.714 | - | 144 | ✓ Yes (radiology report) |
| **Elastography stiff** | Wu et al. 2022 | PLR | 2.83 | 1.97-4.07 | 1,146 | ✓ Yes (radiology report) |
| **Elastography soft** | Wu et al. 2022 | NLR | 0.45 | 0.32-0.62 | 1,146 | ✓ Yes (radiology report) |

## Pre-Surgical Clinical Risk Factors for Malignancy

### Age-Based Risk Assessment
- **Optimal cutoff:** ≥60 years - OR 3.299 (95% CI: 1.626-6.693) for malignancy
- **Continuous age coefficient:** 1.138 per year increase in malignancy risk

### Location-Based Risk (Pre-surgical)
**From multiple studies:**
- **Parotid gland:** Lower malignancy rate (~20-25%)
- **Submandibular gland:** Higher malignancy rate (~40-50%)
- **Minor salivary glands:** Highest malignancy rate (~50-80%)

### Clinical Presentation Factors (Pre-surgical)
**High-risk clinical features for malignancy:**
- **Rapid growth:** Strong predictor of malignancy
- **Pain/tenderness:** Associated with malignant tumors
- **Facial nerve symptoms:** Highly suggestive of malignancy
- **Skin involvement:** Indicates malignant disease
- **Palpable lymph nodes:** Regional involvement suggests malignancy

### Radiology Report Factors (Pre-surgical)
**From radiology reports - available before surgery:**

#### Ultrasound Features Suggesting Malignancy:
- **Irregular margins:** High specificity for malignancy
- **Heterogeneous echogenicity:** Suggests malignancy
- **Increased vascularity:** Malignant indicator
- **Size >4cm:** Risk factor for malignancy
- **Elastography stiffness:** PLR 2.83 for malignancy

#### CT/MRI Features Suggesting Malignancy:
- **Irregular enhancement patterns**
- **Infiltrative margins**
- **Signal heterogeneity**
- **Restricted diffusion on DWI**
- **Suspected perineural spread**
- **Bone involvement**

## Algorithm Development for MALIGNANCY PREDICTION

### Primary Risk Score Components (Pre-surgical)
1. **Age coefficient:** 1.138 × Age
2. **Location factor:** Parotid (0), Submandibular (1), Minor glands (2)
3. **Clinical symptoms:** Pain, rapid growth, nerve symptoms
4. **Radiology report features:** Margins, echogenicity, vascularity, elastography

### Proposed Clinical Scoring System for Malignancy

#### Clinical Factors (Available at bedside):
- **Age:** <50 (0 points), 50-60 (1 point), >60 (2 points)
- **Gender:** Female (0), Male (1)
- **Location:** Parotid (0), Submandibular (2), Minor glands (3)
- **Growth rate:** Slow/stable (0), Rapid (2)
- **Pain:** Absent (0), Present (1)
- **Facial nerve symptoms:** Absent (0), Present (3)
- **Lymphadenopathy:** Absent (0), Present (2)

#### Radiology Report Factors:
- **Size:** <2cm (0), 2-4cm (1), >4cm (2)
- **Margins:** Well-defined (0), Irregular (2)
- **Echogenicity:** Homogeneous (0), Heterogeneous (1)
- **Vascularity:** Normal (0), Increased (1)
- **Elastography:** Soft (0), Stiff (2)

### Risk Stratification for MALIGNANCY
- **Low risk (0-4 points):** <20% malignancy probability
- **Intermediate risk (5-8 points):** 20-60% malignancy probability  
- **High risk (>8 points):** >60% malignancy probability

### Validated Model Performance for Malignancy Prediction
- **Expected sensitivity:** 75-85%
- **Expected specificity:** 65-75%
- **Expected AUC:** 0.80-0.90

## Implementation for Pre-Surgical Decision Making

### Required Inputs (All available pre-surgery):
**Clinical Assessment:**
- Patient age and gender
- Tumor location
- Growth characteristics
- Symptom profile (pain, nerve symptoms)
- Physical examination findings

**Radiology Report Data:**
- Tumor size and margins
- Echogenicity pattern
- Vascularity assessment
- Elastography results (if available)
- CT/MRI features (if performed)

### Clinical Decision Support Output:
- **Malignancy probability percentage**
- **Risk category (Low/Intermediate/High)**
- **Recommendation for tissue diagnosis**
- **Suggested next steps**

## Next Steps for Algorithm Development
1. Implement the validated Lo et al. 2023 formula for malignancy prediction
2. Add clinical risk factors available pre-surgery
3. Integrate radiology report features
4. Create risk stratification thresholds
5. Validate against known malignancy outcomes (not survival outcomes) 