from flask import Flask, render_template, request

app = Flask(__name__)

# Define a route for the root URL ("/") and render an HTML template
@app.route('/')
def home():
    items = ["Item 1", "Item 2", "Item 3"]
    return render_template('index.html', items=items)

@app.route('/generate_story', methods=['POST'])
def generate_story():
    name = request.form.get('name')
    age = request.form.get('age')
    job_title = request.form.get('job_title')

    story = f"Once upon a time, {name}, at the age of {age}, dreamed of becoming a {job_title}."

    return render_template('story.html', story=story)

@app.route('/search')
def search():
    return render_template('search.html', results=None)


@app.route('/search_results', methods=['GET'])
def search_results():
    query = request.args.get('query')

    # Perform your search logic here and populate the 'results' variable with search results.
    # For this example, we'll assume 'results' is a list of search results.
    results = ['Result 1', 'Result 2', 'Result 3']
    results.append(str(query))# Replace with your actual search results.

    return render_template('search.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)
