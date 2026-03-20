import requests
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score

def url_ml():
    url = "https://dummyjson.com/users"

    request = requests.get(url=url)
    resp = request.json()['users']

    df = pd.DataFrame(resp)
    df['seniors'] = df['age'].apply(lambda x:1 if x>30 else 0)
    
    # New column add we can use and & condition also
    # df['high_value_user'] = (
    #     (df['age'] > 30) & (df['weight'] > 70)
    # ).astype(int)
    
    
    x = df[['age', 'height', 'weight']]
    y = df['seniors']
    
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.5,random_state=42)
    
    model = LogisticRegression()
    model.fit(x_train, y_train)
    
    y_pred = model.predict(x_test)

    acc = accuracy_score(y_pred, y_test)
    
    print(y_pred)
    print(y_test)
    print(acc)
    
    # new_data = pd.DataFrame([35], columns=['age'])
    # new_data = pd.DataFrame([25], columns=['age'])
    # new_data = pd.DataFrame([40], columns=['age'])
    # new_data = pd.DataFrame([32], columns=['age'])
    # new_data = pd.DataFrame([22], columns=['age'])
    new_data = pd.DataFrame({
        'age': [35, 25, 40, 32, 22],
        'height': [175, 168, 180, 172, 165],
        'weight': [75, 60, 85, 70, 55]
    })  
    print(model.predict(new_data))
    
    # instead of split we can use cross validation
    scores = cross_val_score(model, x, y, cv=5)
    print(scores)
    print("Average accuracy:", scores.mean())
    
    return acc