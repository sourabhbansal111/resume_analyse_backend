"""
Script to auto-create the first admin user (PRODUCTION SAFE)
"""
from database import Database
from auth import hash_password
import os

def create_admin():
    """Create admin user automatically from ENV"""
    db = Database()

    print("=" * 60)
    print("Auto Admin Creator")
    print("=" * 60)

    # ✅ Get credentials from ENV (Render dashboard)
    email = os.environ.get("ADMIN_EMAIL")
    password = os.environ.get("ADMIN_PASSWORD")
    name = os.environ.get("ADMIN_NAME", "Super Admin")

    if not email or not password:
        print("⚠️ ADMIN_EMAIL or ADMIN_PASSWORD not set.")
        print("⚠️ Skipping admin creation.")
        return

    try:
        # ✅ Check if user already exists
        existing_user = db.get_user_by_email(email)
        if existing_user:
            print("✅ Admin already exists. Skipping creation.")
            return

        # ✅ Check if any admin already exists
        conn = db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM users WHERE role = ?", ("admin",))
        if cursor.fetchone():
            print("✅ Admin role already exists. Skipping creation.")
            conn.close()
            return
        conn.close()

        # ✅ Create admin
        password_hash = hash_password(password)
        user_id = db.create_user(email, password_hash, name, "admin")

        print("\n✅ Admin user created successfully!")
        print(f"   Email: {email}")
        print(f"   Name: {name}")
        print(f"   User ID: {user_id}")

    except Exception as e:
        print(f"❌ Admin creation failed: {str(e)}")

if __name__ == "__main__":
    create_admin()
