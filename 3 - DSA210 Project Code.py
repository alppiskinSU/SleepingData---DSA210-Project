import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
import statsmodels.api as sm

# 1. Load Data
file_path = "2 - Sleep_Study_Data.xlsx"
data = pd.read_excel(file_path)

# 2. Rename columns
data = data.rename(columns={
    'Sleep Time - (Calculation)': 'SleepHours',
    'Sleep Quality - (1-10)':     'SleepQuality',
    'Study Duration - (Calculation)': 'StudyHours',
    'Study Quality - (1-10)':     'StudyQuality'
})

# 3. Convert date
data['Date'] = pd.to_datetime(data['Date'])

# 4. Prepare a filled version for most analyses
num_cols = ['SleepHours', 'SleepQuality', 'StudyHours', 'StudyQuality']
filled = data.copy()
filled[num_cols] = filled[num_cols].fillna(filled[num_cols].mean())

# —————————————————————————————
# 5. Correlation Matrix
plt.figure(figsize=(10,6))
sns.heatmap(filled[num_cols].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.tight_layout()
plt.show()

# 6. Scatter: Sleep Hours vs Study Hours
plt.figure(figsize=(8,6))
sns.scatterplot(x='SleepHours', y='StudyHours', data=filled)
plt.title('Sleep Duration vs Study Hours')
plt.xlabel('Sleep Duration (Hours)')
plt.ylabel('Study Hours')
plt.tight_layout()
plt.show()

# 7. Scatter: Sleep Quality vs Study Quality
plt.figure(figsize=(8,6))
sns.scatterplot(x='SleepQuality', y='StudyQuality', data=filled)
plt.title('Sleep Quality vs Study Quality')
plt.xlabel('Sleep Quality (1-10)')
plt.ylabel('Study Quality (1-10)')
plt.tight_layout()
plt.show()

# 8. Box Plot: Sleep Quality vs Study Hours
plt.figure(figsize=(8,6))
sns.boxplot(x=filled['SleepQuality'].round().astype(int), y='StudyHours', data=filled)
plt.title('Sleep Quality vs Study Hours')
plt.xlabel('Sleep Quality (1-10)')
plt.ylabel('Study Hours')
plt.tight_layout()
plt.show()

# 9. Histograms
plt.figure(figsize=(8,6))
sns.histplot(filled['SleepHours'], bins=10, kde=True)
plt.title('Distribution of Sleep Hours')
plt.xlabel('Sleep Duration (Hours)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,6))
sns.histplot(filled['StudyHours'], bins=10, kde=True)
plt.title('Distribution of Study Hours')
plt.xlabel('Study Duration (Hours)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# 10. Time Series
ts = data.set_index('Date')[['SleepHours','StudyHours']].sort_index()
full_idx = pd.date_range(ts.index.min(), ts.index.max(), freq='D')
ts_full = ts.reindex(full_idx)

plt.figure(figsize=(12,6))
plt.plot(ts_full.index, ts_full['SleepHours'], marker='o', label='Sleep Hours')
plt.plot(ts_full.index, ts_full['StudyHours'], marker='s', label='Study Hours')
plt.title('Sleep and Study Hours Over Time')
plt.xlabel('Date')
plt.ylabel('Hours')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 11. Correlation & Hypothesis Test
corr, p_value = pearsonr(filled['SleepHours'], filled['StudyHours'])
print(f"Correlation between SleepHours and StudyHours: {corr:.3f}")
print(f"P-Value: {p_value:.3f}")
if p_value < 0.05:
    print("There is a statistically significant relationship.")
else:
    print("There is no statistically significant relationship.")

# 12. Machine Learning Models

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Model 1: SleepQuality → StudyQuality
X1 = filled[['SleepQuality']]
y  = filled['StudyQuality']

model1 = LinearRegression()
model1.fit(X1, y)
y_pred1 = model1.predict(X1)

r2_1  = r2_score(y, y_pred1)
mae_1 = mean_absolute_error(y, y_pred1)
print(f"Model 1 (SleepQuality → StudyQuality): R² = {r2_1:.3f}, MAE = {mae_1:.3f}")

plt.figure(figsize=(8,6))
sns.regplot(
    x='SleepQuality',
    y='StudyQuality',
    data=filled,
    scatter_kws={'s':50},
    line_kws={'color':'red'}
)
plt.title('Model 1: Sleep Quality vs Study Quality')
plt.xlabel('Sleep Quality (1–10)')
plt.ylabel('Study Quality (1–10)')
plt.tight_layout()
plt.savefig('images/model1_sleepquality_studyquality.png')
plt.show()


# Model 2: SleepHours → StudyQuality
X2 = filled[['SleepHours']]

model2 = LinearRegression()
model2.fit(X2, y)
y_pred2 = model2.predict(X2)

r2_2  = r2_score(y, y_pred2)
mae_2 = mean_absolute_error(y, y_pred2)
print(f"Model 2 (SleepHours → StudyQuality): R² = {r2_2:.3f}, MAE = {mae_2:.3f}")

plt.figure(figsize=(8,6))
sns.regplot(
    x='SleepHours',
    y='StudyQuality',
    data=filled,
    scatter_kws={'s':50},
    line_kws={'color':'red'}
)
plt.title('Model 2: Sleep Hours vs Study Quality')
plt.xlabel('Sleep Duration (Hours)')
plt.ylabel('Study Quality (1–10)')
plt.tight_layout()
plt.savefig('images/model2_sleephours_studyquality.png')
plt.show()

