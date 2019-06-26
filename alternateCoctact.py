from flask import render_template, request,session
import hashlib
from db_config import doctor,patient
from app import app                   

def FillAlternateContact():
    @app.route('/AlternateContact')
    def rootAC():
        return render_template('AlternateContact.html')

    @app.route('/AlternateContact',methods = ['POST'])
    def AlternateContact():
        if request.method == 'POST':
 
            fname = request.form["Full Name"]
            mno = request.form["MobileNo"]
            Rship=  request.form["RelationShip"]
          
            # payload=request.get_json()
            mydict={'Full Name':fname,'MobileNo':mno,'RelationShip':Rship}
            for pId in patient.find():
                if session['docId'] == pId['DoctorId']:
                    name=pId["Firstname"]+' '+pId["Lastname"]
                    if request.form["Patient name"] == name:
                        try:
                            
                            pId['AlternateContact'].append(mydict)
                            patient.update_one({
                                    '_id':pId['_id']
                                },{
                                    '$set':{
                                
                                        'AlternateContact':pId['AlternateContact']
                                        }
                                    }
                                )
                        except KeyError:
                            patient.update_one({
                                    '_id':pId['_id']
                                },{
                                    '$set':{
                                
                                            'AlternateContact':[mydict]
                                        }
                                    }
                            )
                        return render_template("AlternateContact.html",a='AlternateContact Add')

FillAlternateContact()
