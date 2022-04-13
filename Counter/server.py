from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'Count_da_counting_da_Nums' #secret key is secrets


# refreshing page will increase site count
@app.route("/")
def index():
    if "count" not in session:
        session["count"] = 1
    else:
        session["count"] += 1 
# defining the count = session for browser to pickup code
    return render_template('index.html', count = session["count"])

# Button in form content container will increment by 2
@app.route("/count", methods = ["POST"])
def view_count():
    if (request.form["change"]) == "add":
        session["count"] += 1
    elif (request.form["change"]) == "reset":
        session["count"] = 0
    
    return redirect('/')

# Clearing session - Code copied from Great Numba Game
@app.route("/reset")
def reset_session():
    session.clear()
    return redirect("/")


#debug / remove if publishing/finished 
if __name__ == "__main__":
    app.run(debug=True)
