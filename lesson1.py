from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    context = {'title': 'Главное меню', 'content': 'Сдесь должени быть список товаров'}
    return render_template("index.html", **context)

@app.route('/jacket.html')
def jacket():
    context = {'title': 'одежда', 'content': 'Сдесь должени быть список товаров'}
    return render_template("jacket.html", **context)

@app.route('/cloth.html')
def cloth():
    context = {'title': 'куртки', 'content': 'Сдесь должени быть список товаров'}
    return render_template("cloth.html", **context)

@app.route('/shoes.html')
def shoes():
    context = {'title': 'обувь', 'content': 'Сдесь должени быть список товаров'}
    return render_template("shoes.html", **context)



if __name__ == '__main__':
    app.run(debug=True)