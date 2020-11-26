# placement_prediction_heroku_deployment
This is a classification use case which will classify whether a student will be able to get college placements or not based on various factors.

### Prerequisites
You must have Scikit Learn, Pandas (for Machine Leraning Model) and Flask (for API) installed.

### Project Structure :

1.templates
i) indext.html -- HTML for taking input from user
ii) predict.html -- HTML form for showing predictions
 
2. app.py - This contains Flask APIs that receives student details through GUI or API calls, computes the precited value based on our model and returns it.

3. model.ipynb - This contains code of model training and model testing.

4. model.pkl - contains our serialized trained model which will be used for making predictions.

5. requirements.txt - contains name of libraries which will get installed while deployment of application.

6. procfile - A mandatory file required when app is getting deployed on 'Heroku Cloud'.

7. Data_Preprocessing - Contains jupyter notebooks of EDA and all dataset Preprocessing and also scaled data.

### Running a File

Goto -- Anaconda Propt

Type -- cd "Path where file is saved"  then click enter

Then you will be on that path

Then type command
~~~
python app.py
~~~

App will start running and it will generate following local url

~~~
http://localhost:5000/
~~~

Enter this url on any browser, then you will see user input form.


#### This File is a deployable file on Heroku cloud
