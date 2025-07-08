import React, { useEffect, useState } from "react";
import { useAPI } from "./api";
import "./IncidentTable.css";

const IncidentTable = () => {
    const { getIncidents, createIncident, updateIncident, deleteIncident } = useAPI();
    const [incidents, setIncidents] = useState([]);
    const [title, setTitle] = useState("");
    const [description, setDescription] = useState("");

    const loadIncidents = async () => {
        const data = await getIncidents();
        setIncidents(data);
    };

    useEffect(() => {
        loadIncidents();
        const ws = new WebSocket("ws://localhost:8000/ws/incidents");
        ws.onmessage = (event) => {
            const message = JSON.parse(event.data);
            console.log("WebSocket update received:", message);
            loadIncidents();
        };
        return () => ws.close();
    }, []);
    

    const handleAddIncident = async () => {
        if (!title.trim() || !description.trim()) return;
        await createIncident({ title, description, status: "open" });
        setTitle("");
        setDescription("");
    };

    const handleStatusChange = async (id, newStatus) => {
        const incident = incidents.find(i => i.id === id);
        if (!incident) return;
        await updateIncident(id, { ...incident, status: newStatus });
    };

    const handleDelete = async (id) => {
        await deleteIncident(id);
    };

    return (
        <div className="table-container">
            
            <div className="add-container">
                <input
                    type="text"
                    placeholder="Title"
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                />
                <input
                    type="text"
                    placeholder="Description"
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
                />
                <button onClick={handleAddIncident}>Add Incident</button>
            </div>
            <table className="incident-table">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Title</th>
                        <th>Description</th>
                        <th>Status</th>
                        <th>Created At</th>
                        <th>Created By</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {incidents.map((incident) => (
                        <tr key={incident.id}>
                            <td>{incident.id}</td>
                            <td>{incident.title}</td>
                            <td>{incident.description}</td>
                            <td>
                                <select
                                    value={incident.status}
                                    onChange={(e) => handleStatusChange(incident.id, e.target.value)}
                                >
                                    <option value="open">Open</option>
                                    <option value="in-progress">In-progress</option>
                                    <option value="resolved">Resolved</option>
                                </select>
                            </td>
                            <td>{new Date(incident.created_at).toLocaleString()}</td>
                            <td>{incident.created_by || "Unknown"}</td>
                            <td>
                                <button className="delete-button" onClick={() => handleDelete(incident.id)}>
                                    Delete
                                </button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default IncidentTable;
