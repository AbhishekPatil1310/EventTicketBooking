from flask import Blueprint, request, jsonify
from models import Connect_DB

booking_routes = Blueprint("booking", __name__)

@booking_routes.route("/api/events", methods=["GET"])
def get_events():
    conn = Connect_DB()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM events")
    events = cursor.fetchall()
    conn.close()
    return jsonify(events)


@booking_routes.route("/api/book", methods=["POST"])
def book_event():
    try:
        data = request.get_json()
        print("Incoming booking data:", data)

        # Safely extract values
        user_name = data.get('user_name')
        event_id = data.get('event_id')
        tickets = data.get('tickets')

        # Validate input
        if not user_name or not event_id or not tickets:
            return jsonify({'message': 'Missing booking fields'}), 400

        conn = Connect_DB()
        cursor = conn.cursor()

        # Check ticket availability
        cursor.execute("SELECT available_tickets FROM events WHERE id = %s", (event_id,))
        result = cursor.fetchone()

        if result and result[0] >= tickets:
            # Insert booking
            cursor.execute(
                "INSERT INTO bookings (user_name, event_id, ticket_booked) VALUES (%s, %s, %s)",
                (user_name, event_id, tickets)
            )
            # Update event ticket count
            cursor.execute(
                "UPDATE events SET available_tickets = available_tickets - %s WHERE id = %s",
                (tickets, event_id)
            )
            conn.commit()
            response = {'message': 'Booking successful'}
        else:
            response = {'message': 'Not enough tickets available'}

        conn.close()
        return jsonify(response)

    except KeyError as e:
        return jsonify({'error': f'Missing field: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500
