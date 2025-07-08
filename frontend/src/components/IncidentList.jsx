import React, { useState, useEffect } from 'react';

function WebSocketUpdates() {
    const [updates, setUpdates] = useState([]);

    useEffect(() => {
        const ws = new WebSocket("ws://localhost:8000/ws/incidents");

        ws.onmessage = (event) => {
            const data = JSON.parse(event.data);
            setUpdates(prev => [data, ...prev]);
        };

        return () => ws.close();
    }, []);

    return (
        <div>
            <h2>Real-Time Updates</h2>
            {updates.length === 0 ? (
                <p>No updates yet.</p>
            ) : (
                <ul className="incident-list">
                    {updates.map((update, idx) => (
                        <li key={idx}><b>{update.title}</b>: {update.description}</li>
                    ))}
                </ul>
            )}
        </div>
    );
}

export default WebSocketUpdates;
