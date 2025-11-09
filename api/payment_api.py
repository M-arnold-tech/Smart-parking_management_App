# Is the route for the payments

from flask import Blueprint, request, jsonify
from process.payment import initiate_payment, confirm_payment, get_payment_status

payment_bp = Blueprint("paymnet_bp", __name__)

# === INITIATE PAYMENT ===
@payment_bp.route("/initiate", methods=["POST"])
def payment_initiation():
  """
  Will helping in processing a payment for a reservation
  """

  data = request.get_json()
  if not data:
    return jsonify({"success": False, "message": "Missing JSON Data."}), 400
  
  result = initiate_payment(data)
  return jsonify(result), 200 if result.get("success") else 400


# === CONFIRM/FAIL PAYMENT ===
@payment_bp.route("/confirm", methods=["PUT"])
def payment_confirmation():
  """
  Will help to log confirmed payment
  """
  data = request.get_json()
  if not data:
    return jsonify({"success": False, "message": "Missing JSON Data."})
  
  result = confirm_payment(data)
  return jsonify(result), 200 if result.get("success") else 400


# === GET PAYMENT STATUS ===
@payment_bp.route("/status/<int:res_id>", methods=["GET"])
def payment_status(res_id):
  """Get payment info for a specific reservation."""
  result = get_payment_status(res_id)
  return jsonify(result), 200 if result.get("success") else 400
