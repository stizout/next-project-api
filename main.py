from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from openai import OpenAI
from decouple import config

client = OpenAI(api_key=config('OPENAI_API_KEY'))

app = Flask(__name__)
cors = CORS(app, origins=['http://127.0.0.1'])
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/generate', methods=['POST', 'OPTIONS'])
@cross_origin()
def generate():
    print('hello')
    return 'Success'
    # data = request.get_json()
    # print(data)
    # try:
    #     response = client.chat.completions.create(model='gpt-3.5-turbo', messages=[{'role': 'system', 'content': 'You are an assistant who helps a user seem more elegant. You will receive two inputs, who the user is talking to, and what they said. You are to help the user better talk to the specified person. '},{'role': 'user', 'content': 'i am ok'}])
    #     print(response)
    #     return jsonify({'message': response.choices[0].message.content}),200
    # except Exception as e:
    #     print(e)
    #     return 'Error on server', 500

if __name__ == '__main__':
    app.run(debug=True)