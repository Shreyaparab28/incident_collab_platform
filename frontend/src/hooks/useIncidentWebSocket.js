import { useEffect } from "react";

const useIncidentWebSocket = (onMessage) => {
    useEffect(() => {
        const ws = new WebSocket("ws://localhost:8000/ws/incidents");

        ws.onopen = () => {
            console.log("Connected to WebSocket server.");
        };

        ws.onmessage = (event) => {
            const data = JSON.parse(event.data);
            console.log("WebSocket message received:", data);
            onMessage(data);
        };

        ws.onerror = (error) => {
            console.error("WebSocket error:", error);
        };

        ws.onclose = () => {
            console.log("WebSocket connection closed.");
        };

        return () => ws.close();
    }, [onMessage]);
};

export default useIncidentWebSocket;
