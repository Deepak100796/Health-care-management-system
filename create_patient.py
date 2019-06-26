from flask import render_template, request,session,jsonify
# import hashlib

from db_config import doctor,patient
from app import app 


def CreatPatient():
    # @app.route('/New_Patient')
    # def root1():
    #     return render_template('New_Patient.html')
    @app.after_request
    def apply_caching(response):
            response.headers["Content-Type"] = "application/json"
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Headers'] = 'content-type'
            return response

    @app.route('/New_Patient',methods = ['POST'])
    def New_Patient():
        if request.method == 'POST':
 
            # fnm = request.form["Firstname"]
            # lnm = request.form["Lastname"]
            # gen=  request.form["Gender"]
            # eml = request.form["EmailId"]
            # dob = request.form["Birth Date"]
            # mno = request.form["Mobile"]
            # print(session['docId'])
            payload=request.get_json()
            # print(request.form['doc_ID'])
            payload['DoctorId']=payload['doc_ID']
            # mydict = {"DoctorId":session['docId'],"Firstname": fnm,"Lastname":lnm,"Gender":gen,"Birth Date":dob,"EmailId":eml,"Mobile_Num":mno}
          
            # payload['DoctorId']=session['docId']
            # print(payload)
            # session['docId']=False 
            # patient.insert_one(mydict)
            patient.insert_one(payload)   
            # print(mydict)
            # return render_template("ContactDetail.html")
            response = jsonify({'status':'successjdbfjdfbgjfbgjfbgj'})
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers['Access-Control-Allow-Origin'] = '*'
            print(response)
            print(response.headers)
            return response

CreatPatient()