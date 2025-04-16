import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from xgboost import XGBClassifier, XGBRegressor
from sklearn.metrics import accuracy_score, f1_score, mean_squared_error, r2_score


df = pd.read_csv('C:/Users/LENOVO/Downloads/updated_health_insurance_dataset.csv')


if 'Person_ID' in df.columns:
    df.drop(['Person_ID'], axis=1, inplace=True)


categorical_cols = df.select_dtypes(include='object').columns.tolist()

le = LabelEncoder()
for col in categorical_cols:
    df[col] = le.fit_transform(df[col])


scaler = StandardScaler()
features = df.drop(columns=['Insurance Type', 'Annual Premium (USD)'])  # ✅ 
X_scaled = scaler.fit_transform(features)


X_cls = X_scaled
y_cls = df['Insurance Type']


X_train_cls, X_test_cls, y_train_cls, y_test_cls = train_test_split(X_cls, y_cls, test_size=0.2, random_state=42)


selector_cls = SelectFromModel(RandomForestClassifier(n_estimators=100, random_state=42))
selector_cls.fit(X_train_cls, y_train_cls)
X_train_fs_cls = selector_cls.transform(X_train_cls)
X_test_fs_cls = selector_cls.transform(X_test_cls)


model_cls = XGBClassifier(eval_metric='mlogloss')
model_cls.fit(X_train_fs_cls, y_train_cls)
y_pred_cls = model_cls.predict(X_test_fs_cls)


print("🎯 Classification Results:")
print("Accuracy:", accuracy_score(y_test_cls, y_pred_cls))
print("F1 Score:", f1_score(y_test_cls, y_pred_cls, average='weighted'))



X_reg = X_scaled
y_reg = df['Annual Premium (USD)']


X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)


selector_reg = SelectFromModel(RandomForestRegressor(n_estimators=100, random_state=42))
selector_reg.fit(X_train_reg, y_train_reg)
X_train_fs_reg = selector_reg.transform(X_train_reg)
X_test_fs_reg = selector_reg.transform(X_test_reg)


model_reg = XGBRegressor()
model_reg.fit(X_train_fs_reg, y_train_reg)
y_pred_reg = model_reg.predict(X_test_fs_reg)


print("\n📈 Regression Results:")
print("RMSE:", mean_squared_error(y_test_reg, y_pred_reg, squared=False))
print("R² Score:", r2_score(y_test_reg, y_pred_reg))
