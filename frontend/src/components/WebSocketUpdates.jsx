import React, { useEffect, useState } from "react";

function WebSocketUpdates() {
    const [updates, setUpdates] = useState([]);

    useEffect(() => {
        const ws = new WebSocket("ws://localhost:8000/ws/incidents");

        ws.onmessage = (event) => {
            const data = JSON.parse(event.data);
            setUpdates(prev => [data, ...prev]);
        };

        ws.onclose = () => console.log("WebSocket connection closed");
        ws.onerror = (error) => console.error("WebSocket error:", error);

        return () => ws.close();
    }, []);

    return (
        <div>
            <h2 className="text-2xl font-bold text-center mt-6">Real-Time Updates</h2>
            {updates.length === 0 ? (
                <p className="text-center">No updates yet.</p>
            ) : (
                <ul className="mt-2 space-y-2">
                    {updates.map((update, idx) => (
                        <li key={idx} className="bg-blue-100 p-2 rounded shadow">
                            <b>{update.title}</b>: {update.description}
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
}

export default WebSocketUpdates;