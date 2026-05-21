from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Databricks Flask App Working</h1>
    <p>If you can see this, deployment is working correctly.</p>
    """
