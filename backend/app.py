import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

API_KEY = os.getenv("WHOIS_API_KEY")  # Ensure this exists in your .env

@app.route("/api/whois", methods=["POST"])
def whois_lookup():
    data = request.get_json()
    domain = data.get("domain")
    info_type = data.get("type")

    if not domain or not info_type:
        return jsonify({"error": "Missing domain or type"}), 400

    url = "https://www.whoisxmlapi.com/whoisserver/WhoisService"
    params = {
        "apiKey": API_KEY,
        "domainName": domain,
        "outputFormat": "JSON"
    }

    try:
        res = requests.get(url, params=params)
        res.raise_for_status()
        whois_data = res.json().get("WhoisRecord", {})

        if info_type == "domain":
            result = {
                "Domain Name": whois_data.get("domainName", ""),
                "Registrar": whois_data.get("registrarName", ""),
                "Registration Date": whois_data.get("createdDate", ""),
                "Expiration Date": whois_data.get("expiresDate", ""),
                "Estimated Age": whois_data.get("estimatedDomainAge", ""),
                "Hostnames": whois_data.get("nameServers", {}).get("hostNames", []),
            }
        elif info_type == "contact":
            result = {
                "Registrant Name": whois_data.get("registrant", {}).get("name", ""),
                "Technical Contact": whois_data.get("technicalContact", {}).get("name", ""),
                "Admin Contact": whois_data.get("administrativeContact", {}).get("name", ""),
                "Contact Email": whois_data.get("contactEmail", ""),
            }
        else:
            return jsonify({"error": "Invalid type selected"}), 400

        return jsonify(result)

    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}")
        return jsonify({"error": "Failed to fetch WHOIS data"}), 500


