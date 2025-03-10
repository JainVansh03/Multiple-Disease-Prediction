import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('diabetes.pkl', 'rb'))
model1 = pickle.load(open('heart.pkl', 'rb'))
model2 = pickle.load(open('kidney.pkl', 'rb'))


    

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['GET'])
def predict():
   
    '''
    For rendering results on HTML GUI
    '''
    return render_template('index.html')
   
    
@app.route('/predict/diabetes',methods=['POST'])
def diabetes():
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    #print(final_features)
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    if output == 1 :
        
       return render_template('info.html')
    else:
      
       return render_template('info1.html')
@app.route('/predict1',methods=['GET'])
def predict1():
   
    '''
    For rendering results on HTML GUI
    '''
    return render_template('index1.html')
@app.route('/predict1/heart',methods=['POST'])
def heart():
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    #print(final_features)
    prediction = model1.predict(final_features)

    output = round(prediction[0], 2)
    if output == 1 :
        return render_template('info2.html')
    else:
      return render_template('info3.html')

@app.route('/predict2',methods=['GET'])
def predict2():
   
    '''
    For rendering results on HTML GUI
    '''
    return render_template('index2.html')
@app.route('/predict2/Kidney',methods=['POST'])
def kidney():
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    #print(final_features)
    prediction = model2.predict(final_features)

    output = round(prediction[0], 2)
    if output == 1 :
       return render_template('info4.html')
    else:
       return render_template('info5.html')
@app.route('/predict/information')
def information():
    return render_template('information.html')
    
@app.route('/predict/information1')
def information1():
    return render_template('information1.html')
    
@app.route('/predict/information2')
def information2():
    return render_template('information2.html')
    
@app.route('/predict/information3')
def information3():
    return render_template('information3.html')
    
@app.route('/predict/information4')
def information4():
    return render_template('information4.html')
    
@app.route('/predict/information5')
def information5():
    return render_template('information5.html')
   
    

    
 
   

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(host='0.0.0.0')