import React, { useEffect, useState } from 'react';

function WebSocketUpdates() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    const ws = new WebSocket("ws://127.0.0.1:8000/ws/incidents/");
    ws.onmessage = (event) => {
      setMessage(event.data);
    };
    ws.onerror = (error) => {
      console.error("WebSocket error:", error);
    };
    return () => {
      ws.close();
    };
  }, []);

  return (
    <div>
      <h2>Real-Time Updates</h2>
      {message ? <p>{message}</p> : <p>No updates yet.</p>}
    </div>
  );
}

export default WebSocketUpdates;
