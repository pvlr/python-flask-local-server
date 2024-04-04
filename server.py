from flask import Flask, request, redirect, url_for, render_template
import os, subprocess, webbrowser

# Инициализация приложения в переменной app
app = Flask(__name__)


@app.route('/')
def index():
    # Рендер главной страницы
    return render_template('index.html')


# Обработка запроса create-file
@app.route('/create-file', methods = ['GET'])
def createFile():
    # С помощью библиотеки request получаем название и содержимое файла
    # из параметров GET-запроса
    filename = request.args.get('filename')
    content = request.args.get('content')
    # Указываем путь к создаваемому файлу. Можно указывать абсолютный либо относительный
    path = os.path.join('C:/my-web-service/files', filename)

    # Попытка создать файл по указанному пути
    with open(path, 'w') as file:
        # В файл записываем содержимое - content
        file.write(content)

    # Переадресация пользователя обратно на главную страницу
    return redirect(url_for('index'))


# Обработка запроса music
@app.route('/music')
def openYoutube():
    # Открываем ссылку в новой вкладке браузера
    # Если указать параметр new = 2, ссылка будет открыта в новом окне
    webbrowser.open('https://youtu.be/dQw4w9WgXcQ?si=hPRN_O27yOUPo0ai', new = 1)

    # Отправляем пользователя обратно на главную страницу
    return redirect(url_for('index'))


# Обработка запроса openvscode
@app.route('/openvscode')
def openVSCode():
    # С помощью библиотеки subprocess запускаем VS Code
    subprocess.Popen(['C:\Microsoft VS Code\Code.exe'])

    # Отправляем пользователя обратно на главную страницу
    return redirect(url_for('index'))


# Точка входа
if __name__ == '__main__':
    app.run(host = '192.168.1.161', port = 5000, debug = True)
