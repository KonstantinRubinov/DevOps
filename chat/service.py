from flask import Flask, render_template
import json
import requests

app = Flask(__name__)





@app.route('<int:room>', methods=['GET'])
def return_data(room):
  return render_template('index.html')



@app.route('/chat/<int:room>', methods=['POST'])
def accept_data(room):
  data = {}
  data['chat'] = []
  data['chat'].append({
    'date': 'Scott',
    'time': 'stackabuse.com',
    'name': request.form['username'],
    'msg': request.form['msg']
  })

  filepath = room + 'log.json'
  with open(filepath, 'w') as outfile:
      json.dump(data, outfile)

  return 'Received !' # response to your request.





"[2018-02-25 14:00:51] omri: hi everybody!"











@app.route('/chat/<int:room>', methods=['GET'])
def return_chat(room):
  filepath = room + 'log.json'
  with open(filepath, "r") as fp:
   content = fp.readlines()
  return content[-1]



if __name__ == '__main__':
app.run(debug=True, host='0.0.0.0')




