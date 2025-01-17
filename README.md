goit-cs-hw-06

# WebSocket Message Server

This project is a WebSocket-based messaging server that allows users to send and receive real-time messages. The server stores messages in a MongoDB database and also keeps a copy in a local JSON file. The project includes a basic frontend to display the message history in a table format and handle user interactions.

## Features

- Real-time messaging using WebSockets
- Message persistence using MongoDB
- Backup of messages to a local JSON file (data.json)
- Simple HTML frontend to view the message history
- Error handling and custom error pages

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Installation

1.  Clone the repository:

        git clone https://github.com/yourusername/websocket-message-server.git
        cd websocket-message-server

2.  Start the services using Docker Compose:

        docker-compose up

    This command will create and run three containers:

    - An HTTP server, available on port 3000.
    - A WebSocket server, available on port 5000.
    - MongoDB, available on port 27017.

3.  Access the frontend:

- Open your web browser and navigate to http://localhost:3000.

### Usage

- To send a message, use the form provided at http://localhost:3000/message.
- To view the message history, go to http://localhost:3000/history.

### API Endpoints

- POST /message: Endpoint to send a new message. Expects a JSON payload with date, username, and message fields.
- GET /get_messages: Endpoint to fetch all messages stored in data.json.

### WebSocket

The WebSocket server runs on the same address and port. Clients can connect to receive real-time updates when new messages are sent.

### Frontend

The frontend is a simple HTML page that uses JavaScript to fetch and display messages from the server.

### Viewing Message History

- Open http://localhost:3000/history The table will be populated with messages from the server.

### Error Handling

To handle 404 errors, create an error.html file in the public directory. This file will be served when a user accesses a non-existent route.

In your server configuration, make sure to serve this file for 404 errors.

### Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes.

### Contact

For any inquiries, please contact https://www.linkedin.com/in/vekh/

### After using:

      docker-compose down
