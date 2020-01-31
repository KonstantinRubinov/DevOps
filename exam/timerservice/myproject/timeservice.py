from flask import Flask
import datetime
import os
import pathlib

app = Flask(__name__)

@app.route('/')

def my_log():
  mypath=os.path.dirname(os.path.abspath(__file__))
  now = datetime.datetime.now()
  f = open("/log.txt", "a+")
  f.write('Read at ' + now.strftime("%a %b %d %Y %H:%M:%S") + ' GTM+0000 (UTC)' + os.linesep)
  f.close()
  return mypath

if __name__ == '__main__':
   app.run(host='0.0.0.0',port='5000')
