from flask import render_template, request,session
import hashlib
from db_config import doctor,patient
from app import app
               

def fillContact():
    @app.route('/ContactDetail')
    def root2():
        return render_template('ContactDetail.html')

    @app.route('/ContactDetail',methods = ['POST'])
    def ContactDetail():
        if request.method == 'POST':
 
            add = request.form["Addrass"]
            city = request.form["City1"]
            country=  request.form["Country"]
            state = request.form["State/Provide"]
            Zip = request.form["ZIP/Postal Code"]
            ph1 = request.form["Phone1"]
            ph2 = request.form["Phone2"]
            
            # payload=request.get_json()
            for pId in patient.find():
                if session['docId'] == pId['DoctorId']:
                    name=pId["Firstname"]+' '+pId["Lastname"]
                    if request.form["Patient name"] == name:
                        patient.update_one({
                                    '_id':pId['_id']
                            },{
                            # '$set':{'name':'chandra'},
                                '$set':{
                                'adresss':{'Addrass':add,'City':city,'Country':country,'State/Provide':state,'ZIP/Postal Code':Zip,'Phone1':ph1,'Phone2':ph2}
                                }
                            }
                        )
                        return render_template("AlternateContact.html",a='Detail Submit')

fillContact()
    