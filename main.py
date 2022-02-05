from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return "<b>Миссия Колонизация Марса</b>"


@app.route('/index')
def index():
    return "<b>И на Марсе будут цвести яблони!</b>"


@app.route('/promotion')
def promotion():
    return '''<pre><b>Человечество вырастает из детства.

Человечеству мала одна планета.

Мы сделаем обитаемыми безжизненные пока планеты.

И начнем с Марса!

Присоединяйся!</b></pre>'''


@app.route('/image_mars')
def image_mars():
    return f'''
    <h1 class=""bg-info text-white>Жди нас Марс!</h1>
    <img src="img/mars.png">
    <br> Вот такая она какая, красная планета'''


@app.route('/promotion_image')
def promotion_image():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" type="text/css" href="style.css'" />
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Жди нас Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас Марс!</h1>
                    <img src="img/mars.png">
                    <div class="alert alert-secondary" role="alert">
                      Человечество вырастает из детства
                    </div>
                    <div class="alert alert-success">
                      Человечеству мала одна планета
                    </div>
                    <div class="alert alert-secondary">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-warning">
                      И начнем с Марса!
                    </div>
                    <div class="alert alert-danger">
                      Присоединяйся!
                    </div>
                  </body>
                </html>'''




if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')