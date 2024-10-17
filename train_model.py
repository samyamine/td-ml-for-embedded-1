def build_model():
    import pandas as pd 
    from sklearn.linear_model import LinearRegression
    import joblib
    df = pd.read_csv('houses.csv')
    X = df[['size', 'nb_rooms', 'garden']]
    y = df['price']
    model = LinearRegression()
    model.fit(X, y)
    joblib.dump(model, "regression.joblib")
    
build_model()