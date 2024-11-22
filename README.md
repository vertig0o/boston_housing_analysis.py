# Boston Housing Analysis

## İlk beş Data:
| crim   | zn   | indus | chas | nox   | rm    | age   | dis    | rad | tax  | ptratio | b      | lstat | medv  |
|--------|------|-------|------|-------|-------|-------|--------|-----|------|---------|--------|-------|-------|
| 0.00632 | 18.0 | 2.31  | 0    | 0.538 | 6.575 | 65.2  | 4.0900 | 1   | 296  | 15.3    | 396.90 | 4.98  | 24.0  |
| 0.02731 | 0.0  | 7.07  | 0    | 0.469 | 6.421 | 78.9  | 4.9671 | 2   | 242  | 17.8    | 396.90 | 9.14  | 21.6  |
| 0.02729 | 0.0  | 7.07  | 0    | 0.469 | 7.185 | 61.1  | 4.9671 | 2   | 242  | 17.8    | 392.83 | 4.03  | 34.7  |
| 0.03237 | 0.0  | 2.18  | 0    | 0.458 | 6.998 | 45.8  | 6.0622 | 3   | 222  | 18.7    | 394.63 | 2.94  | 33.4  |
| 0.06905 | 0.0  | 2.18  | 0    | 0.458 | 7.147 | 54.2  | 6.0622 | 3   | 222  | 18.7    | 396.90 | 5.33  | 36.2  |

## Eksik Değerler

Veri setindeki tüm özelliklerde eksik değer bulunmamaktadır:

| Özellik | Eksik Değer |
|---------|-------------|
| crim    | 0           |
| zn      | 0           |
| indus   | 0           |
| chas    | 0           |
| nox     | 0           |
| rm      | 0           |
| age     | 0           |
| dis     | 0           |
| rad     | 0           |
| tax     | 0           |
| ptratio | 0           |
| b       | 0           |
| lstat   | 0           |
| medv    | 0           |

![indir (1)](https://github.com/user-attachments/assets/ec320efa-50a5-4748-b06b-bbf62d77381d)

## Outlier Removal:

- **IQR**: 7.98
- **Lower Bound**: 5.06
- **Upper Bound**: 36.96

Outlier'lar temizlendikten sonra veri seti boyutu: `(466, 14)`.

## Best Model: Random Forest

- **RMSE (Training)**: 2.93
- **RMSE (Test)**: 2.43

## Feature Importances:

| Feature | Importance |
|---------|------------|
| lstat   | 0.520859   |
| rm      | 0.233512   |
| dis     | 0.064071   |
| crim    | 0.043720   |
| nox     | 0.024773   |
| age     | 0.024765   |
| b       | 0.022158   |
| tax     | 0.021205   |
| ptratio | 0.019051   |
| indus   | 0.018391   |
| rad     | 0.004302   |
| zn      | 0.002425   |
| chas    | 0.000768   |


![indir (1)](https://github.com/user-attachments/assets/d005312f-3fcc-45c6-b414-2d61af36ec1a)
