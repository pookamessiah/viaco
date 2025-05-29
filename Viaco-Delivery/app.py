from flask import Flask, render_template, request

app = Flask(__name__)

# Sample Data: Tracking IDs and Parcel Details
parcels = {
    "RP4hwTTMzz34": {
        "recipient_name": "John Doe",
        "phone": "+123456789",
        "email": "john@example.com",
        "takeoff_location": "123 Elm Street, CA",
        "delivery_address": "456 Oak Street, NY",
        "expected_date": "2025-02-10",
        "sender_name": "Michael Scott",
        "sender_contact": "+1987654321"
    },
    "HJK7sLMNop89": {
        "recipient_name": "Alice Smith",
        "phone": "+987654321",
        "email": "alice@example.com",
        "takeoff_location": "567 Maple Ave, FL",
        "delivery_address": "789 Pine Street, TX",
        "expected_date": "2025-02-12",
        "sender_name": "Jane Doe",
        "sender_contact": "+1547896321"
    },
      "DP4hwTTMcv76": {
        "recipient_name": "John Doe",
        "phone": "+123456789",
        "email": "john@example.com",
        "takeoff_location": "123 Elm Street, CA",
        "delivery_address": "456 Oak Street, NY",
        "expected_date": "2025-02-10",
        "sender_name": "Michael Scott",
        "sender_contact": "+1987654321"
    },
      "YW8hwEEMzz21": {
        "recipient_name": "John Doe",
        "phone": "+123456789",
        "email": "john@example.com",
        "takeoff_location": "123 Elm Street, CA",
        "delivery_address": "456 Oak Street, NY",
        "expected_date": "2025-02-10",
        "sender_name": "Michael Scott",
        "sender_contact": "+1987654321"
    },
      "MJ4hwLLMzz56": {
        "recipient_name": "John Doe",
        "phone": "+123456789",
        "email": "john@example.com",
        "takeoff_location": "123 Elm Street, CA",
        "delivery_address": "456 Oak Street, NY",
        "expected_date": "2025-02-10",
        "sender_name": "Michael Scott",
        "sender_contact": "+1987654321"
    },
      "HP4swCVMzz90": {
        "recipient_name": "John Doe",
        "phone": "+123456789",
        "email": "john@example.com",
        "takeoff_location": "123 Elm Street, CA",
        "delivery_address": "456 Oak Street, NY",
        "expected_date": "2025-02-10",
        "sender_name": "Michael Scott",
        "sender_contact": "+1987654321"
    },
      "GD4hwPPKii57": {
        "recipient_name": "John Doe",
        "phone": "+123456789",
        "email": "john@example.com",
        "takeoff_location": "123 Elm Street, CA",
        "delivery_address": "456 Oak Street, NY",
        "expected_date": "2025-02-10",
        "sender_name": "Michael Scott",
        "sender_contact": "+1987654321"
    },
      "AK4iqGGMee00": {
        "recipient_name": "John Doe",
        "phone": "+123456789",
        "email": "john@example.com",
        "takeoff_location": "123 Elm Street, CA",
        "delivery_address": "456 Oak Street, NY",
        "expected_date": "2025-02-10",
        "sender_name": "Michael Scott",
        "sender_contact": "+1987654321"
    },
      "BB4hwTTMhh67": {
        "recipient_name": "John Doe",
        "phone": "+123456789",
        "email": "john@example.com",
        "takeoff_location": "123 Elm Street, CA",
        "delivery_address": "456 Oak Street, NY",
        "expected_date": "2025-02-10",
        "sender_name": "Michael Scott",
        "sender_contact": "+1987654321"
    },
      "AA4xxTTMjz52": {
        "recipient_name": "John Doe",
        "phone": "+123456789",
        "email": "john@example.com",
        "takeoff_location": "123 Elm Street, CA",
        "delivery_address": "456 Oak Street, NY",
        "expected_date": "2025-02-10",
        "sender_name": "Michael Scott",
        "sender_contact": "+1987654321"
    },
}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/track", methods=["GET", "POST"])
def track():
    result = None
    if request.method == "POST":
        tracking_id = request.form.get("tracking_id")
        result = parcels.get(tracking_id, None)
    return render_template("track.html", result=result)

if __name__ == "__main__":
    from os import environ
    port = int(environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
