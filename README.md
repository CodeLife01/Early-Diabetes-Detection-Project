# Early-Diabetes-Detection-Project  

## 📌 Overview  
The **Early Diabetes Detection Project** is a machine learning classification project that aims to predict the likelihood of diabetes at an early stage using patient symptoms and demographic data. The dataset used in this project was collected from Sylhet Diabetes Hospital, Bangladesh, and consists of 520 instances with 16 features.  

## 📊 About the Dataset  
### **Dataset Characteristics:**  
- **Type:** Multivariate  
- **Subject Area:** Computer Science / Healthcare  
- **Associated Task:** Classification  
- **Feature Type:** Categorical, Integer  
- **Number of Instances:** 520  
- **Number of Features:** 16  
- **Missing Values:** Yes  

This dataset comprises information on signs and symptoms of newly diagnosed diabetic patients or individuals at risk. The data was gathered via direct questionnaires and validated by medical professionals.  

### **Reference Paper:**  
*"Likelihood Prediction of Diabetes at Early Stage Using Data Mining Techniques"*  
Authors: M. M. F. Islam, Rahatara Ferdousi, Sadikur Rahman, Humayra Yasmin Bushra  
Published in: *Computer Vision and Machine Intelligence in Medical Image Analysis (2019)*  

## 📑 Features and Variables  
| Feature | Type | Description |
|---------|------|-------------|
| `age` | Integer | Age of the patient (20-65 years) |
| `gender` | Categorical | Gender (1 = Male, 2 = Female) |
| `polyuria` | Binary | Excessive urination (1 = Yes, 2 = No) |
| `polydipsia` | Binary | Excessive thirst (1 = Yes, 2 = No) |
| `sudden_weight_loss` | Binary | Sudden weight loss (1 = Yes, 2 = No) |
| `weakness` | Binary | Feeling of weakness (1 = Yes, 2 = No) |
| `polyphagia` | Binary | Excessive hunger (1 = Yes, 2 = No) |
| `genital_thrush` | Binary | Fungal infection (1 = Yes, 2 = No) |
| `visual_blurring` | Binary | Blurry vision (1 = Yes, 2 = No) |
| `itching` | Binary | Experience of itching (1 = Yes, 2 = No) |
| `irritability` | Binary | Irritability (1 = Yes, 2 = No) |
| `delayed_healing` | Binary | Slow wound healing (1 = Yes, 2 = No) |
| `partial_paresis` | Binary | Muscle weakness (1 = Yes, 2 = No) |
| `muscle_stiffness` | Binary | Muscle stiffness (1 = Yes, 2 = No) |
| `alopecia` | Binary | Hair loss (1 = Yes, 2 = No) |
| `obesity` | Binary | Obesity (1 = Yes, 2 = No) |
| `class` | Binary | Diabetes diagnosis (1 = Positive, 2 = Negative) |

## 🚀 Project Goals  
- Develop a **machine learning model** to predict early-stage diabetes risk.  
- Perform **exploratory data analysis (EDA)** to understand feature importance.  
- Implement **data preprocessing**, handling missing values, and feature engineering.  
- Train and evaluate multiple **classification models** (Logistic Regression, Decision Tree, Random Forest, SVM, etc.).  

## 🛠 Installation & Setup  
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/Early-Diabetes-Detection-Project.git
   cd Early-Diabetes-Detection-Project
   ```
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Jupyter Notebook or Python script to train models:  
   ```bash
   jupyter notebook
   ```

## 📌 Usage  
- Load and preprocess the dataset  
- Perform exploratory data analysis (EDA)  
- Train and evaluate machine learning models  
- Visualize model performance  

## 📈 Model Performance  
The project will compare different models based on accuracy, precision, recall, and F1-score. Results and visualizations will be included in the analysis.  

## 🤝 Contribution  
Contributions are welcome! Feel free to:  
- Submit issues  
- Suggest improvements  
- Create pull requests  

## 📜 License  
This project is open-source and available under the **MIT License**.  

## 🏷 Acknowledgments  
Special thanks to the authors of the dataset and research paper for making this valuable dataset publicly available.  

---