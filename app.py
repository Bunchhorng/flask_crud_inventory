from flask import Flask, render_template, request, redirect, url_for
from connect import connectDB

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('layout/base.html')


@app.route('/category')
def index_category():
    return render_template('category/index.html')


@app.route('/category/create', methods = ['GET', 'POST'])
def create_category():
    if request.method=="POST":
        name = request.form['name']
        status = request.form['status']


        db = connectDB()
        cursor = db.cursor()
        cursor.execute("INSERT INTO categories(name, status)" \
        "VALUES(%s, %s)", (name, status))

        db.commit()
        cursor = db.close()
        return redirect(url_for('index_category'))
    return render_template('category/create.html')

@app.route('/category/update')
def update_category():
    return render_template('category/update.html')


# ============Product Route====

@app.route('/product')
def index_product():
    return render_template('product/index.html')



if __name__ == "__main__":
    app.run(debug=True)