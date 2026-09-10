from flask import Flask, render_template

app = Flask(__name__)

@app.route('/dashboard')
def dashboard():
    return render_template('layout/base.html')


@app.route('/category')
def index_category():
    return render_template('category/index.html')


@app.route('/category/create')
def create_category():
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