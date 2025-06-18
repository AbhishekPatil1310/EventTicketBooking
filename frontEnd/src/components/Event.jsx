import { useEffect, useState } from "react";
import axios from "axios";
import '../style/Event.css'

function EventList() {
  const [events, setEvents] = useState([]);
  const [bookingInputs, setBookingInputs] = useState({}); // Track input per event

  useEffect(() => {
    axios.get(`${import.meta.env.VITE_API_BASE_URL}/events`)
      .then((res) => setEvents(res.data))
      .catch(console.error);
  }, []);

  const handleInputChange = (eventId, field, value) => {
    setBookingInputs(prev => ({
      ...prev,
      [eventId]: {
        ...prev[eventId],
        [field]: value
      }
    }));
  };

  const handleBook = (eventId) => {
    const booking = bookingInputs[eventId];
    if (!booking?.user_name || !booking?.tickets) {
      alert("Please enter your name and number of tickets.");
      return;
    }

    axios.post(`${import.meta.env.VITE_API_BASE_URL}/book`, {
      user_name: booking.user_name,
      event_id: eventId,
      tickets: Number(booking.tickets)
    })
      .then(res => alert(res.data.message))
      .catch(err => {
        console.error(err);
        alert("Booking failed.");
      });
  };

 return (
  <div className="event-container">
    <h1 className="event-title">Events</h1>
    {events.map(e => (
      <div key={e.id} className="event-card">
        <h3>{e.name}</h3>
        <p>{e.description}</p>
        <p>Date: {e.date}</p>
        <p>Available Tickets: {e.available_tickets}</p>

        <input
          type="text"
          placeholder="Your Name"
          value={bookingInputs[e.id]?.user_name || ""}
          onChange={ev => handleInputChange(e.id, "user_name", ev.target.value)}
        />
        <input
          type="number"
          min="1"
          value={bookingInputs[e.id]?.tickets || ""}
          onChange={ev => handleInputChange(e.id, "tickets", ev.target.value)}
        />
        <button onClick={() => handleBook(e.id)}>Book</button>
      </div>
    ))}
  </div>
);

}

export default EventList;
