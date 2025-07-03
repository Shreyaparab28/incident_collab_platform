import React from 'react';
import IncidentList from './components/IncidentList';
import IncidentForm from './components/IncidentForm';
import WebSocketUpdates from './components/WebSocketUpdates';

function App() {
  return (
    <div className="App">
      <h1>Incident Collaboration Platform</h1>
      <IncidentForm />
      <IncidentList />
      <WebSocketUpdates />
    </div>
  );
}

export default App;
