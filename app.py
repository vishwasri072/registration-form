from flask import Flask,render_template_string,request
app=Flask(__name__)
html= """
<!DOCTYPE html>
<html>
<head>
    <title>Registration Form</title>
</head>
<body>
    <h2>Registration Form</h2>
    <form method="POST" action="/register">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>
        <input type="submit" value="Register">
    </form>
    {% if message %}
        <p>{{ message }}</p>
    {% endif %}
</body>
</html>
"""
@app.route('/', methods=['GET', 'POST'])
def register():
    message = None
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        # Here you can add code to save the data to a database or perform other actions
        message = f"Thank you for registering, {name}! We have received your email: {email}."
    return render_template_string(html, message=message)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)