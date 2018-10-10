from flask import Flask, request
from caesar import rotate_string


app = Flask(__name__)
app.config['DEBUG'] = True


markup = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/caesar" method="post">
        <label for="rotate" />Rotate by:</label>
        <input id="rotate" type="text" value=0 name="rot" />
        <textarea name="text" cols="50" rows="3">{ctext}</textarea>
        <input type="submit" />
        </form>
    </body>
</html>
"""


@app.route("/", methods =['POST', 'GET'])
def index():
    form = markup.format(ctext="")
    return form

@app.route("/caesar", methods =['POST'])
def encrypt():
    rot = int(request.form["rot"])
    text = request.form["text"]
    cipher = rotate_string(text, rot)
    form = markup.format(ctext=cipher)
    return form

app.run()