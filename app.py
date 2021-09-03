from flask import Flask
from flask import request

app = Flask(__name__)


def animal_say(animal, sound, count, method):
    say_phrase = ""
    for i in range(int(count)):
        if method == 'POST':
            say_phrase = say_phrase + str("{} says {} \n".format(animal, sound))
        else:
            say_phrase = say_phrase + str("<p style='font-size:12pt'><b>{}</b> says {} </p>".format(animal, sound))

    if method == 'POST':
        say_phrase = say_phrase + "Made with by vacilyok \n"
    else:
        say_phrase = say_phrase + "<p style='font-size:12pt'>Made with by <a href='https://github.com/vacilyok'>vacilyok</a></p>"

    return say_phrase


def incorrectPage():
    html = '''
            <html>
            <body>
            <h1>No data found to display</h1>
            <h2>Exemple data</h2>
            <p>
            <a href='?animal=ram&sound=beeee&count=3'>localhost?animal=ram&sound=beeee&count=3</a>
            </p>

            </body>
            </html>
           '''
    return html


@app.route("/", methods=['GET', 'POST'])
def hello():
    count = 2
    animal = '-'
    sound = '-'
    if request.method == 'POST':
        request_data = request.get_json()
        if request_data == None:
            animal = request.form.get('animal')
            sound = request.form.get('sound')
            count = request.form.get('count')
            if (animal == None or sound == None or count == None):
                return "Incorrect data format"

        else:
            if 'animal' in request_data:
                animal = request_data['animal']
            else:
                return "Incorrect data format. Not found 'animal' key "
            if 'sound' in request_data:
                sound = request_data['sound']
            else:
                return "Incorrect data format. Not found 'sound' key "
            if 'count' in request_data:
                count = request_data['count']
            else:
                return "Incorrect data format. Not found 'count' key "

    if request.method == 'GET':
        animal = request.args.get("animal")
        sound = request.args.get("sound")
        count = request.args.get("count")
        if (animal == None or sound == None or count == None):
            return incorrectPage()

    return animal_say(animal, sound, count, request.method)


if __name__ == "__main__":
    from waitress import serve
    # website_url = 'localhost'
    # app.config['SERVER_NAME'] = website_url
    # app.run()
    serve(app, port=80)
