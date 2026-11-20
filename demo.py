from flask import Flask, render_template
from gpiozero import Buzzer

app = Flask(__name__)
buzzer = Buzzer(17)

@app.get("/")
def hello():
    return render_template("home.html", person="anoniempje")

@app.get("/buzzer/<action>")
def buzzer_action(action):
    if(action == "on"):
        buzzer.on()
        return ""
    if(action == "off"):
        buzzer.off()
        return ""
    else:
        return "not a valid action"

@app.get("/team/<person>")
def team(person):
    return render_template("home.html", person=person)

@app.get("/contact")
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(
        host="0.0.0.0", 
        port=5000, 
        debug=True,
        use_reloader=False
    )