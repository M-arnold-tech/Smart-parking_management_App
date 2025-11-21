# Will handle the routes for parking spots and Lots management

from flask import Blueprint, request, jsonify
from process.parkingSpots import add_parking_spot, get_available_parking_spots

parking_bp = Blueprint("parking_bp", __name__)

@parking_bp.route("/add", methods=["POST"])
def add_parking_spot_route():
  data = request.get_json()
  result = add_parking_spot(data)
  return jsonify(result)

@parking_bp.route("/available", methods=["GET"])
def available_parking_spots_route():
  result = get_available_parking_spots()
  return jsonify(result)
