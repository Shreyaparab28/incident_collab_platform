import IncidentList from "./components/IncidentList";
import IncidentForm from "./components/IncidentForm";
import WebSocketUpdates from "./components/WebSocketUpdates";

function App() {
  return (
    <div>
      <h1>Real-Time Incident Collaboration</h1>
      <IncidentForm />
      <IncidentList />
      <WebSocketUpdates />
    </div>
  );
}

export default App;
