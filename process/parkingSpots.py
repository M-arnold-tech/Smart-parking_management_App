# parkingSpots.py will handle all parking spots management and availability

# In-memory data before db

parking_lots = []
reservations = []
def add_parking_spot(data):
  """
  Parking operator will add a new parking location with the capacity
  """
  spot_address = data.get("spotAddress")
  capacity = data.get("spot_capacity", 1)

  if not spot_address:
    return{"success": False, "message": "Spot address is required!"}
  
  # TODO: in real db setup, you will check:
  # SELECT * FROM parkingSpot WHERE spotAddress = %s
  # If it exists -> update capacity instead of duplicate insert

  # TODO: If not exists, insert:
  # INSERT INTO parkingSpot (spotAddress, spot_capacity) VALUES (%s, %s)

  for lot in parking_lots:
    if lot["address"].lower() == spot_address.lower():
      return {"success": False, "message": "Parking lot already exists"}
  
  new_lot = {
    "spot_id": len(parking_lots) + 1,
    "address": spot_address,
    "spot_capacity": capacity,
  }
  parking_lots.append(new_lot)
  return {"success": True, "message": f"Parking lot '{spot_address}' added successfully", "lot": new_lot}

def get_parking_spots():
  """
  Shows all parking locations with current availability.
  with each including:
    - Total capacity
    - Number of occupied spots
    - Number of available spots
  """
  lots = []
  for lot in parking_lots:
    # Count occupied spots
    occupied = len([r for r in reservations if r.get("spot_id") == lot["spot_id"] and r.get("status") == "active"])
    available = max(lot["spot_capacity"] - occupied, 0)
    lots.append({
      "spot_id": lot["spot_id"],
      "address": lot["address"],
      "spot_capacity": lot["spot_capacity"],
      "occupied_spots": occupied,
      "available_spots": available
    })

    return {"success": True, "parking_lots": lots}
  

def update_parking_spot(data):
  """
  The parking operator can update an existing parking location:
  Can update the address name of the parking lot or the capacity of the parking lot.
  """
  spot_id = data.get("spot_id")
  new_address = data.get("spotAddress")
  new_capacity = data.get("spot_capacity")

  if not spot_id:
    return {"success": False, "message": "Spot ID is required"}
  
  # TODO: Example query:
  # UPDATE parkingSpot SET spotAddress=%s, spot_capacity=%s WHERE spot_id=%s

  updated_fields = []
  if new_address:
    updated_fields.append(f"address='{new_address}'")
  if new_capacity:
    updated_fields.append(f"capacity={new_capacity}")
  
  updates = ", ".join(updated_fields) if updated_fields else "No changes"
  return {"success": True, "message": f"Spot updated successfully: {updates}"}


def delete_parking_spot(spot_id):
  """Parking operator can delete a parking spot if necessary."""

  if not spot_id:
    return {"success": False, "message": "Spot ID required"}
  
  # TODO: Execute DELET FROM parkingSpot WHERE spot_id = %s
  return {"success": True, "message": f"Parking spot with ID {spot_id} deleted successfully!"}
  
