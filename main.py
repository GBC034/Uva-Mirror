#coding=utf-8
from bottle import route,request,template,view,run,Bottle,static_file,get, post, response
import bottle
    
@get("/js/<filepath:re:.*\.(css|jpg|png|gif|ico|svg|js|eot|otf|svg|ttf|woff|woff2?)>")
def szsh1(filepath):
    return static_file(filepath, root="js")
@get("/js2/<filepath:re:.*\.(css|jpg|png|gif|ico|svg|js|eot|otf|svg|ttf|woff|woff2?)>")
def szsh2(filepath):
    return static_file(filepath, root="js2")
@get("/images/<filepath:re:.*\.(css|jpg|png|gif|ico|svg|js|eot|otf|svg|ttf|woff|woff2?)>")
def szsh3(filepath):
    return static_file(filepath, root="images")
@get("/images2/<filepath:re:.*\.(css|jpg|png|gif|ico|svg|js|eot|otf|svg|ttf|woff|woff2?)>")
def szsh4(filepath):
    return static_file(filepath, root="images2")
@get("/css/<filepath:re:.*\.(css|jpg|png|gif|ico|svg|js|eot|otf|svg|ttf|woff|woff2?)>")
def szsh5(filepath):
    return static_file(filepath, root="css")
@get("/css2/<filepath:re:.*\.(css|jpg|png|gif|ico|svg|js|eot|otf|svg|ttf|woff|woff2?)>")
def szsh6(filepath):
    return static_file(filepath, root="css2")
@get("/uploadfile/<filepath:re:.*\.(css|jpg|png|gif|ico|svg|js|eot|otf|svg|ttf|woff|woff2?)>")
def szsh7(filepath):
    return static_file(filepath, root="uploadfile")
@get("/html/<filepath:re:.*\.(html|1)>")
def szsh8(filepath):
    return static_file(filepath, root="html")
@get("/2016/<filepath:re:.*\.(html)>")
def szsh9(filepath):
    return static_file(filepath, root="2016")
@get("/2017/<filepath:re:.*\.(html)>")
def szsh10(filepath):
    return static_file(filepath, root="2017")
@get("/2020/<filepath:re:.*\.(html)>")
def szsh11(filepath):
    return static_file(filepath, root="2020")
@get("/2021/<filepath:re:.*\.(html)>")
def szsh12(filepath):
    return static_file(filepath, root="2021")    
@get("/active/<filepath:re:.*\.(html)>")
def szsh13(filepath):
    return static_file(filepath, root="active")     
@get("/complaint/<filepath:re:.*\.(html)>")
def szsh14(filepath):
    return static_file(filepath, root="complaint")  
@get("/event/<filepath:re:.*\.(html)>")
def szsh15(filepath):
    return static_file(filepath, root="event")  
@get("/policy/<filepath:re:.*\.(html)>")
def szsh16(filepath):
    return static_file(filepath, root="policy")      
@get("/research/<filepath:re:.*\.(html)>")
def szsh17(filepath):
    return static_file(filepath, root="research")  
@get("/service/<filepath:re:.*\.(html)>")
def szsh18(filepath):
    return static_file(filepath, root="service")   
@get("/<filepath:re:.*\.(html)>")
def szsh19(filepath):
    return static_file(filepath, root="") 
    
@route('/',method = 'GET')
def index():
    return template("index" , result = [])
 
run(host='0.0.0.0',port=8888)