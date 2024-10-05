from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://canaryproject_user:tBvTtZE65hv2WdYnTreIiXJwxaRq7UEh@dpg-cs029d3tq21c738t145g-a/canaryproject'
db = SQLAlchemy(app)

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email_id = db.Column(db.String, nullable=False)
    public_ip = db.Column(db.String, nullable=False)
    user_agent = db.Column(db.String, nullable=False)
    access_time = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Log {self.email_id}>'
    
@app.route("/")
def home():
    return "Welcome to the Home Page!"

@app.route('/api/logs', methods=['GET'])
def get_logs():
    logs = Log.query.all()
    return jsonify([{'email_id': log.email_id, 'public_ip': log.public_ip} for log in logs])

@app.route('/api/logs', methods=['POST'])
def create_log():
    data = request.get_json()  # Get JSON data from the request
    access_time = data.get('access_time', datetime.utcnow())  # Get access_time from the request or use current time
    new_log = Log(
        email_id=data['email_id'],
        public_ip=data['public_ip'],
        user_agent=data['user_agent'],
        access_time=datetime.utcnow() # Include access_time in the log entry
    )
    db.session.add(new_log)  # Add the new log to the session
    db.session.commit()  # Commit the transaction
    return jsonify({'message': 'Log created successfully!'}), 201

if __name__ == '__main__':
    app.run()
