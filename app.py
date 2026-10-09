from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

app.secret_key = "mysecretkey"


@app.route("/", methods=["GET", "POST"])
def admin():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == "Admin" and password == "1234":

            session["admin_logged_in"] = True

            return redirect(url_for("dashboard"))

        else:

            return render_template(
                "admin.html",
                error="Invalid username or password"
            )

    return render_template("admin.html")


@app.route("/dashboard")
def dashboard():

    if not session.get("admin_logged_in"):
        return redirect(url_for("admin"))

    return render_template("dashboard.html")


@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("admin"))


if __name__ == "__main__":
    app.run(debug=True,port=5000)