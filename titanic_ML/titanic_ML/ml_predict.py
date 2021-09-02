import pickle
def prediction_model(pclass,sex,age,sibsp,parch,fare,embarked,title):
    x = [[pclass,sex,age,sibsp,parch,fare,embarked,title]] # to make sure it is a correct order
    rf = pickle.load(open('titanic_model.sav','rb'))
    prediction = rf.predict(x)
    if prediction == 0:
        prediction = 'Not survived'
    elif prediction == 1:
        prediction = 'Survived'
    else:
        prediction = 'ERROR'
    return prediction
