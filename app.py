from flask import Flask, render_template
app = Flask(__name__)

@app.route('/category')
def index_category():
    return render_template('/category/index.html')

if __name__=="__main__":
    app.run(debug=True)