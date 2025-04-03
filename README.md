# **Financial Data Pipeline 🚀**  

A **Flask-based** data pipeline that extracts, transforms, and loads (ETL) financial transactions into a **MySQL database** and stores processed data in **AWS S3**.  

---

## **📌 Features**
✅ **Data Ingestion** – Uploads financial transaction CSV files.  
✅ **ETL Process** – Extracts, transforms, and loads data into MySQL.  
✅ **AWS S3 Integration** – Uploads processed data to AWS S3.  
✅ **REST API** – Flask endpoints for data processing and retrieval.  
✅ **MySQL Storage** – Saves transactions for further analysis.  

---

## **📁 Project Structure**
```
financial-data-pipeline/
│── app.py                  # Flask application
│── config.py               # Database & AWS configuration
│── models.py               # Database schema (SQLAlchemy)
│── database.py             # MySQL connection
│── etl.py                  # ETL pipeline for data processing
│── aws_utils.py            # AWS S3 file upload functions
│── templates/              # HTML for visualization (Optional)
│── static/                 # CSS, JS files (Optional)
│── requirements.txt        # Dependencies
│── sample_data.csv         # Sample test data
│── README.md               # Project Documentation
```

---

## **⚙️ Setup & Installation**
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/havish7728/financial-data-pipeline.git
cd financial-data-pipeline
```

### **2️⃣ Create Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Configure MySQL Database**
1. Start MySQL and create a database:
   ```sql
   CREATE DATABASE financial_db;
   ```
2. Update `config.py` with MySQL credentials.

### **5️⃣ Set AWS Credentials (For S3 Upload)**
```sh
export AWS_ACCESS_KEY="your-access-key"
export AWS_SECRET_KEY="your-secret-key"
export AWS_BUCKET_NAME="your-bucket-name"
```
or add them to `.env` file.

---

## **🚀 Running the Application**
### **Start Flask Server**
```sh
python app.py
```
The server will start at **http://127.0.0.1:5000/**.

---

## **📌 API Endpoints**
### **1️⃣ Home Page**
- **URL:** `/`
- **Method:** `GET`
- **Response:** `"Financial Data Pipeline Running!"`

### **2️⃣ Add a Transaction**
- **URL:** `/add_transaction`
- **Method:** `POST`
- **Body (JSON):**
  ```json
  {
    "amount": 100.50,
    "category": "Groceries"
  }
  ```
- **Response:**
  ```json
  { "message": "Transaction added successfully!" }
  ```

### **3️⃣ Run ETL Pipeline**
- **URL:** `/run_etl`
- **Method:** `GET`
- **Response:**
  ```json
  { "message": "ETL completed!", "s3_url": "https://s3.amazonaws.com/your-bucket/file.csv" }
  ```

---

## **📊 Sample CSV Format**
Create a sample CSV file `sample_data.csv`:
```csv
id,date,amount,category
1,2024-03-30,100.50,Groceries
2,2024-03-30,50.00,Transport
3,2024-03-30,200.00,Entertainment
```

---