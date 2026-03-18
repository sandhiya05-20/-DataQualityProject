from flask import Flask, jsonify, request, render_template, send_from_directory
import mysql.connector
import re

app = Flask(__name__, template_folder='../frontend', static_folder='../frontend', static_url_path='')

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Root@123",
        database="DataQualityDB"
    )

def convert_dates(record):
    for key in record:
        if hasattr(record[key], 'isoformat'):
            record[key] = str(record[key])
    return record

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/records', methods=['GET'])
def get_records():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Main_Data_Record")
    records = cursor.fetchall()
    cursor.close()
    db.close()
    return jsonify([convert_dates(r) for r in records])

@app.route('/api/quarantine', methods=['GET'])
def get_quarantine():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Quarantine_Record")
    records = cursor.fetchall()
    cursor.close()
    db.close()
    return jsonify([convert_dates(r) for r in records])

@app.route('/api/health', methods=['GET'])
def get_health():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Health_Metrics")
    metrics = cursor.fetchone()
    cursor.close()
    db.close()
    return jsonify(convert_dates(metrics))

@app.route('/api/logs', methods=['GET'])
def get_logs():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT cl.log_id, mdr.name, vr.rule_name, cl.action_taken, cl.timestamp
        FROM Cleanup_Log cl
        JOIN Main_Data_Record mdr ON cl.record_id = mdr.record_id
        JOIN Validation_Rule vr ON cl.rule_id = vr.rule_id
    """)
    logs = cursor.fetchall()
    cursor.close()
    db.close()
    return jsonify([convert_dates(r) for r in logs])

@app.route('/api/records', methods=['POST'])
def add_record():
    data = request.json
    name = data['name']
    email = data['email']
    phone = data['phone']

    issues = []

    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        issues.append('Invalid Email Format')

    if not re.match(r'^\d{10}$', phone):
        issues.append('Invalid Phone Number')

    if not name.strip():
        issues.append('Empty Name')

    db = get_db()
    cursor = db.cursor()

    if issues:
        cursor.execute("""
            INSERT INTO Main_Data_Record (name, email, phone, status)
            VALUES (%s, %s, %s, %s)
        """, (name, email, phone, 'QUARANTINED'))
        db.commit()
        record_id = cursor.lastrowid

        for issue in issues:
            cursor.execute("""
                INSERT INTO Quarantine_Record (record_id, raw_name, raw_email, raw_phone, issue_type)
                VALUES (%s, %s, %s, %s, %s)
            """, (record_id, name, email, phone, issue))
            cursor.execute("""
                INSERT INTO Cleanup_Log (record_id, rule_id, action_taken)
                VALUES (%s, %s, %s)
            """, (record_id, 1, 'QUARANTINED'))

        db.commit()
        cursor.close()
        db.close()
        return jsonify({'message': 'Record has issues and was quarantined!'})

    else:
        cursor.execute("""
            INSERT INTO Main_Data_Record (name, email, phone, status)
            VALUES (%s, %s, %s, %s)
        """, (name, email, phone, 'VALID'))
        db.commit()
        record_id = cursor.lastrowid

        cursor.execute("""
            INSERT INTO Cleanup_Log (record_id, rule_id, action_taken)
            VALUES (%s, %s, %s)
        """, (record_id, 1, 'VALIDATED'))
        db.commit()
        cursor.close()
        db.close()
        return jsonify({'message': 'Record added successfully!'})

@app.route('/admin-login')
def admin_login():
    return render_template('admin-login.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)