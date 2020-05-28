from flask import Flask, request, render_template
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    isbn = request.args.get("isbn")
    book = {}
    if isbn:
        url = f'https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data'
        r = requests.get(url).json()
        k = f'ISBN:{isbn}'
        if k in r:
            book = r[k]
            book['authors'] = ", ".join([author['name'] for author in book['authors']])
            book['image'] = book['cover']['large']
    return render_template('index.html', book=book)


if __name__ == '__main__':
    app.run()
