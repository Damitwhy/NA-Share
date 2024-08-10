from flask import Flask, render_template
import os

app = Flask(__name__)

# Path to the file that stores the visitor count
counter_file = 'counter.txt'

def get_visitor_count():
    if not os.path.exists(counter_file):
        with open(counter_file, 'w') as f:
            f.write('0')
    with open(counter_file, 'r') as f:
        count = int(f.read())
    return count

def increment_visitor_count():
    count = get_visitor_count() + 1
    with open(counter_file, 'w') as f:
        f.write(str(count))
    return count

@app.route('/')
def index():
    count = increment_visitor_count()
    return render_template('index.html', count=count)

if __name__ == '__main__':
    app.run(debug=True)