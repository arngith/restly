---
title: Restly
emoji: 🤖
colorFrom: blue
colorTo: indigo
sdk: docker
pinned: false
---

# Restly
> **Deploy AI Agent as an Endpoint in seconds**

An intelligent Restly management platform that automatically generates ready-to-use API endpoints for every Restly Agent you create.

**Restly** is a modern AI Agent platform designed with an API-centric (RESTful) architecture. This project enables seamless, fast, and efficient integration of intelligent assistants into various applications powered by **Gemini**.

# Features

-   **RESTful Agent API**: Access AI capabilities through standardized and easy-to-integrate API endpoints.
-   **Gemini AI Integration**: Directly integrated with Google Gemini API for a highly responsive and intelligent brain.
-   **Smart Hibernation (Local Only)**: Leverages **Sablier** and **Traefik** technology to save resources by hibernating containers when inactive and automatically waking them upon request.
-   **Multi-Service Architecture**: Supports service separation between frontend, backend, and API for better scalability.

# Tech Stack

-   **AI Engine**: Google Gemini API
-   **Core**: Python (**Django** & Flask/FastAPI)
-   **Containerization**: Docker & Docker Compose
-   **Infrastructure**: Sablier & Traefik (Local Hibernation & Proxy)
-   **Platform**: Hugging Face Spaces

# Prerequisites

### 1. Get Google Gemini API Key
To use the AI capabilities, you need a Gemini API key:
1.  Go to [Google AI Studio](https://aistudio.google.com/).
2.  Login with your Google account.
3.  Click on **"Get API key"** and then **"Create API key in new project"**.
4.  Copy the generated key.

# Deployment

### Hugging Face Spaces

To deploy the **Restly** frontend to Hugging Face, follow these steps:

1.  **Create Space**: Create a new Space on Hugging Face and select **Docker** as the SDK.
2.  **Environment Variables**: Set the following variables in the Space settings:
    -   `HF_TOKEN`: Your Hugging Face API Token.
    -   `API_PUBLIC`: Your public backend API URL.
    -   `AGENT`: Default Agent name.
    -   `MODULE`: Default Module name (e.g., `chat`).
3.  **Push Code**: Push this repository to your Space. Hugging Face will automatically build the container using the provided `Dockerfile`.

# Usage

After deployment, you can access the **Restly** interface through your Hugging Face Space URL. 

This frontend connects to the **[Restly Backend](https://huggingface.co/spaces/arnhuggingface/restly-api)** for AI processing. For API documentation and technical details, please visit the **[backend Space](https://huggingface.co/spaces/arnhuggingface/restly-backend)**.

---

# Support

If you encounter any issues or have questions, please refer to the [issues page](https://github.com/arngith/restly/issues) for assistance.

---

# License

This project is licensed under the terms of the MIT license.
