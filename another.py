from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, headers='Content-Type')
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET'])
def home():
    print('chicking')
    return 'Success', 200
if __name__ == '__main__':
    app.run(debug=True)