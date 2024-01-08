from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

# Configure MongoDB
app.config['MONGO_URI'] = 'mongodb://localhost:27017/University_db'
mongo = PyMongo(app)

# Faculty collection in MongoDB
faculty_collection = mongo.db.faculty

# Route for adding a new faculty
@app.route('/faculty', methods=['POST'])
def add_faculty():
    try:
        faculty_data = request.json
        faculty_collection.insert_one(faculty_data)
        return jsonify({'message': 'Faculty added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route for updating an existing faculty
@app.route('/faculty/<faculty_id>', methods=['PUT'])
def update_faculty(faculty_id):
    try:
        faculty_data = request.json
        result = faculty_collection.update_one({"faculty_id": faculty_id}, {"$set": faculty_data})
        if result.matched_count > 0:
            return jsonify({'message': 'Faculty updated successfully'}), 200
        else:
            return jsonify({'message': 'Faculty not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route for deleting an existing faculty
@app.route('/faculty/<faculty_id>', methods=['DELETE'])
def delete_faculty(faculty_id):
    try:
        result = faculty_collection.delete_one({"faculty_id": faculty_id})
        if result.deleted_count > 0:
            return jsonify({'message': 'Faculty deleted successfully'}), 200
        else:
            return jsonify({'message': 'Faculty not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route for retrieving all faculty
@app.route('/faculty', methods=['GET'])
def get_all_faculty():
    try:
        faculty_data = list(faculty_collection.find({}, {'_id': 0}))
        return jsonify(faculty_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
