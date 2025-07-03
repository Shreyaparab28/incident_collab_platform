import { useState } from "react";
import axios from "axios";

export default function IncidentForm() {
  const [title, setTitle] = useState("");
  const [description, setDesc] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post("http://localhost:8000/incidents/", { title, description });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input value={title} onChange={(e) => setTitle(e.target.value)} placeholder="Title" />
      <input value={description} onChange={(e) => setDesc(e.target.value)} placeholder="Description" />
      <button type="submit">Submit</button>
    </form>
  );
}
