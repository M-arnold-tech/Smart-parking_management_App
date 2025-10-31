# authentication.py will handle signup and login processes for both drivers and parking operators.

# Temporary in-memory data before db setup

drivers = []
operators = []


def signup_driver(data):
  """Registration of a new driver."""
  username = data.get("username")
  vehicle = data.get("vehicle")
  phone = data.get("phoneNumber")

  # TODO: check if the driver already exists in the db
  # TODO: add new driver in the db if they don't exist
  if not username or not vehicle or not phone:
    return {"success": False, "message": "All fields are required"}
  
  for d in drivers:
    if d["username"] == username:
      return {"success": False, "message": "Driver already exists"}
    
  new_driver = {
    "driver_id": len(drivers) + 1,
    "username": username,
    "vehicle": vehicle,
    "phoneNumber": phone,
  }
  drivers.append(new_driver)
  return {"success": True, "message": "Driver signup successful", "driver": new_driver}

def signup_operator(data):
  """Registration of a new parking operator."""
  username = data.get("username")
  phone = data.get("phoneNumber")

  # TODO: check if operator already exists in the db
  # TODO: insert new operator in the db if they don't exist
  if not username or not phone:
    return {"success": False, "message": "All fields are required"}
  
  for o in operators:
    if o["username"] == username:
      return {"success": False, "message": "Operator already exists"}
    
  new_operator = {
    "operator_id": len(operators) + 1,
    "username": username,
    "phoneNumber": phone, 
  }
  operators.append(new_operator)
  return {"success": True, "message": "Operator signup successfully", "operator": new_operator}


def login_user(data):
  """Authentication of the user (driver or operator)"""
  username = data.get("username")
  role = data.get("role")

  # TODO: query correct table by role
  # TODO: verify if user exists
  if not username or not role:
    return {"success": False, "message": "Username and role are required!"}
  
  if role == "driver":
    user = next((d for d in drivers if d["username"] == username), None)
  elif role == "operator":
    user = next((o for o in operators if o["username"] == username), None)
  else:
    return {"success": False, "message": "INvalid role"}
  
  if user:
    return {"success": True, "message": f"{role.capitalize()} login Successful", "user": user}
  return {"success": False, "message": "User not found"}
