from flask import Flask, render_template, request
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

app = Flask(__name__)


@app.route("/", methods=["GET","POST"])
def index():
	msg1 = ""
	msg2 = ""
	btn1 = ""
	btn2 = ""
	yellow = GPIO.input(17)
	red = GPIO.input(18)

	if not yellow:
		btn1 = "Turn on Yellow"
	elif yellow:
		btn1 = "Turn off Yellow"
	if not red:
		btn2 = "Turn on Red"
	elif red:
		btn2 = "Turn off Red"

	if request.method == "POST":
		val = request.form.get("submitBtn")
		print(val)
		if val == "You clicked 1!" and not yellow:
			msg1 = request.form.get("submitBtn")
			GPIO.output(17,GPIO.HIGH)
			yellow = False
			btn1 = "Turn off Yellow"
		elif val == "You clicked 1!" and yellow:
			msg1 = request.form.get("submitBtn")
                        GPIO.output(17,GPIO.LOW)
			yellow = True
			btn1 = "Turn on Yellow"
		elif val == "You clicked 2!" and not red:
			msg2 = request.form.get("submitBtn")
			GPIO.output(18,GPIO.HIGH)
			red = False
			btn2 = "Turn off Red"
		elif val == "You clicked 2!" and red:
			msg2 = request.form.get("submitBtn")
			GPIO.output(18,GPIO.LOW)
			red = True
			btn2 = "Turn on Red"
	else:
		GPIO.output(17,GPIO.LOW)
		msg1 = "Button 1: No click yet."
		GPIO.output(18,GPIO.LOW)
		msg2 = "Button 2: No click yet."
	return render_template("index.html", msg1=msg1, msg2=msg2, btn1=btn1, btn2=btn2)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80)
