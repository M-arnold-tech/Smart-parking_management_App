# Will handle the reservation, viewing and cancelling

from flask import Blueprint, request, jsonify
from process.reservations import reserve_spot, cancel_reservation, get_driver_reservations, reservation_checkout

reservation_bp = Blueprint("reservation_bp", __name__)

# === BOOK RESERVATION ===
@reservation_bp.route("/book", methods=["POST"])
def book_reservation():
  data = request.get_json()
  if not data:
    return jsonify({"success": False, "message": "Missing JSON Data."}), 400
  
  result = reserve_spot(data)
  return jsonify(result), 200 if result.get("success") else 400

# ===CANCEL RESERVATION ===
@reservation_bp.route("/cancel", methods=["PUT"])
def cancel_reservation_route():
  data = request.get_json()
  if not data:
    return jsonify({"success": False, "message": "Missing JSON Data."}), 400
  result = cancel_reservation(data)
  return jsonify(result), 200 if result.get("success") else 400

# === GET DRIVER RESERVATIONS ===
@reservation_bp.route("/driver/<int:driver_id>", methods=["GET"])
def get_reservation_for_driver(driver_id):
  result = get_driver_reservations(driver_id)
  return jsonify(result), 200 if result.get("success") else 404

# === CHECKOUT RESERVATION ===
@reservation_bp.route("/checkout", methods=["PUT"])
def checkout_reservation_route():
  data = request.get_json()
  if not data:
    return jsonify({"success": False, "message": "Missing JSON Data."}), 400
  
  result = reservation_checkout(data)
  return jsonify(result), 200 if result.get("success") else 400
