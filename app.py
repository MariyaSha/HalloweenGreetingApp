from flask import Flask, render_template, request, flash
import random

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888" #this is a DUMMIE secret key

@app.route("/")
def index():
	flash("what's your name?")
	return render_template("index.html")

@app.route("/greet", methods=['POST'])
def greeter():
	monsters = ["Selenderman",
				"Dracula",
				"Frankenstein",
				"Davy Jones",
				"Michael Myers", 
				"Freddy Krueger", 
				"Hannibal Lecter",
				"Ghostface", 
				"Norman Bates",
				"Samara",
				"Patrick Bateman",
				"The Wicked Witch of The West",
				"Captain Spaulding",
				"Beetlejuice",
				"Jason Voorhees", 
				"Leatherface", 
				"Chucky", 
				"The Blair Witch", 
				"Pyramid Head",
				"Oogie Boogie",
				"Boogeyman",
				"Erlking",
				"Baba Yaga",
				"John Kramer",
				"Krampus",
				"Agent Smith"]
	flash("Hi " + str(request.form['name_input']) + "! " + random.choice(monsters) + " is happy to see you!")
	return render_template("index.html")
