from flask import Flask, render_template, url_for, request, redirect, make_response, flash

app = Flask(__name__)
app.secret_key = b'd962ea0e739a57e13f523ac4c0d843d2ecde7120cf6722cf4a13811d5cb10d3e'

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/hello/')
def hello():
    name = request.cookies.get('username')
    return render_template('hellou.html', name=name)

@app.route('/submit/', methods=['POST', 'GET'])
def submit():
    if request.method == "POST":
        if not request.form.get('name') or not request.form.get('url'):
            flash('введите имя и почту')
            return redirect(url_for('index'))
        respons = make_response(redirect(url_for('hello')))
        name = request.form.get('name')
        url_f = request.form.get('url')
        respons.set_cookie('username', name)
        respons.set_cookie('url', url_f)
        return respons
    return render_template('form.html')


@app.post('/delet_cookie')
def delete():
   respons= make_response(redirect(url_for('index')))
   respons.set_cookie('username', '')
   respons.set_cookie('url', '')
   return respons




if __name__ == '__main__':
    app.run(debug=True)