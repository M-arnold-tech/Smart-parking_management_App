# Will handle the reservation, viewing and cancelling

from flask import Blueprint, request, jsonify
from process.reservations import reserve_spot, cancel_reservation, get_driver_reservations

reservation_bp = Blueprint("reservation_bp", __name__)

@reservation_bp.route("/book", methods=["POST"])
def book_reservation():
  data = request.get_json()
  result = reserve_spot(data)
  return jsonify(result)

@reservation_bp.route("/cancel", methods=["PUT"])
def cancel_reservation_route():
  data = request.get_json()
  result = cancel_reservation(data)
  return jsonify(result)

@reservation_bp.route("/driver/<int:driver_id>", methods=["GET"])
def get_reservation_for_driver(driver_id):
  result = get_driver_reservations(driver_id)
  return jsonify(result)
