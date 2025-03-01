#!/bin/bash

# Generate Random Name
names=("Rahul" "Amit" "Suresh" "Priya" "Neha" "Vikram" "Anjali")
name_d=${names[$RANDOM % ${#names[@]}]}

# Generate Random College Name
colleges=("Delhi University" "IIT Bombay" "BITS Pilani" "Agra University" "Anna University")
college_name_d=${colleges[$RANDOM % ${#colleges[@]}]}

# Generate Random Graduation Year (Between 2015 and Current Year)
current_year=$(date +%Y)
graduation_year_d=$((RANDOM % (current_year - 2015 + 1) + 2015))

# Generate Random Age (Between 18 and 30)
age_d=$((RANDOM % 13 + 18))

# Generate Random Point of Contact
pocs=("Kantar" "Sunil" "Rajesh" "Manoj" "Pooja" "Sneha")
poc_d=${pocs[$RANDOM % ${#pocs[@]}]}

# Generate Random Phone Number (Indian Format)
phone="9$((RANDOM % 9000000000 + 1000000000))"

# Random Gender Selection
genders=("Male" "Female" "Other")
gender_d=${genders[$RANDOM % ${#genders[@]}]}

# API URL (Submission Endpoint)
url="https://registration-verification-official.onrender.com/submit"

# Send POST Request
response=$(curl -s -X POST "$url" \
    -H "Content-Type: application/json" \
    -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" \
    -d '{
        "name_d": "'"$name_d"'",
        "college_name_d": "'"$college_name_d"'",
        "graduation_year_d": "'"$graduation_year_d"'",
        "age_d": "'"$age_d"'",
        "point_of_contact_(poc)_d": "'"$poc_d"'",
        "phone": "'"$phone"'",
        "gender_d": "'"$gender_d"'",
        "otp_needed": "False",
        "form_id": "2LgGsJ"
    }')

# Print Random Details Used
echo -e "\n🔹 Generated Random Details:"
echo "Name: $name_d"
echo "College: $college_name_d"
echo "Graduation Year: $graduation_year_d"
echo "Age: $age_d"
echo "POC: $poc_d"
echo "Phone: $phone"
echo "Gender: $gender_d"

# Print Server Response
echo -e "\n🔹 Server Response:"
echo "$response"
