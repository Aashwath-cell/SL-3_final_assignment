from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.exceptions import BadRequest

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        try:
            name = request.form.get('name', '').strip()
            age = request.form.get('age', '').strip()
            
            # Basic validation
            if not name:
                raise BadRequest('Name is required')
            if not age:
                raise BadRequest('Age is required')
            
            try:
                age = int(age)
                if age <= 0:
                    raise BadRequest('Age must be a positive number')
            except ValueError:
                raise BadRequest('Age must be a number')
            
            return f'Hello, {name}! You are {age} years old.'
            
        except BadRequest as e:
            flash(str(e))
            return redirect(url_for('greet'))
    
    return '''
        <form method="POST">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required><br>
            <label for="age">Age:</label>
            <input type="number" id="age" name="age" required><br>
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 