# reservation.py will work together with parkingSpots.py module to manage bookings and avilability of parking lots

from database import get_connection
from process.parkingSpots import update_parking_spot_availability

# ===CREATE A RESERVATION===

def reserve_spot(data):
  """This module is for reservation by drivers"""

  driver_id = data.get("driver_id")
  spot_id = data.get("spot_id")
  start_time = data.get("start_time")
  end_time = data.get("end_time")
  total_price = data.get("total_price")

  # VALIDATION
  if not all([driver_id, spot_id, start_time, end_time, total_price]):
    return{"success": False, "message": "All fields are required!"}
  

  conn = get_connection()
  if not conn:
    return{"success": False, "message": "Database coonection failed!"}
  cursor = conn.cursor(dictionary=True)

  # check if the spot exists and is available
  cursor.execute("SELECT * FROM parking_spot WHERE spot_id=%s AND is_available=1", (spot_id,))
  spot = cursor.fetchone()
  if not spot:
    cursor.close()
    conn.close()
    return {"success": False, "message": "Parking spot not available!"}
  
  # Create reservation
  cursor.execute(
    """
    INSERT INTO reservation (driver_id, spot_id, start_time, end_time, total_price, status)
    VALUES (%s, %s, %s, %s, %s, 'active')
    """,
    (driver_id, spot_id, start_time, end_time, total_price)
  )
  conn.commit()
  
  # Get new reservation ID
  res_id = cursor.lastrowid


  # Updating available spots
  new_available_spots = spot["available_spots"] - 1
  update_parking_spot_availability(spot_id, new_available_spots)
  
  cursor.close()
  conn.close()
  return{
    "success": True, 
    "message": "Reservation successful.",
    "reservation_id": res_id,
    "spot_id": spot_id,
    "available_spots": new_available_spots
  }


# === CANCELLING A RESERVATION ===

def cancel_reservation(data):
  """This module is for cancelling a reservation made"""
  res_id = data.get("res_id")

  if not res_id:
    return{"success": False, "message": "reservation Id is required."}
  
  conn = get_connection()
  if not conn:
    return {"success": False, "message": "database connection failed!"}
  cursor = conn.cursor(dictionary=True)

  # Find reservation
  cursor.execute("SELECT * FROM reseervation WHERE res_id=%s AND status='active'", (res_id,))
  res = cursor.fetchone()
  if not res:
    cursor.close()
    conn.close()
    return{"success": False, "message": "Active reservation not found!"}
  
  # Cancel
  cursor.execute("UPDATE reservation SET status='cancelled' WHERE res_id=%s", (res_id))
  conn.commit()

  # Free parking spot
  cursor.execute("SELECT * FROM parking_spot WHERE spot_id=%s", (res["spot_id"],))
  spot = cursor.fetchone()
  if spot:
    available_spots = spot["available_spots"] + 1
    update_parking_spot_availability(res["spot_id"], available_spots)
  
  cursor.close()
  conn.close()
  return{"success": True, "message": "Reservation cancelled successfully!"}

# === VIEWING DRIVER'S RESERVATIONS ===

def get_driver_reservations(driver_id):
  """Return all reservation made by a driver"""

  if not driver_id:
    return{"success": False, "message": "Driver ID Is required."}
  
  conn = get_connection()
  if not conn:
    return{"Success": False, "message": "Database connection failed!"}
  cursor = conn.cursor(dictionary=True)

  cursor.execute("""
    SELECT r.res_id, r.spot_id, p.location, e.start_time, r.end_time, r.total_price, r.status
    FROM reservation r
    JOIN parking_spot p ON r.spot_id = p.spot_id
    WHERE r.driver_id = %s
    ORDER BY r.start_time DESC
  """, (driver_id))

  reservations = cursor.fetchall()
  cursor.close()
  conn.close()

  if not reservations:
    return {"success": True, "reservations": [], "message": "No reservations found"}
  
  return {"success": True, "reservations": reservations}
