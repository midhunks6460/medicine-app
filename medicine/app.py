from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

medicines = [
    {'id': 1, 'name': 'Aspirin', 'dosage': '500mg'},
    {'id': 2, 'name': 'Ibuprofen', 'dosage': '200mg'},
    {'id': 3, 'name': 'Paracetamol', 'dosage': '650mg'},
]

@app.route('/')
def index():
    return render_template('index.html', medicines=medicines)

@app.route('/add', methods=['POST'])
def add_medicine():
    data = request.get_json()
    new_medicine = {
        'id': len(medicines) + 1,
        'name': data['name'],
        'dosage': data['dosage']
    }
    medicines.append(new_medicine)
    return jsonify(new_medicine), 201

@app.route('/search', methods=['POST'])
def search_medicine():
    search_term = request.get_json()['searchTerm']
    results = [medicine for medicine in medicines if search_term.lower() in medicine['name'].lower()]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
