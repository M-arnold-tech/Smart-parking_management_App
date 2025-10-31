# reservation.py will work together with parkingSpots.py module to manage bookings and avilability of parking lots

from process.parkingSpots import parking_lots
reservations = []

def reserve_parkingSpot(data):
  """
  Allows a driver to reserve a parking spot in parking lot
  """
  driver_id = data.get("driver_id")
  spot_id = data.get("spot_id")

  if not driver_id or not spot_id:
    return {"success": False, "message": "Driver ID and spot ID are required!"}
  
  # Check if the parking lot exists
  parking_lot = next((p for p in parking_lots if p["spot_id"] == spot_id), None)
  if not parking_lot:
    return {"success": False, "message": "Parking lot not found"}
  
  # Count active reservations for the spot
  active_reservations = [r for r in reservations if r["spot_id"] == spot_id and r["status"] == "active"]

  if len(active_reservations) >= parking_lot["spot_capacity"]:
    return {"success": False, "message": "No available spots at this parking lot"}
  
  # Create a new reservation
  new_reservation = {
    "reservation_id": len(reservations) + 1,
    "driver_id": driver_id,
    "spot_id": spot_id,
    "address": parking_lot["address"],
    "status": "active"
  }
  reservations.append(new_reservation)
  return{
    "success": True,
    "message": f"reservation confirmed at {parking_lot['address']}",
    "reservation": new_reservation
  }

def view_reservations():
  """
  Returns a list of all reservations.
  """
  return{"success": True, "reservations": reservations}

def view_reservations_by_driver(driver_id):
  """
  Return all reservations made by a specific driver
  """
  driver_reservations = [r for r in reservations if r["driver_id"] -- driver_id]
  return {"success": True, "reservations": driver_reservations}

def cancl_reservation(data):
  """
  Driver can cancel reservation anytime.
  """
  reservation_id = data.get("reservation_id")
  if not reservation_id:
    return {"success": False, "message": "Reservation ID is required!"}
  
  for res in reservations:
    if res["reservation_id"] == reservation_id and res["status"] == "active":
      res["status"] = "cancelled"
      return {"success": True, "message": f"Reservation {reservation_id} cancelled successfully"}
    
  return {"success": False, "message": "Active reservation not found"}

def get_parking_availability():
  """
  Will handle availability for all parking lots based on reservation.
  """
  results = []
  for lot in parking_lots:
    active = len([r for r in reservations if r["spot_id"] == lot["spot_id"] and r["status"] == "active"])
    available = max(lot["spot_capacity"] - active, 0)
    results.append({
      "spot_id": lot["spot_id"],
      "address": lot["address"],
      "total_capacity": lot["spot_capacity"],
      "occupied": active,
      "available": available
    })
  return {"success": True, "parking_availability": results}
