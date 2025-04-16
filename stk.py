stack_reg = StackingRegressor(
    estimators=[
        ('rf', RandomForestRegressor()),
        ('xgb', XGBRegressor()),
        ('ada', AdaBoostRegressor())
    ],
    final_estimator=LinearRegression(),
    passthrough=True
)
stack_reg.fit(X_reg_train_fs, y_reg_train)
stack_preds = stack_reg.predict(X_reg_test_fs)
mae = mean_absolute_error(y_reg_test, stack_preds)
rmse = np.sqrt(mean_squared_error(y_reg_test, stack_preds))
r2 = r2_score(y_reg_test, stack_preds)
print(f"Stacked Ensemble: MAE = {mae:.2f}, RMSE = {rmse:.2f}, R² = {r2:.4f}")
