# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 10:43:44 2021

@author: baner
"""




from flask import Flask,request,jsonify,render_template
import requests





app = Flask(__name__)




@app.route('/upload', methods=['GET','POST'])
def upload():

    if request.method == "POST":
        
        payload = request.form
        files = request.files
        # for k, v in files.items():
        #     print(k, v)
        print(files["audio"].filename)
        
        
        # print(dir(files))
        print("xxxxxxxxxxxxxxxxxx")
        # print(dir(files["audio"]))
        response = requests.request(
        "POST", 
        "https://speechrecognitionapi.herokuapp.com/upload", 
        data=payload, 
        files={files["audio"].name : (files["audio"].filename, files["audio"], files["audio"].mimetype)}
    )
    
    
        print(response.content)
        data = response.json()
        print(data['Emotion'])
        
        
        
        
      
    
        return render_template('base.html',emotion=data['Emotion'])

    print("gettttttttttt")
    return render_template('home.html')
        
    
    
    
                    
            
        
    
    
    
    


   
            
    
    

if __name__ == "__main__":
    app.run(debug=True)
