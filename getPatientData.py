from app import app
from flask import render_template, request,session,jsonify

from db_config import patient


def signupDoctor():
    @app.route('/PatientData')
    def pdata():
        # # return render_template('New_Patient.html')
        # print("jnvjdksbjfbfjvbfjv")
        # return "jkndcdj"
        pass
def patientData():
    @app.route('/PatientData')#, methods=['GET'])
    def patientdata():
        if request.method =='GET':
            data=patient.find()
            for i in data:
                
                # if i['DoctorId']==session['docId']:
                    a=i['Firstname']+' '+i['Lastname']
                    print(a,'************+')
                    if a =='prashant katiyar':
                        i['_id']=str(i['_id'])
                        return jsonify([i])
                    else:
                        pass
                # else:
                #     return "No data for this doctor"
                
            
            return "No Data found"
    
patientData()
# if __name__ == '__main__':

#     app.run(debug=True,port=5002)