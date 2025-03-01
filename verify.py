import requests
from bs4 import BeautifulSoup

# Base URL (Update if necessary)
BASE_URL = "https://registration-verification-official.onrender.com"

# Extracting form ID from the HTML
FORM_ID = "2LgGsJ"  # Found inside <div id="form-id-div">

# Registration endpoint
REGISTER_URL = f"{BASE_URL}/form/{FORM_ID}"

# Headers with User-Agent (Avoid getting blocked)
HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# User details for registration
user_data = {
    "name_d": "Laudu",
    "college_name_d": "Agra University",
    "graduation_year_d": "2024",
    "age_d": "55",
    "point_of_contact_(poc)_d": "Kantar",
    "phone": "9682490015",
    "gender_d": "Male",
    "otp_needed": "True",  # OTP is required for registration
    "form_id": FORM_ID
}

# Step 1: Send Registration Request
print("\n🚀 Sending Registration Request...")
register_response = requests.post(REGISTER_URL, json=user_data, headers=HEADERS)

# Debugging: Print raw response
print("\n🔹 Raw Response Status:", register_response.status_code)
print("🔹 Raw Response Text:", register_response.text)

try:
    register_json = register_response.json()  # Parse JSON response
    print("\n✅ Registration Response:", register_json)

    # Step 2: Check if OTP is required
    if "message" in register_json and "OTP sent" in register_json["message"]:
        otp = input("\n📩 Enter the OTP received on your phone: ")

        # OTP Verification Endpoint
        VERIFY_URL = f"{BASE_URL}/verify-otp"

        otp_data = {
            "phone": user_data["phone"],
            "otp": otp
        }

        # Step 3: Send OTP Verification Request
        print("\n🚀 Verifying OTP...")
        otp_response = requests.post(VERIFY_URL, json=otp_data, headers=HEADERS)

        try:
            otp_json = otp_response.json()
            print("\n✅ OTP Verification Response:", otp_json)

            # Check if OTP was accepted
            if "message" in otp_json and "success" in otp_json["message"].lower():
                print("\n🎉 Registration Completed Successfully!")
            else:
                print("\n❌ OTP Verification Failed. Try Again.")

        except requests.exceptions.JSONDecodeError:
            print("\n❌ Error: OTP verification response is not valid JSON. Server might be rejecting the request.")

except requests.exceptions.JSONDecodeError:
    print("\n❌ Error: The registration response is not valid JSON. Check the URL and API documentation.")
	
