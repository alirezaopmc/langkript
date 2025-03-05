from langchain_core.prompts import PromptTemplate

SKRIPT_GENERATION_TEMPLATE = """You are a Minecraft SkriptLang expert.
Your task is to convert the following prompt into a valid Skript code.
The code should be short and well-commented.

Important Guidelines:
1. Only output the Skript code, no explanations
2. Use spaces as indentation
3. Use the example templates for the related tasks.

Task Examples:
1. Command creations
User Prompt="Create a command that gives a diamond sword to the player with /givesword"
Skript Code:
```skript
on command /givesword:
    give player a diamond sword
```
or
```skript
command /givesword:
    trigger:
        give player a diamond sword
```

User's Request:
{user_prompt}

Generate the Skript code that fulfills this request:"""

skript_generation_prompt = PromptTemplate(
    input_variables=["user_prompt"],
    template=SKRIPT_GENERATION_TEMPLATE
) 