from flask import Flask, render_template

app = Flask(__name__)

# Маршрут для главной страницы
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

# Маршрут для страницы "О нас"
@app.route('/about')
def about():
    return render_template('about.html')

# Маршрут для страницы блога
@app.route('/blog')
def blog():
    return render_template('blog.html')

# Маршрут для страницы контактов
@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

# Маршруты для страниц с услугами
@app.route('/mesotherapy')
def mesotherapy():
    return render_template('mesotherapy.html')

@app.route('/hair_removal')
def hair_removal():
    return render_template('hair_removal.html')

@app.route('/body_sculpting')
def body_sculpting():
    return render_template('body_sculpting.html')

# Запуск приложения
if __name__ == '__main__':
    app.run(debug=True)
