import React, { useState } from 'react';
import axios from 'axios';

const API_URL = "http://127.0.0.1:8000";

function IncidentForm() {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post(`${API_URL}/incidents/incidents/`, { title, description });
      setTitle("");
      setDescription("");
      alert("Incident created successfully!");
    } catch (error) {
      console.error("Error creating incident:", error);
    }
  };

  return (
    <div>
      <h2>Create Incident</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
        />
        <br />
        <textarea
          placeholder="Description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          required
        />
        <br />
        <button type="submit">Create Incident</button>
      </form>
    </div>
  );
}

export default IncidentForm;
