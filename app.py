from flask import Flask, render_template

# Create the app and tell Flask to use the current directory for templates
app = Flask(__name__, template_folder='.')


@app.route('/')
def index():
	return render_template('index.html')


if __name__ == '__main__':
	# Run on all interfaces so it's accessible from other devices if needed
	app.run(host='0.0.0.0', port=5000, debug=True)

