from flask import Flask, render_template, request
import logging
from datetime import datetime

app = Flask(__name__)

# Set up logging to a file
logging.basicConfig(filename='visitor_logs.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

@app.route('/')
def index():
    # Get the visitor's IP address and User-Agent
    ip_address = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0]
    user_agent = request.user_agent.string
    
    # Log the IP address and User-Agent to the log file
    logging.info(f"IP Address: {ip_address}, User-Agent: {user_agent}")
    
    # Render the index page (index.html)
    return render_template('index.html')

@app.route('/print')
def print_log():
    # Read the log file and display its contents
    try:
        with open('visitor_logs.txt', 'r') as log_file:
            logs = log_file.readlines()
    except FileNotFoundError:
        logs = ['No logs found.']
    
    # Render the print page (print.html)
    return render_template('print.html', logs=logs)

if __name__ == '__main__':
    app.run(debug=True)
