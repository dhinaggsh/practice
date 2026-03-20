data = [
{"age":25,"experience":3,"education":2,"skill_score":7,"salary":56000},
{"age":30,"experience":8,"education":1,"skill_score":6,"salary":62000},
{"age":40,"experience":18,"education":3,"skill_score":9,"salary":120000},
{"age":28,"experience":6,"education":2,"skill_score":5,"salary":58000},
{"age":35,"experience":13,"education":1,"skill_score":8,"salary":85000},
{"age":22,"experience":0,"education":1,"skill_score":4,"salary":30000},
{"age":27,"experience":5,"education":2,"skill_score":6,"salary":60000},
{"age":45,"experience":23,"education":3,"skill_score":9,"salary":135000},
{"age":32,"experience":10,"education":2,"skill_score":7,"salary":80000},
{"age":29,"experience":7,"education":1,"skill_score":5,"salary":55000},

{"age":26,"experience":4,"education":2,"skill_score":6,"salary":58000},
{"age":38,"experience":16,"education":3,"skill_score":8,"salary":110000},
{"age":31,"experience":9,"education":1,"skill_score":7,"salary":70000},
{"age":24,"experience":2,"education":1,"skill_score":5,"salary":40000},
{"age":36,"experience":14,"education":2,"skill_score":8,"salary":90000},
{"age":42,"experience":20,"education":3,"skill_score":9,"salary":130000},
{"age":33,"experience":11,"education":2,"skill_score":7,"salary":82000},
{"age":28,"experience":6,"education":1,"skill_score":6,"salary":60000},
{"age":39,"experience":17,"education":3,"skill_score":8,"salary":115000},
{"age":23,"experience":1,"education":1,"skill_score":4,"salary":32000},

{"age":41,"experience":19,"education":3,"skill_score":9,"salary":128000},
{"age":34,"experience":12,"education":2,"skill_score":7,"salary":85000},
{"age":27,"experience":5,"education":1,"skill_score":6,"salary":58000},
{"age":37,"experience":15,"education":2,"skill_score":8,"salary":92000},
{"age":44,"experience":22,"education":3,"skill_score":9,"salary":132000},
{"age":21,"experience":0,"education":1,"skill_score":3,"salary":28000},
{"age":29,"experience":7,"education":2,"skill_score":6,"salary":65000},
{"age":35,"experience":13,"education":2,"skill_score":7,"salary":88000},
{"age":48,"experience":26,"education":3,"skill_score":10,"salary":140000},
{"age":30,"experience":8,"education":1,"skill_score":5,"salary":60000},

{"age":26,"experience":4,"education":1,"skill_score":5,"salary":50000},
{"age":38,"experience":16,"education":2,"skill_score":8,"salary":95000},
{"age":32,"experience":10,"education":1,"skill_score":6,"salary":72000},
{"age":25,"experience":3,"education":2,"skill_score":7,"salary":57000},
{"age":40,"experience":18,"education":3,"skill_score":9,"salary":125000},
{"age":28,"experience":6,"education":1,"skill_score":6,"salary":61000},
{"age":36,"experience":14,"education":2,"skill_score":8,"salary":90000},
{"age":43,"experience":21,"education":3,"skill_score":9,"salary":130000},
{"age":31,"experience":9,"education":2,"skill_score":7,"salary":78000},
{"age":27,"experience":5,"education":1,"skill_score":5,"salary":55000},

{"age":39,"experience":17,"education":3,"skill_score":8,"salary":112000},
{"age":22,"experience":0,"education":1,"skill_score":4,"salary":30000},
{"age":33,"experience":11,"education":2,"skill_score":7,"salary":82000},
{"age":45,"experience":23,"education":3,"skill_score":9,"salary":135000},
{"age":29,"experience":7,"education":1,"skill_score":6,"salary":60000},
{"age":34,"experience":12,"education":2,"skill_score":7,"salary":85000},
{"age":41,"experience":19,"education":3,"skill_score":9,"salary":128000},
{"age":26,"experience":4,"education":1,"skill_score":5,"salary":52000},
{"age":37,"experience":15,"education":2,"skill_score":8,"salary":92000},
{"age":30,"experience":8,"education":2,"skill_score":6,"salary":70000},

{"age":28,"experience":6,"education":1,"skill_score":5,"salary":60000},
{"age":42,"experience":20,"education":3,"skill_score":9,"salary":130000},
{"age":35,"experience":13,"education":2,"skill_score":7,"salary":88000},
{"age":24,"experience":2,"education":1,"skill_score":4,"salary":38000},
{"age":38,"experience":16,"education":3,"skill_score":8,"salary":110000},
{"age":31,"experience":9,"education":2,"skill_score":7,"salary":78000},
{"age":27,"experience":5,"education":1,"skill_score":6,"salary":58000},
{"age":44,"experience":22,"education":3,"skill_score":9,"salary":132000},
{"age":33,"experience":11,"education":2,"skill_score":7,"salary":82000},
{"age":29,"experience":7,"education":1,"skill_score":5,"salary":55000},

{"age":36,"experience":14,"education":2,"skill_score":8,"salary":90000},
{"age":40,"experience":18,"education":3,"skill_score":9,"salary":125000},
{"age":26,"experience":4,"education":1,"skill_score":5,"salary":52000},
{"age":32,"experience":10,"education":2,"skill_score":7,"salary":80000},
{"age":23,"experience":1,"education":1,"skill_score":4,"salary":32000},
{"age":39,"experience":17,"education":3,"skill_score":8,"salary":115000},
{"age":28,"experience":6,"education":1,"skill_score":6,"salary":61000},
{"age":35,"experience":13,"education":2,"skill_score":7,"salary":88000},
{"age":47,"experience":25,"education":3,"skill_score":10,"salary":138000},
{"age":30,"experience":8,"education":1,"skill_score":6,"salary":62000}
]

import pandas as pd
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# from sklearn.ensemble import RandomForestRegressor

def learning_ml():
    
    # Random Forest Regressor is best for these complex data
    df = pd.DataFrame(data)
    
    x = df[['age', 'experience', 'education', 'skill_score']]
    y= df['salary']
    
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
    
    # model = RandomForestRegressor()
    model = LinearRegression()
    model.fit(x_train, y_train)
    
    y_pred = model.predict(x_test)
    
    accuracy = r2_score(y_pred, y_test)
    
    print(y_test)
    print(y_pred)
    print(float(accuracy))
    
    new_data = pd.DataFrame([[22, 1, 2, 5]], columns=['age', 'experience', 'education', 'skill_score'])
    pre = model.predict(new_data)
    print(pre)
    
    return int(pre[0])

# Machine Learning is a Concept of AI
# It's used to learn past data and predict new data automatically
    
