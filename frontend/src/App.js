import React from "react";
import IncidentTable from "./IncidentTable";
import { SignedIn, SignedOut, SignInButton, UserButton } from "@clerk/clerk-react";
import "./App.css"; // ensure global styles
function App() {
    return (
        <><div style={{ padding: "20px" }}>
            <h1>🚀 Incident Collaboration Platform</h1>
        </div>
        <div className="container">
            <SignedOut>
                <h2>Please sign in to continue</h2>
                <SignInButton />
            </SignedOut>
            <SignedIn>
                <div style={{
                    position: "absolute",
                    top: "20px",
                    left: "20px",
                    borderRadius: "50%",
                    overflow: "hidden",
                    boxShadow: "0 2px 8px rgba(0,0,0,0.2)",
                    cursor: "pointer"
                }}>
                    <UserButton />
                </div>
                <IncidentTable />
            </SignedIn>

        </div></>
    );
}

export default App;
