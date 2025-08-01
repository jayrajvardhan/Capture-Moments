from flask import Flask, render_template, request, jsonify

# Step 1: Create the Flask app instance
app = Flask(__name__)

# Step 2: Dummy data for photographers (simulating database)
photographers = [
    {"id": "p1", "name": "Amit Lensman", "skills": ["Wedding", "Portrait"], "image": "amit.jpg"},
    {"id": "p2", "name": "Sana Clickz", "skills": ["Fashion", "Event"], "image": "sana.jpg"},
    {"id": "p3", "name": "Peter", "skills": ["Video editing", "creativity"], "image": "peter.jpg"},
    {"id": "p4", "name": "Richard Johnson", "skills": ["Style Development", "Designing"], "image": "Richard.jpg"}
]

# Step 3: Dummy availability data mapped by photographer ID
availability_data = {
    "p1": ["2025-06-20", "2025-06-23"],
    "p2": ["2025-06-19", "2025-06-22"],
    "p3": ["2025-07-18", "2025-07-27"],
    "p4": ["2025-08-12", "2025-08-19"]
}

#Home page
@app.route('/')
def home():
    return render_template('home.html')

#Booking from route
@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        photographer_id = request.form.get('photographer_id')
        user_id = request.form.get('user_id')
        date = request.form.get('date')
        return f"<h2 style='Color:green'>Booking Confirmed! For {photographer_id} on {date}.</h2>"
    return render_template('book.html')


#View photographers
@app.route('/show-photographers')
def show_photographers():
    return render_template('photographers.html', photographers=photographers, availability_data=availability_data)

if __name__ == '__main__' :
    app.run(debug=True)