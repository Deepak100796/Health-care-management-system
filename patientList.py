from app import app
from flask import render_template, request,session,jsonify
from db_config import patient

# def signupDoctor():                     
#     @app.route('/patientList')
#     def plist():
#         pass
    #     return render_template('signup.html')
def PatientList():
    @app.after_request
    def apply_caching(response):
            response.headers["Content-Type"] = "application/json"
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Headers'] = 'content-type'
            return response
            
    @app.route('/patientList', methods=['POST'])
    def patientlist():
        if request.method =='POST':
            data=patient.find()
            l=[]
            print(request.get_json(),'*************23')
            for i in data:
                # if i['DoctorId']==request.form['doc_ID']:
                    name=i['Firstname']+' '+i['Lastname']   
                    gender=i['Gender']
                    email=i['EmailId']
                    dob=i['Birth Date']
                    mob=i['Mobile_Num']
                    mydict={'name':name,'gen':gender,'email':email,'DOB':dob,'mobile':mob}
                    l.append(mydict)
                    # if i['Firstname']+' '+i['Lastname']=='vikash sharma':
            # return jsonify(l)
            response = jsonify(l)#({'DocId':str(i["_id"])})
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers['Access-Control-Allow-Origin'] = '*'
            print(response)
            print(response.headers)
            return response
            # return "None"
                
PatientList()   

# if __name__ == '__main__':

#     app.run(debug=True,port=5002)