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
    data = request.get_json()
    print(data)
    prompt = f"""
You are an assistant who updates someones speech in order to sound better depending on the authority. 
You will receive two inputs, the speech that needs to be updated and the authority of whom they are speaking to.
You are to use no more than 10 words.
speech: {data['speaker']}
authority: {data['authority']}
    """
    try:
        response = client.chat.completions.create(model='gpt-3.5-turbo', messages=[{'role': 'system', 'content': prompt},{'role': 'user', 'content': 'i am ok'}])
        print(response)
        return jsonify({'message': response.choices[0].message.content}),200
    except Exception as e:
        print(e)
        return 'Error on server', 500

if __name__ == '__main__':
    app.run(debug=True)