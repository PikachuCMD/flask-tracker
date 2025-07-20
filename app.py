from flask import Flask, request, make_response
import requests
from datetime import datetime
import os

app = Flask(__name__)

def get_location(ip):
    try:
        res = requests.get(f"http://ip-api.com/json/{ip}")
        data = res.json()
        return {
            "ip": ip,
            "country": data.get("country"),
            "region": data.get("regionName"),
            "city": data.get("city"),
            "timezone": data.get("timezone"),
            "isp": data.get("isp"),
            "lat": data.get("lat"),
            "lon": data.get("lon"),
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    except:
        return {"ip": ip, "error": "Location not found"}

@app.route('/update.css')
def stealth_track():
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    if ',' in user_ip:
        user_ip = user_ip.split(',')[0]

    location = get_location(user_ip)

    log_file = os.environ.get("LOG_FILE", "click_log.txt")
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(str(location) + "\n")

    response = make_response('', 204)
    response.headers["Content-Type"] = "text/css"
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
