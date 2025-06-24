from flask import Flask, request, jsonify
import random
import datetime

app = Flask(__name__)

# Карты соответствий между sensorID и location
sensor_to_location = {
    "1": "Living Room",
    "2": "Bedroom",
    "3": "Kitchen"
}

location_to_sensor = {v: k for k, v in sensor_to_location.items()}


@app.route('/temperature', methods=['GET'])
def get_temperature():
    location = request.args.get('location')
    sensor_id = request.args.get('sensorId')

    if not location:
        location = sensor_to_location.get(sensor_id, "Unknown")
    if not sensor_id:
        sensor_id = location_to_sensor.get(location, "0")

    temperature = round(random.uniform(18.0, 30.0), 1)

    return jsonify({
        "value": temperature,
        "unit": "°C",
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "location": location,
        "status": "ok",
        "sensor_id": sensor_id,
        "sensor_type": "temperature",
        "description": f"Sensor at {location}"
    })


@app.route('/temperature/<sensor_id>', methods=['GET'])
def get_temperature_by_id(sensor_id):
    location = sensor_to_location.get(sensor_id, "Unknown")
    temperature = round(random.uniform(18.0, 30.0), 1)

    return jsonify({
        "value": temperature,
        "unit": "°C",
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "location": location,
        "status": "ok",
        "sensor_id": sensor_id,
        "sensor_type": "temperature",
        "description": f"Sensor at {location}"
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
