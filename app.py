from flask import Flask,render_template,request,url_for,jsonify,json
from pythonping import ping
import requests
import sublist3r
import socket
# from scanner import *
import threading
import resolve

import nmap


#user function 
def ScanPort(domain):
    nmScan=nmap.PortScanner()
    res=nmScan.scan(domain,'20-1024')
    key,value=list(res['scan'].items())[0]
    return value


app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def hello_world():
    return render_template("index.html")


@app.route('/sudomain',methods=['POST'])
def sudomain():
    if request.method=="POST":
        domain=request.form["domain"]
        # dis={}
        dictOfWords={}
        suds={}
        try:
            subdomains=sublist3r.main(domain, 40, 'yahoo_subdomains.txt', ports= None, silent=False, verbose= False, enable_bruteforce= False, engines=None)
            
            for i in range(0,len(subdomains)):
                if "<BR>" in subdomains[i]:
                    s=subdomains[i].split("<BR>")
                    for ss in range(0,len(s)):
                        suds[ss]=s[ss]
                else:
                    suds[i]=subdomains[i]

            # suds= { i : if "<BR>" in subdomains[i]:for subdomains in subdomains[i] for i in range(0, len(subdomains) ) }
            # for s in subdomains:
                
                # dictOfWords[s]=
                # print(dictOfWords)
                
            

            dictOfWords=suds
            
            
            jsonStr = json.dumps(dictOfWords)
            
        except RuntimeError as e:
            print(str(e))
        
        return jsonify(jsonStr)

@app.route('/detail',methods=['POST'])
def getDetails():
    if request.method=="POST":
        domain=request.form['domain']
        s=resolve.resolve(domain)
        # print(s)
        return s


@app.route('/port',methods=['POST'])
def sudomains():
    if request.method=="POST":
        domain=request.form["domain"]
        # dis={}
        dictOfWords={}
        
        try:
           
            dictOfWords=ScanPort(domain)
            
            
            jsonStr = json.dumps(dictOfWords)
            
        except RuntimeError as e:
            print(str(e))
        
        return jsonify(jsonStr)






if __name__ == '__main__':
   app.run(debug = True)






