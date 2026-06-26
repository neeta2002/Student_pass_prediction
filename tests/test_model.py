import joblib
def test_student_pass():
    model=joblib.load("model/model.pkl")
    prediction=model.predict([[7]])
    assert prediction[0]==1