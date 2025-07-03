import React, { useEffect, useState } from 'react';
import axios from 'axios';

const API_URL = "http://127.0.0.1:8000";

function IncidentList() {
  const [incidents, setIncidents] = useState([]);

  const fetchIncidents = async () => {
    try {
      const response = await axios.get(`${API_URL}/incidents/incidents/`);
      setIncidents(response.data);
    } catch (error) {
      console.error("Error fetching incidents:", error);
    }
  };

  useEffect(() => {
    fetchIncidents();
  }, []);

  return (
    <div>
      <h2>Incidents</h2>
      {incidents.length === 0 ? (
        <p>No incidents available.</p>
      ) : (
        <ul>
          {incidents.map((incident) => (
            <li key={incident.id}>
              <strong>{incident.title}</strong>: {incident.description}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default IncidentList;
