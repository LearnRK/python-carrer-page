from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        "id": 1,
        "title": "Data Analyst",
        "location": "Bengaluru, India",
        "salary": "Rs. 10,00,000"
    },
    {
        "id": 2,
        "title": "FrontEnd Developer",
        "location": "Bengaluru, India",
        "salary": "Rs. 10,00,000"
    },
    {
        "id": 3,
        "title": "BackEnd Developer",
        "location": "Bengaluru, India",
        "salary": "Rs. 10,00,000"
    },
]

@app.route("/")
def hello_career():
    return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__" :
  app.run(host='0.0.0.0', port=8080, debug=True)