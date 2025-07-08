import axios from "axios";
import { useAuth } from "@clerk/clerk-react";

const API_URL = "http://localhost:8000";



export const useAPI = () => {
  const { getToken } = useAuth();

  const getHeaders = async () => {
      const token = await getToken({ template: "for_user" });
      return { Authorization: `Bearer ${token}` };
  };

  const getIncidents = async () => {
      const headers = await getHeaders();
      try {
          const response = await axios.get(`${API_URL}/incidents/`, { headers });
          return response.data;
      } catch (error) {
          console.error("Error fetching incidents:", error);
          throw error;
      }
  };

  const createIncident = async (incident) => {
      const headers = await getHeaders();
      const response = await axios.post(`${API_URL}/incidents/`, incident, { headers });
      return response.data;
  };

  const updateIncident = async (id, incident) => {
      const headers = await getHeaders();
      const response = await axios.put(`${API_URL}/incidents/${id}`, incident, { headers });
      return response.data;
  };

  const deleteIncident = async (id) => {
      const headers = await getHeaders();
      const response = await axios.delete(`${API_URL}/incidents/${id}`, { headers });
      return response.data;
  };

  return { getIncidents, createIncident, updateIncident, deleteIncident };
};
