
from app import app
from sign import signupDoctor   
from login import loginDoctor
from create_patient import CreatPatient
from contact import fillContact
from alternateCoctact import FillAlternateContact
from patientList import PatientList
from getPatientData import patientData


# signupDoctor()
# a=loginDoctor()           
# print(a)
# CreatPatient()
# fillContact()


if __name__ == '__main__':
#    app.run(debug = True)
    # app.secret_key = 'some secret key'
    app.debug = True
    app.run(host='0.0.0.0',port=5001)