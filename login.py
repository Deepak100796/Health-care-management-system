from flask import render_template, request,session,jsonify
import hashlib
from db_config import doctor
from app import app

# from flask_cors import CORS
# CORS(app)


# def loginDoctor():
# # #         # app=Flask(__name__,template_folder='template')
#         @app.route('/login')
#         def rootes():
# #             # pass
# # #             # if not session.get('logged_in'):
#                 return render_template('C:/Users/chandra/Desktop/login/dataGrazp/template/login.html')
#             #     # return "True1"
#             # else:
            #     session['logged_in']=False
            #     return 'Hello!'
def loginDoctor():
        @app.after_request
        def apply_caching(response):
            response.headers["Content-Type"] = "application/json"
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Headers'] = 'content-type'
            return response
        @app.route('/login',methods = ['POST', 'GET'])
        def login():
            if request.method == 'POST':
                eml=doctor.find()
                payload=request.get_json()
                # print(payload,"*********")
                # em={}
                for i in eml:
                    # try:
                        if payload["Username"] == i["EmailId"]:      
                        # if hashlib.sha256(str.encode(payload['Password'])).hexdigest() == i['Password']:
                            if payload['Password'] == i['Password']:
                            # em['docId']= str(i["_id"])
                            # return render_template('New_Patient.html',a='Login Success')
                            # return jsonify([{'DocId':str(i["_id"])}])
                            # return '123'
                                response = jsonify({'DocId':str(i["_id"])})
                                response.headers.add('Access-Control-Allow-Origin', '*')
                                response.headers['Access-Control-Allow-Origin'] = '*'
                                print(response)
                                print(response.headers)
                                return response
                            else:
                                pass
                        else:
                        
                            # return render_template('login.html',a='wrong password ')
                            # response = jsonify({'wrong':'password wrong'})
                            # response.headers.add('Access-Control-Allow-Origin', '*')
                            # response.headers['Access-Control-Allow-Origin'] = '*'
                            # print(response)
                            # print(response.headers)
                            # return response
                            pass
                    # else:
                        # response = jsonify({'DocId':'email wrong'})
                        # response.headers.add('Access-Control-Allow-Origin', '*')
                        # response.headers['Access-Control-Allow-Origin'] = '*'
                        # print(response)
                        # print(response.headers)
                        # return response
                        # pass

                # return render_template('login.html',a='wrong login Id')
                
                # return render_template('login.html',a='wrong password ')
                response = jsonify({'wrong':'worng email/password'})
                response.headers.add('Access-Control-Allow-Origin', '*')
                response.headers['Access-Control-Allow-Origin'] = '*'
                print(response)
                print(response.headers)
                return response,202         
loginDoctor()
