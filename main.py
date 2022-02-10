from flask import Flask, url_for, request

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
    <img src="/img/mars.png">
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


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" type="text/css" href="style.css'" />
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Анкета претендента</h1>
                            <h2>на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите фамилию" name="email">
                                    <input type="password" class="form-control" id="password" placeholder="Введите имя" name="password">
                                    <input type="password" class="form-control" id="password" placeholder="Введите адресс почты" name="password">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее специальное</option>
                                          <option>Высшее</option>>
                                        </select>
                                     </div>
  
                            <div class="form-group">
                                        <label for="form-check">Какие у вас есть профессии?</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="prof" id="engineer_researcher"
                                           value="engineer_researcher" checked>
                                          <label class="form-check-label" for="engineer_researcher">
                                            Инженер-иследователь
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="prof" id="civil_engineer" value="civil_engineer">
                                          <label class="form-check-label" for="civil_engineer">
                                            Инженер-строитель
                                          </label>
                                        </div>
                                    </div>
                                                                     <div class="form-check">
                                          <input class="form-check-input" type="radio" name="prof" id="pilot" value="pilot" checked>
                                          <label class="form-check-label" for="pilot">
                                            Пилот
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="prof" id="meteo" value="meteo" checked>
                                          <label class="form-check-label" for="meteo">
                                            Метеоролог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="prof" id="life_support_engineer" 
                                          value="life_support_engineer" checked>
                                          <label class="form-check-label" for="life_support_engineer">
                                            Инженер по жизнеобесепчению
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="prof" id="radiation_protection_engineer" 
                                          value="radiation_protection_engineer" checked>
                                          <label class="form-check-label" for="radiation_protection_engineer">
                                            Инженер по радиационной защите
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="prof" id="doctor" 
                                          value="doctor" checked>
                                          <label class="form-check-label" for="doctor">
                                            Врач
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="prof" id="ekz" 
                                          value="ekz" checked>
                                          <label class="form-check-label" for="ekz">
                                            Экзобиолог
                                          </label>
                                        </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>

                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')