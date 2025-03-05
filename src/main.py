import os
import subprocess
from typing import Optional
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage
import mcrcon
from src import config
from src.prompt_templates import skript_generation_prompt
import re

def ensure_directory_exists(path: str) -> None:
    """Ensure that a directory exists, create if it doesn't."""
    if not os.path.exists(path):
        os.makedirs(path)

def generate_skript(prompt: str) -> str:
    """Generate Skript code from the user's prompt using Groq LLM."""
    llm = ChatGroq(
        api_key=config.GROQ_API_KEY,
        model_name=config.MODEL_NAME
    )
    
    formatted_prompt = skript_generation_prompt.format(user_prompt=prompt)
    messages = [HumanMessage(content=formatted_prompt)]
    
    response = llm.invoke(messages)
    content = response.content
    content = content.replace('```skript', '')
    content = content.replace('```', '')
    return content

def save_skript_to_file(code: str, filename: str) -> str:
    """Save the generated Skript code to a file."""
    ensure_directory_exists(config.LOCAL_SCRIPTS_PATH)
    
    file_path = os.path.join(config.LOCAL_SCRIPTS_PATH, filename)
    with open(file_path, 'w') as f:
        f.write(code)
    
    return file_path

def copy_to_server(local_path: str, filename: str) -> bool:
    """Copy the Skript file to the Minecraft server using scp."""
    remote_path = f"{config.SSH_USER}@{config.MINECRAFT_SERVER_HOST}:{config.REMOTE_SCRIPTS_PATH}/{filename}"
    
    try:
        subprocess.run([
            'scp',
            '-i', config.SSH_KEY_PATH,
            local_path,
            remote_path
        ], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error copying file to server: {e}")
        return False

def reload_skript(filename: str) -> bool:
    """Reload the Skript using RCON."""
    try:
        with mcrcon.MCRcon(
            config.MINECRAFT_SERVER_HOST,
            config.MINECRAFT_SERVER_RCON_PASSWORD,
            port=config.MINECRAFT_SERVER_RCON_PORT
        ) as mcr:
            response = mcr.command(f"skript reload {filename}")
            return "successfully" in response.lower()
    except Exception as e:
        print(f"Error reloading Skript: {e}")
        return False

def process_prompt(prompt: str, filename: Optional[str] = None) -> bool:
    """Process a user prompt and create a Minecraft behavior using Skript.
    
    Args:
        prompt (str): The user's prompt describing desired Minecraft behavior
        filename (Optional[str]): Custom filename for the Skript file (default: auto-generated)
    
    Returns:
        bool: True if successful, False otherwise
    """
    if filename is None:
        # Generate a filename based on the first few words of the prompt
        words = prompt.lower().split()[:3]
        filename = f"{'_'.join(words)}.sk"
    
    # Generate Skript code
    skript_code = generate_skript(prompt)
    
    # Save to local file
    local_path = save_skript_to_file(skript_code, filename)
    
    # Copy to server
    if not copy_to_server(local_path, filename):
        return False
    
    # Reload the Skript
    return reload_skript(filename)

# Example usage:
if __name__ == "__main__":
    test_prompt = input("Enter a prompt: ")
    success = process_prompt(test_prompt)
    print(f"Script processing {'successful' if success else 'failed'}") 