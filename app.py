from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import datetime
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init marshmallow
ma = Marshmallow(app)

# Climate Class/Model
class Climate(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.String(20))
    rainfall = db.Column(db.String(10))
    temperature = db.Column(db.Float)

    def __init__(self, date, rainfall, temperature):
        self.date = date
        self.rainfall = rainfall
        self.temperature = temperature
    
# Climate Schema
class ClimateSchema(ma.Schema):
    class Meta:
        fields = ('id','date','rainfall','temperature')

# Init schema
climate_schema = ClimateSchema(strict=True)
climates_schema = ClimateSchema(many=True, strict=True)

# Add climate
@app.route('/climate', methods=['POST'])
def add_climate():
    date = request.json['date']
    rainfall = request.json['rainfall']
    temperature = request.json['temperature']

    new_climate = Climate(date, rainfall, temperature)

    db.session.add(new_climate)
    db.session.commit()

    return climate_schema.jsonify(new_climate)

# Get All Climates
@app.route('/climate', methods=['GET'])
def get_climates():
    all_climates = Climate.query.all()
    result = climates_schema.dump(all_climates)
    return jsonify(result.data)

# Get Single Climate
@app.route('/climate/<id>', methods=['GET'])
def get_climate(id):
    climate = Climate.query.get(id)
    return climate_schema.jsonify(climate)

# Update a Climate
@app.route('/climate/<id>', methods=['PUT'])
def update_climate(id):
    climate = Climate.query.get(id)

    date = request.json['date']
    rainfall = request.json['rainfall']
    temperature = request.json['temperature']
    
    climate.date = date
    climate.rainfall = rainfall
    climate.temperature = temperature
    
    db.session.commit()

    return climate_schema.jsonify(climate)

# Delete Climate
@app.route('/climate/<id>', methods=['DELETE'])
def delete_climate(id):
    climate = Climate.query.get(id)
    db.session.delete(climate)
    db.session.commit()

    return climate_schema.jsonify(climate)

# Run Server
if __name__ == '__main__':
    app.run(debug=True)
