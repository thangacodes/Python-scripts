from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# Custom 404 error page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404
if(__name__=='__main__'):
    app.run(debug=True, host='0.0.0.0', port=5000)
