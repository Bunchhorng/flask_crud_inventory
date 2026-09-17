from flask import Flask, render_template, request, redirect, url_for
from connect import connectDB

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('layout/base.html')


@app.route('/category', methods = ['GET', 'POST'])
def index_category():
    db =  connectDB()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM categories')
    categories = cursor.fetchall()
    db.commit()
    cursor.close()
    return render_template('category/index.html', categories=categories)


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

@app.route('/category/update/<int:id>', methods = ['GET', 'POST'])
def update_category(id):

    db = connectDB()
    cursor = db.cursor()

    if request.method == 'POST':
        newName = request.form['name']
        newStatus = request.form['status']

        sql = "UPDATE categories SET name=%s, status=%s WHERE id=%s"
        cursor.execute(sql, (newName, newStatus, id))
        db.commit()
        cursor.close()
        return redirect(url_for('index_category'))

    cursor.execute("SELECT * FROM categories WHERE id=%s", (id,))
    category = cursor.fetchone()
    db.commit()
    cursor.close()

    if not category:
        return "Category not Found"
    
    return render_template('category/update.html', category=category)

@app.route("/category/delete/<int:id>", methods = ['GET', 'POST'])
def delete_category(id):
    db = connectDB()
    cursor =db.cursor()
    cursor.execute("DELETE FROM categories WHERE id=%s", (id,))
    db.commit()
    cursor.close()
    return redirect(url_for('index_category'))

# ============Product Route====

@app.route('/product')
def index_product():
    return render_template('product/index.html')



if __name__ == "__main__":
    app.run(debug=True)