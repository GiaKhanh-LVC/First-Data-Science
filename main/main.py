import pandas as pd
import matplotlib.pyplot as plt
row=0
data = pd.read_csv(r"D:/Heart-Disease-Dataset-first-Data-Science/main/heart.csv")
categories=['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal','target']
values=[
    data.loc[row, 'age'],       # Age of the patient
    data.loc[row, 'sex'],       # Sex (1 = male; 0 = female)
    data.loc[row, 'cp'],        # Chest pain type
    data.loc[row, 'trestbps'],  # Resting blood pressure
    data.loc[row, 'chol'],      # Serum cholesterol
    data.loc[row, 'fbs'],       # Fasting blood sugar > 120 mg/dl (1 = true; 0 = false)
    data.loc[row, 'restecg'],   # Resting electrocardiographic results
    data.loc[row, 'thalach'],   # Maximum heart rate achieved
    data.loc[row, 'exang'],     # Exercise induced angina (1 = yes; 0 = no)
    data.loc[row, 'oldpeak'],   # ST depression induced by exercise relative to rest
    data.loc[row, 'slope'],     # Slope of the peak exercise ST segment
    data.loc[row, 'ca'],        # Number of major vessels (0-3) colored by fluoroscopy
    data.loc[row, 'thal'],      # Thalassemia (3 = normal; 6 = fixed defect; 7 = reversible defect)
    data.loc[row, 'target']     # Target variable (1 = heart disease; 0 = no heart disease)
]
plt.bar(categories, values, color='skyblue', edgecolor='black')
plt.title("Heart Disease Dataset")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()