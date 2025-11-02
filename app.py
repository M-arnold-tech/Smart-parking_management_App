from flask import Flask
from api.authentication_api import auth_bp
from api.parking_api import parking_bp
from api.reservation_api import reservation_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(parking_bp, url_prefix="/parking")
app.register_blueprint(reservation_bp, url_prefix="/reservation")

@app.route("/", methods=["GET"])
def home():
  return{"message": "Welcome to SmartSpaces"}

if __name__ == "__main__":
  app.run(debug=True)
