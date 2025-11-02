# parkingSpots.py will handle all parking spots management and availability

from database import get_connection

# === ADD A PARKING LOT ===

def add_parking_spot(data):
  """
  Parking operator will add a new parking location with the capacity
  """
  operator_id = data.get("operator_id")
  location = data.get("location")
  price_per_hour = data.get("price_per_hour")
  total_spots = data.get("total_spots")

  # Validation
  if not all([operator_id, location, price_per_hour, total_spots]):
    return {"success": False, "message": "All fields are required!"}
  
  conn = get_connection()
  if not conn:
    return {"success": False, "message": "Database connection failed!"}
  
  cursor = conn.cursor(dictionary=True)

  # Checking for duplicates
  cursor.execute(
    "SELECT * FROM parking_spot WHERE operator_id=%s AND location=%s",
    (operator_id, location)
  )
  if cursor.fetchone():
    cursor.close()
    conn.close()
    return{"success": False, "message": "Parking lot already exists!"}
  
  # Add parking lot
  cursor.execute(
    """
    INSERT INTO parking_spot (operaotr_id, location, price_per_hour, total_spots, available_spots, is_available)
    """,
    (operator_id, location, price_per_hour, total_spots)
  )
  conn.commit()
  cursor.close()
  conn.close()

  return {"success": True, "message": f"Parking lot '{location}' added successfully!"}

# === GET ALL AVAILABLE PARKING SPOTS ===

def get_available_parking_spots():
  """Fetches all parking lots with availble parking spots."""
  conn = get_connection()
  if not conn:
    return {"success": False, "message": "Database connection failed!"}
  cursor = conn.cursor(dictionary=True)

  cursor.execute("""
      SELECT spot_id, location, price_per_hour, total_spots, available_spots
      FROM parking_spot
      WHERE is_available = 1
      ORDER BY location ASC
  """)
  spots = cursor.fetchall()

  cursor.close()
  conn.close()

  if not spots:
    return {"success": True, "parking_spots": [], "message": "No available spots found!"}
  
  return {"success": True, "parking_spots": spots}


# UPDATE PARKING SPOT AVAILABILITY

def update_parking_spot_availability(spot_id, available_spots):
  """Updates the number of available spots in a parking lot"""

  conn = get_connection()
  if not conn:
    return{"success": False, "message": "DATABASE connection failed!"}
  
  cursor = conn.cursor(dictionary=True)

  # Get total spots
  cursor.execute("SELECT total_spots FROM parking_spot WHERE spot_id=%s", (spot_id,))
  spot = cursor.fetchone()

  if not spot:
    cursor.close()
    conn.close()
    return {"success": False, "message": "Parking spot not found!"}
  
  total_spots = spot["total_spots"]
  is_available = 1 if available_spots > 0 else 0

  # Update spot
  cursor.execute("""
    UPDATE parking_spot
    SET available_spots = %s, is_available = %s
    WHERE spot_id = %s
  """, (available_spots, is_available, spot_id))

  conn.commit()
  cursor.close()
  conn.close()
  return {"success": True, "message": "Parking availability update successfully!"}
