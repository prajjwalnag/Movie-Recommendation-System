from flask import Flask, request, render_template
from searchv import init, search_items

app = Flask(__name__)

# Initialize the model once when the app starts
#init()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    search_term = request.form['search_term']
    init()
    results = search_items(search_term)
    return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)