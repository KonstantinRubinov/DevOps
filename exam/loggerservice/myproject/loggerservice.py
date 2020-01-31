from flask import Flask
import pathlib

app = Flask(__name__)

@app.route('/usage.log')

def my_log():
  str = ""
  mypath=pathlib.Path(__file__).parent.absolute() + "/log.txt"
  with open(mypath, "r") as fp:
      content = fp.readlines()
      for ele in content:  
        str=str+ele+'<br>'
      return str
  
if __name__ == '__main__':
   app.run(host='0.0.0.0',port='5001')
