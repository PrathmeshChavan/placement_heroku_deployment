from flask import Flask , render_template , request
import pickle
import numpy as np

app = Flask(__name__)
model=pickle.load(open("model.pkl" , 'rb'))

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/predict', methods=["GET" , "POST"])
def predict():

            ssc_p = float(request.form['ssc_p'])
            hsc_p = float(request.form['hsc_p'])
            degree_p = float(request.form['degree_p'])
            workex = float(request.form['workex'])
            specialisation = float(request.form['specialisation'])
            gender = float(request.form['gender'])
            
            pred_agrs = [ssc_p , hsc_p , degree_p , workex , specialisation , gender]
                        
            
            pred_agrs_arr = np.array(pred_agrs)
            pred_agrs_arr = pred_agrs_arr.reshape(1 , -1)
            
            model_pred = model.predict(pred_agrs_arr)
            model_pred = round(float(model_pred))

            if model_pred == 0:
                return render_template('predict.html' , prediction = "Student will not get placement")
            
            if model_pred == 1:
                return render_template('predict.html' , prediction = "Student will get placement")
                

if __name__ == "__main__":
    app.run(debug=True)







