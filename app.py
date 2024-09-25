from flask_cors import cross_origin , CORS
from flask import Flask, render_template, request, jsonify
from text_summary import summarizer

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
@cross_origin()
def summarize_text():
    
    text = request.get_json()['text']
    summary = summarizer(text)
    print(summary)
    return jsonify({'summary' :summary})

@app.route('/try', methods = ['GET'])
def try_text():
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True)
