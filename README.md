# Diabetes Prediction using Machine Learning

## Project Overview

This project predicts whether a person is diabetic or non-diabetic based on various medical attributes using Machine Learning techniques. The model is trained on the Pima Indians Diabetes Dataset and uses data preprocessing, feature scaling, train-test splitting, and classification algorithms to make predictions.

The goal of this project is to demonstrate the complete Machine Learning workflow, from data collection and preprocessing to model training, evaluation, and prediction.

---

## Objectives

* Analyze diabetes-related health data.
* Preprocess and clean the dataset.
* Train a Machine Learning model for classification.
* Evaluate model performance using accuracy metrics.
* Predict diabetes status for new patient data.

---

##  Dataset Information

The dataset contains the following features:

| Feature                  | Description                                      |
| ------------------------ | ------------------------------------------------ |
| Pregnancies              | Number of pregnancies                            |
| Glucose                  | Plasma glucose concentration                     |
| BloodPressure            | Diastolic blood pressure                         |
| SkinThickness            | Triceps skin fold thickness                      |
| Insulin                  | 2-Hour serum insulin                             |
| BMI                      | Body Mass Index                                  |
| DiabetesPedigreeFunction | Diabetes pedigree function                       |
| Age                      | Age of the patient                               |
| Outcome                  | Target Variable (0 = Non-Diabetic, 1 = Diabetic) |

Dataset Size:

* Total Records: 768
* Features: 8
* Target Variable: Outcome

---

##  Technologies Used

* Python
* NumPy
* Pandas
* Scikit-Learn
* StandardScaler
* Logistic Regression
* VS Code

---

##  Machine Learning Workflow

### 1. Data Collection

* Load diabetes dataset using Pandas.

### 2. Data Exploration

* Analyze dataset shape and structure.
* Check feature distributions and target classes.

### 3. Data Preprocessing

* Separate features and target variable.
* Standardize feature values using StandardScaler.

### 4. Data Splitting

* Split dataset into training and testing sets.

### 5. Model Training

* Train Logistic Regression model using training data.

### 6. Model Evaluation

* Calculate training accuracy.
* Calculate testing accuracy.

### 7. Prediction System

* Accept patient medical data.
* Predict whether the patient is diabetic or non-diabetic.

---

##  Model Performance

Training Accuracy: ~78%

Testing Accuracy: ~77%

Note: Accuracy may vary slightly due to random train-test splits.

---

##  How to Run the Project

### Clone Repository

```bash
git clone https://github.com/ARUNAT007/Diabetes-Prediction.git
```

### Navigate to Project Folder

```bash
cd Diabetes-Prediction
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Project

```bash
python Diabetes_prediction.py
```

---

##  Project Structure

```text
Diabetes-Prediction/
│
├── Diabetes_prediction.py
├── diabetes.csv
├── README.md
├── requirements.txt
└── .gitignore
```

---

##  Future Enhancements

* Build a Streamlit Web Application.
* Compare multiple ML algorithms.
* Perform feature engineering.
* Deploy the model to the cloud.
* Add interactive visualizations and dashboards.

---

##  Learning Outcomes

Through this project, I learned:

* Data preprocessing techniques
* Feature scaling
* Train-test splitting
* Machine Learning model training
* Model evaluation
* Prediction system development
* Git and GitHub project management

---

GitHub: https://github.com/ARUNAT007
