import { useNavigate } from "react-router-dom"; // Make sure the path is correct

const Home = () => {
  const navigate = useNavigate();

  return (
    <div className="home-container">
      <h1 className="home-title">🎟️ Welcome to EventBookr</h1>
      <p className="home-subtitle">
        Book tickets for the latest and hottest events in town!
      </p>
      <button className="home-button" onClick={() => navigate("/events")}>
        View Events
      </button>
    </div>
  );
};

export default Home;
