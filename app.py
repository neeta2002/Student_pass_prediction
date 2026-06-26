from flask import Flask
import joblib 
app=Flask(__name__)
model=joblib.load("model/model.pkl")
@app.route("/")
def home():
    prediction=model.predict([[7]])
    result="Pass" if prediction[0]==1 else "Fail"
    return f"students Result:{result}"

if __name__=="__main__":
    app.run(debug=True)