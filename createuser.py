<<<<<<< HEAD
from main import SessionLocal, User, get_password_hash

# Create a new database session
db = SessionLocal()

# Set your new user's details
username = "testuser"
password = "testpassword"

# Check if user already exists
existing_user = db.query(User).filter(User.username == username).first()
if existing_user:
    print("User already exists!")
else:
    new_user = User(
        username=username,
        hashed_password=get_password_hash(password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    print(f"User '{username}' created successfully!")
=======
from main import SessionLocal, User, get_password_hash

# Create a new database session
db = SessionLocal()

# Set your new user's details
username = "testuser"
password = "testpassword"

# Check if user already exists
existing_user = db.query(User).filter(User.username == username).first()
if existing_user:
    print("User already exists!")
else:
    new_user = User(
        username=username,
        hashed_password=get_password_hash(password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    print(f"User '{username}' created successfully!")
>>>>>>> e4ad3f58ae9bd8d2dcd9942e5013182e5930aeeb
