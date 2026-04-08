# 🌲 EcoType: Forest Cover Type Prediction Using Machine Learning

## 📌 Project Overview
EcoType is a machine learning application that predicts the **forest cover type** of a geographical area using cartographic and environmental features such as elevation, slope, soil type, and hydrological distances.

This project helps in:
- 🌍 Environmental monitoring  
- 🌲 Forestry management  
- 🗺 Land-use planning  

---

## 📊 Dataset Details

- **Size:** 145,890 rows × 13 columns  
- **Target Variable:** `Cover_Type` (7 classes)

### 🔹 Key Features
- Elevation  
- Aspect  
- Slope  
- Distance to Hydrology  
- Distance to Roadways  
- Hillshade indices  
- Soil Type  
- Wilderness Area  

---

## ⚙️ Workflow

### 1️⃣ Data Preprocessing
- Handled missing values (median imputation)
- Removed inconsistencies (inf, NaN)
- Feature scaling & transformation

---

### 2️⃣ Feature Engineering
Created new features:
- Hydrology Ratio  
- Road-Fire Ratio  
- Hillshade Differences  
- Elevation × Slope  

---

### 3️⃣ Exploratory Data Analysis (EDA)
- Distribution plots  
- Class imbalance analysis  
- Correlation heatmaps  

---

### 4️⃣ Class Imbalance Handling
- Applied **SMOTE** to balance dataset  

---

### 5️⃣ Model Building
Trained multiple models:
- Random Forest 🌲  
- Decision Tree  
- Logistic Regression  
- KNN  
- XGBoost  

---

### 🏆 Best Model
**Random Forest Classifier** performed best with high accuracy and stability.

---

### 🔧 Hyperparameter Optimization
- Used optimized parameters for better generalization

---

## 📈 Model Performance
- Evaluated using:
  - Accuracy  
  - Confusion Matrix  
  - Classification Report  

---

## 🚀 Deployment

### 🔹 Streamlit Web App
An interactive UI allows users to:
- Input environmental parameters  
- Get real-time forest cover predictions  

👉 **Live App:** https://ecotype-forest-cover-type-prediction-using-machine-learning-el.streamlit.app/

---

## 🧠 Tech Stack

- Python 🐍  
- Pandas & NumPy  
- Scikit-learn  
- XGBoost  
- Imbalanced-learn  
- Streamlit  

---
EcoType-App/
│── app.py
│── requirements.txt
│── README.md
---

## 💡 Key Highlights

- End-to-end ML pipeline  
- Feature engineering for better accuracy  
- Class imbalance handling using SMOTE  
- Deployment-ready model  
- Live web application  

---

## 🔮 Future Improvements

- Add map-based visualization  
- Improve UI/UX design  
- Deploy using Docker  
- Add real-time GIS integration  

---

## 👨‍💻 Author

**Naveen Kumar**

---
