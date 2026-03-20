import joblib
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import pandas as pd


def base(data):
    num = data['num']
    x = [[1], [2], [3]]
    y = [2, 4, 6]

    model = LinearRegression()
    model.fit(x, y)

    result = model.predict([[num]])
    return round(result[0],2)

def diabetes(data):
    age = data['age']
    sugar = data['sugar']
    data = {
        "age": [25, 45, 35, 50, 23, 40],
        "sugar": [90, 180, 120, 200, 85, 160],
        "diabetic": [0, 1, 0, 1, 0, 1]
    }
    df = pd.DataFrame(data)
    
    x = df[['age','sugar']]
    y = df['diabetic']
    
    model = LogisticRegression()
    model.fit(x, y)
    
    input_df = pd.DataFrame([[age, sugar]], columns=['age', 'sugar'])
    result = model.predict(input_df)
    
    return int(result[0])
    

def practice():
    data = {
    "bills": [
        {"bill_id": "B001", "total": 500, "due_days": 0, "status": "paid"},
        {"bill_id": "B002", "total": 2000, "due_days": 10, "status": "unpaid"},
        {"bill_id": "B003", "total": 1500, "due_days": 5, "status": "paid"},
        {"bill_id": "B004", "total": 3000, "due_days": 20, "status": "unpaid"},
        {"bill_id": "B005", "total": 700, "due_days": 0, "status": "paid"}
    ]
    }
    
    df = pd.DataFrame(data["bills"])

    df['paid'] = df['status'].apply(lambda x: 1 if x=='paid' else 0)
    
    x = df[['total', 'due_days']]
    y = df['paid']
    
    model = LogisticRegression()
    model.fit(x, y)
    
    new_bill = pd.DataFrame([[1500, 5]], columns=['total', 'due_days'])
    result = model.predict(new_bill)
    
    return int(result[0])


def sample():
    data = {
        "amount": [500, 700, 900, 1200, 1500, 1800, 2000, 2200, 2500, 3000],
        "days":   [0,   1,   2,   3,    5,    8,   10,   12,   15,   20],
        "paid":   [1,   1,   1,   1,    1,    0,    0,    0,    0,    0]
    }
    
    df = pd.DataFrame(data)

    X = df[['amount','days']]
    Y = df['paid']

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)
    
    scaler = StandardScaler() 
    x_train = scaler.fit_transform(X_train) 
    x_test = scaler.transform(X_test)
    
    model = LogisticRegression()
    model.fit(x_train, Y_train)
    y_pred = model.predict(x_test)
    
    acc = accuracy_score(Y_test, y_pred)

    print("X_test:\n", X_test)
    print("Actual (Y_test):", list(Y_test))
    print("Predicted:", list(y_pred))
    print("Accuracy:", acc)

    new_data = [[1800, 2]]
    new_pred = model.predict(new_data)

    print("New Prediction (1800,2):", int(new_pred[0]))
    return int(new_pred[0])