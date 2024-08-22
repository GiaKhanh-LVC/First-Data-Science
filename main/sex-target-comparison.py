import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv(r"D:/Heart-Disease-Dataset-first-Data-Science/main/heart.csv")
sex_target_compare=data.groupby(['sex','target']).size().unstack(fill_value=0)
ax=sex_target_compare.plot(kind="bar",color=['skyblue', 'salmon'])
plt.title("Comparison of Sex and Heart Disease")
plt.xlabel("Sex")
plt.ylabel("Number of Individuals")
ax.set_xticklabels(["Female","Male"], rotation=0)
plt.legend(["No Heart Disease", "Heart Disease"])
for i in ax.containers:
    ax.bar_label(i, label_type='edge', fontsize=12, color='black')
plt.tight_layout()
plt.show()