X_reg = df.drop(columns=['Annual Premium (USD)', 'Insurance Type'])
y_reg = df['Annual Premium (USD)']
X_reg_train, X_reg_test, y_reg_train, y_reg_test = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

selector_reg = SelectFromModel(RandomForestRegressor(random_state=42)).fit(X_reg_train, y_reg_train)
X_reg_train_fs = selector_reg.transform(X_reg_train)
X_reg_test_fs = selector_reg.transform(X_reg_test)

models_reg = {
    "Decision Tree": DecisionTreeRegressor(),
    "Random Forest": RandomForestRegressor(),
    "AdaBoost": AdaBoostRegressor(),
    "XGBoost": XGBRegressor()
}

print("\\n📈 Regression Results (with Feature Selection):")
for name, model in models_reg.items():
    model.fit(X_reg_train_fs, y_reg_train)
    preds = model.predict(X_reg_test_fs)
    mae = mean_absolute_error(y_reg_test, preds)
    rmse = np.sqrt(mean_squared_error(y_reg_test, preds))
    r2 = r2_score(y_reg_test, preds)
    print(f"{name}: MAE = {mae:.2f}, RMSE = {rmse:.2f}, R² = {r2:.4f}")
