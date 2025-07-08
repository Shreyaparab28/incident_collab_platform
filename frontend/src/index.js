import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import {
    ClerkProvider,
    SignedIn,
    SignedOut,
    RedirectToSignIn
} from "@clerk/clerk-react";

const clerkPubKey = "pk_test_Y2xlYXItc3BvbmdlLTUyLmNsZXJrLmFjY291bnRzLmRldiQ";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
    <React.StrictMode>
        <ClerkProvider publishableKey={clerkPubKey}>
            <SignedIn>
                <App />
            </SignedIn>
            <SignedOut>
                <RedirectToSignIn />
            </SignedOut>
        </ClerkProvider>
    </React.StrictMode>
);
