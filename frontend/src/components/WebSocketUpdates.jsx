import { useEffect } from "react";

export default function WebSocketUpdates() {
  useEffect(() => {
    const socket = new WebSocket("ws://localhost:8000/ws");

    socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      console.log("Real-time update:", data);
    };

    return () => socket.close();
  }, []);

  return <div>Listening for updates...</div>;
}
