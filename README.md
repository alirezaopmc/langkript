# Minecraft Skript Generator

This application converts natural language prompts into Minecraft Skript code using LangChain and Groq's LLM. It automatically generates, deploys, and loads Skript files on your Minecraft server.

## TODO

- [ ] Telegram Bot

Any suggestion? alirezaopmc@gmail.com

## Prerequisites

- Python 3.8+
- Minecraft server with Skript plugin installed
- SSH access to the Minecraft server
- RCON enabled on the Minecraft server
- Groq API key

## Setup

1. Clone the repository and navigate to it:
```bash
git clone http://github.com/alirezaopmc/langkript
cd langkript
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Copy the example environment file and fill in your details:
```bash
cp .env.example .env
```

5. Edit the `.env` file with your configuration:
- Add your Groq API key
- Configure your Minecraft server details
- Set up SSH access information
- Specify paths for scripts

## Usage

Run the application using the command:

```bash
python -m src.main
```

## Environment Variables

- `GROQ_API_KEY`: Your Groq API key
- `MINECRAFT_SERVER_HOST`: IP or hostname of your Minecraft server
- `MINECRAFT_SERVER_RCON_PORT`: RCON port (default: 25575)
- `MINECRAFT_SERVER_RCON_PASSWORD`: RCON password
- `SSH_USER`: SSH username for the server
- `SSH_KEY_PATH`: Path to your SSH private key
- `REMOTE_SCRIPTS_PATH`: Path to Skript scripts directory on the server
- `LOCAL_SCRIPTS_PATH`: Local path to store generated scripts

## How It Works

1. The application takes a natural language prompt describing desired Minecraft behavior
2. It uses Groq's LLM to generate appropriate Skript code
3. The code is saved to a local file
4. The file is copied to the Minecraft server using SCP
5. The script is loaded using RCON commands

## Error Handling

The application includes error handling for:
- File system operations
- SSH/SCP file transfers
- RCON communication
- LLM API calls

## Contributing

Feel free to submit issues and pull requests.

## License

GNU Public v3.0