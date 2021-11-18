pip install psycopg2-binary
app = Flask(__name__)
@app.route('/')

def hello_world():
    return 'Hello world'
    