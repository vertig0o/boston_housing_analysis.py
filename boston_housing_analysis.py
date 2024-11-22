import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression

# 1. Veri Setinin Yüklenmesi
url = "https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv"
data = pd.read_csv(url)
print("İlk 5 Satır:\n", data.head())

# 2. Eksik Değer Kontrolü
print("\nEksik Değerler:\n", data.isnull().sum())

# 3. Outlier Analizi (Bağımlı Değişken)
plt.figure(figsize=(12, 6))
sns.boxplot(data=data['medv'])
plt.title('Outliers in Target Variable (medv)')
plt.savefig("outliers_visualization.png")
plt.show()

# 4. Outlier Temizliği
Q1 = data['medv'].quantile(0.25)
Q3 = data['medv'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print(f"\nIQR: {IQR}, Lower Bound: {lower_bound}, Upper Bound: {upper_bound}")

# Outlier'ları kaldırıyoruz
data = data[(data['medv'] > lower_bound) & (data['medv'] < upper_bound)]
print(f"\nOutlier'lar temizlendikten sonra veri seti boyutu: {data.shape}")

# 5. Veri Setini Bağımlı ve Bağımsız Değişkenlere Ayırma
X = data.drop(columns=['medv'])
y = data['medv']

# 6. Veri Setini Bölme (Train-Validation-Test)
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# 7. Model Eğitimi ve Performans Karşılaştırması
models = {
    "Linear Regression": LinearRegression(),
    "Random Forest": RandomForestRegressor(random_state=42)
}

results = {}

for name, model in models.items():
    model.fit(X_train, y_train)
    preds = model.predict(X_val)
    rmse = np.sqrt(mean_squared_error(y_val, preds))
    results[name] = rmse

# 8. En İyi Modelin Seçimi
best_model_name = min(results, key=results.get)
print(f"\nBest Model: {best_model_name} with RMSE: {results[best_model_name]}")

# 9. Test Seti Üzerinde Performans
best_model = models[best_model_name]
test_preds = best_model.predict(X_test)
test_rmse = np.sqrt(mean_squared_error(y_test, test_preds))
print(f"Test RMSE for Best Model ({best_model_name}): {test_rmse}")

# 10. Feature Importance (Eğer Random Forest en iyi modelse)
if best_model_name == "Random Forest":
    feature_importances = best_model.feature_importances_
    importance_df = pd.DataFrame({
        'Feature': X.columns,
        'Importance': feature_importances
    }).sort_values(by='Importance', ascending=False)
    print("\nFeature Importances:\n", importance_df)

    # Görselleştirme
    importance_df.plot(kind='bar', x='Feature', y='Importance', title='Feature Importances', legend=False)
    plt.savefig("feature_importances.png")
    plt.show()

# Tüm çıktılar ve grafikler proje dosyasına kaydedilecek.
