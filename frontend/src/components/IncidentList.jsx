import { useEffect, useState } from "react";
import axios from "axios";

export default function IncidentList() {
  const [incidents, setIncidents] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:8000/incidents/").then((res) => {
      setIncidents(res.data);
    });
  }, []);

  return (
    <div>
      <h2>Incident List</h2>
      {incidents.map((incident) => (
        <div key={incident.id}>
          <strong>{incident.title}</strong>: {incident.description}
        </div>
      ))}
    </div>
  );
}
