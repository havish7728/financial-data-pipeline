from flask import Flask, request, jsonify
from models import db, init_db, Transaction
from etl import extract_data, transform_data, load_data
from aws_utils import upload_to_s3
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost/financial_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app)

@app.route('/')
def home():
    return "Financial Data Pipeline Running!"

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    data = request.json
    transaction = Transaction(amount=data['amount'], category=data['category'])
    db.session.add(transaction)
    db.session.commit()
    return jsonify({"message": "Transaction added successfully!"})

@app.route('/run_etl', methods=['GET'])
def run_etl():
    df = extract_data()
    transformed_df = transform_data(df)
    output_file = load_data(transformed_df)
    s3_url = upload_to_s3(output_file, "financial-data-bucket-1")
    return jsonify({"message": "ETL completed!", "s3_url": s3_url})

if __name__ == "__main__":
    app.run(debug=True)