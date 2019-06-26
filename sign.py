from flask import render_template, request,session,jsonify


# from flask_api import status
import hashlib
from db_config import doctor
from app import app

# def signupDoctor():                     
#     @app.route('/signup')
#     def root():
#         return render_template('signup.html')
#         # pass

def signupDoctor():
    @app.after_request
    def apply_caching(response):
        response.headers["Content-Type"] = "application/json"
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = 'content-type'
        return response
    @app.route('/signup',methods = ['POST'])
    def signup():
        if request.method == 'POST':
 
            # fnm = request.form["Firstname"]
            # mnm = request.form["Middlename"]
            # lnm = request.form["Lastname"]
            # eml = request.form["EmailId"]
        
            # mno = request.form["MobileNo"]
            # pasw = hashlib.sha256(str.encode(request.form["Password"])).hexdigest()
            # mydict = {"Firstname": fnm,"Middlename": mnm,"Lastname":lnm,"EmailId":eml,"Mobile_Num":mno,"Password":pasw}
            
            # doctor.insert_one(mydict)
       
            # session['logged_in']=flask
            # return render_template("signup.html")
            payload=request.get_json()
            # payload["Password"] = hashlib.sha256(str.encode(request.form["Password"])).hexdigest()
            # print(payload)
            doctor.insert_one(payload)
            # print(payload)
            # del payload['_id']
            response = jsonify({'status':'Success'})
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers['Access-Control-Allow-Origin'] = '*'
            print(response)
            print(response.headers)
            return response
            # return jsonify([payload])
            # return 'Tru

signupDoctor()  