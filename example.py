from database import get_connection
from werkzeug.security import generate_password_hash

def example_data():
  conn = get_connection()
  if not conn:
    print("Database connection failed!")
    return
  
  cursor = conn.cursor()

  # === Add parking operator ===
  operator_name = "Smartspaces"
  operator_email = "operator@smartspaces.com"
  operator_phone = "0786532598"
  operator_password = generate_password_hash("Admin123")

  cursor.execute("""
     SELECT operator_id FROM parking_operator WHERE email = %s
  """, (operator_email,))
  operator_exists = cursor.fetchone()

  if not operator_exists:
    cursor.execute("""
        INSERT INTO parking_operator (operator_name, email, password_hash, phone_number)
        VALUES (%s, %s, %s, %s)
    """, (operator_name, operator_email, operator_password, operator_phone))
    conn.commit()
    print(f"Added oprator: {operator_name}")
  else:
    print(f"Operator '{operator_name}' already exists.")
  
  # === Add driver ===
  driver_username = "Mnhd"
  driver_email = "mnhd@gmail.com"
  driver_phone = "0788986532"
  driver_plate = "RAF505E"
  driver_password = generate_password_hash("Secret123")

  cursor.execute("""
      SELECT driver_id FROM driver WHERE username = %s OR email = %s
  """, (driver_username, driver_email))
  driver_exists = cursor.fetchone()

  if not driver_exists:
    cursor.execute("""
        INSERT INTO driver (username, email, password_hash, phone_number, vehicle_plate)
        VALUES (%s, %s, %s, %s, %s)
    """, (driver_username, driver_email, driver_password, driver_phone, driver_plate))

    conn.commit()
    print(f"Added driver: {driver_username}")
  else:
    print(f"Driver '{driver_username}' already exists.")
  
  # === Add parking Spot ===
  cursor.execute("SELECT operator_id FROM parking_operator WHERE email=%s", (operator_email,))
  operator = cursor.fetchone()
  if operator:
    operator_id = operator[0]
    location = "Downtown Bus Park"
    price_per_hour = 500
    spot_number = 70

    cursor.execute("""
        SELECT spot_id FROM parking_spot WHERE operator_id = %s AND location = %s
    """, (operator_id, location))
    spot_exists = cursor.fetchone()

    if not spot_exists:
      cursor.execute("""
          INSERT INTO parking_spot (operator_id, location, price_per_hour, spot_number, is_available)
          VALUES (%s, %s, %s, %s, 1)
      """, (operator_id, location, price_per_hour, spot_number))
      conn.commit()
      print(f"Added parking lot: {location}")
    else:
      print(f"Parking lot '{location}' already exists.")
  else:
    print("Operator not found. Could not add Parking lot.")
  
  cursor.close()
  conn.close()
  print("\n Example is Complete!")

if __name__ == "__main__":
  example_data()
