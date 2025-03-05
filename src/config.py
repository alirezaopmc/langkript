from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Groq API Configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = "llama-3.3-70b-versatile"

# Minecraft Server Configuration
MINECRAFT_SERVER_HOST = os.getenv("MINECRAFT_SERVER_HOST")
MINECRAFT_SERVER_RCON_PORT = int(os.getenv("MINECRAFT_SERVER_RCON_PORT", "25575"))
MINECRAFT_SERVER_RCON_PASSWORD = os.getenv("MINECRAFT_SERVER_RCON_PASSWORD")

# SSH Configuration
SSH_USER = os.getenv("SSH_USER")
SSH_KEY_PATH = os.getenv("SSH_KEY_PATH")
REMOTE_SCRIPTS_PATH = os.getenv("REMOTE_SCRIPTS_PATH")

# Local Configuration
LOCAL_SCRIPTS_PATH = os.getenv("LOCAL_SCRIPTS_PATH", "scripts") 