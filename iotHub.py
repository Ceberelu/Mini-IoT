from flask import Flask
from flask import render_template
import subprocess

app = Flask(__name__)

plug = {
	'plug_b': { 
		'on': '16765268', 
		'off': '16765265'
	},
	'plug_c': {
		'on': '16766036',
		'off': '16766033',
	}}
cmd = ['sudo', '/home/pi/tools/433Utils/RPi_utils/codesend']

def plug_action(plug_name, action):
	if plug_name not in plug:
		print plug_name + "not in" + plug
		return
	if action not in plug[plug_name]: 
		print action + "not in" + plug[plug_name]
		return
	
	# returns a list with one element
	
	return [plug[plug_name][action]]

@app.route('/')
def index(name = None):
	return render_template('index.html', name = name)

@app.route('/b_on')
def plug_b_on():
	try:
		subprocess.check_call(cmd + plug_action('plug_b','on'))
	except CalledProcessError:
		return CalledProcessError
	return render_template('index.html')

@app.route('/b_off')
def plug_b_off():
	subprocess.call(cmd + plug_action('plug_b','off'))
	return render_template('index.html')

@app.route('/c_on')
def plug_c_on():
	subprocess.call(cmd + plug_action('plug_c','on'))
	return render_template('index.html')

@app.route('/c_off')
def plug_c_off():
	subprocess.call(cmd + plug_action('plug_c','off'))
	return render_template('index.html')
