# AI-Powered Drug Absorption Prediction

## Project Overview

This project demonstrates an end-to-end QSAR workflow for predicting Caco-2 permeability (logPapp) of small molecules using molecular fingerprints, physicochemical descriptors, and machine learning.
### Live Demo
[Streamlit App](https://permeability-prediction-app-upwot5ruaafrrxx5iotxux.streamlit.app/)

The workflow covers data curation, exploratory analysis, molecular representation, model development, validation, applicability domain analysis, explainable AI, and deployment.

## Workflow

### 1. Data Collection and Curation
- Dataset collection
- Duplicate removal
- Missing value handling
- SMILES standardization
- Data quality checks

### 2. Exploratory Data Analysis (EDA)
- Distribution of logPapp values
- Molecular weight distribution
- LogP distribution
- TPSA distribution
- Correlation analysis
- Outlier identification

### 3. Topological Data Analysis (TDA)
- Chemical space visualization
- Molecular diversity assessment
- Structural similarity analysis
- Dataset coverage evaluation

### 4. Molecular Feature Generation

#### Fingerprint-Based Features
- Morgan Fingerprints (2048 bits)

#### Hybrid Features
- Morgan Fingerprints (2048 bits)
- Molecular Weight
- LogP
- TPSA
- HBD
- HBA
- Rotatable Bonds

### 5. Model Development

#### Fingerprint-Only Models
- Random Forest
- XGBoost
- Extra Trees

#### Fingerprint + Descriptor Models
- Random Forest
- XGBoost
- Extra Trees

### 6. Model Comparison
Models compared using:
- R²
- RMSE
- MAE
- Cross-Validation Performance

Comparison of:
- Fingerprints Only
- Fingerprints + RDKit Descriptors

### 7. Validation Strategy
- Train/Test Split
- 5-Fold Cross Validation
- Scaffold Split Validation

### 8. Applicability Domain Analysis
- k-Nearest Neighbors (kNN)
- Distance-based approach
- AD threshold determination
- Confidence estimation

### 9. Explainable AI
- SHAP Analysis
- Feature Importance
- Descriptor Contribution Analysis

### 10. Prediction Pipeline
Input:
- SMILES

Output:
- Predicted logPapp
- Distance from training compounds
- Applicability Domain status
- Prediction confidence

### 11. Deployment
- Streamlit Web Application
- Cloud Deployment
- Mobile Compatible Interface

## Repository Structure

data/
Raw and processed datasets

notebooks/
EDA, TDA, model development and validation notebooks

models/
Trained models and metadata

app/
Streamlit deployment files

## Skills Demonstrated

- Cheminformatics
- QSAR Modeling
- RDKit
- Molecular Fingerprints
- Descriptor Engineering
- Exploratory Data Analysis
- Topological Data Analysis
- Machine Learning
- Explainable AI (SHAP)
- Applicability Domain Analysis
- Model Deployment
- Python Programming
