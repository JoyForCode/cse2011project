from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://canaryproject_user:tBvTtZE65hv2WdYnTreIiXJwxaRq7UEh@dpg-cs029d3tq21c738t145g-a/canaryproject'
db = SQLAlchemy(app)

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email_id = db.Column(db.String, nullable=False)
    public_ip = db.Column(db.String, nullable=False)
    user_agent = db.Column(db.String, nullable=False)
    access_time = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Log {self.email_id}>'

@app.route('/api/logs', methods=['GET'])
def get_logs():
    logs = Log.query.all()
    return jsonify([{'email_id': log.email_id, 'public_ip': log.public_ip} for log in logs])

if __name__ == '__main__':
    app.run()
