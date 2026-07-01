import asyncio
from prompt_toolkit import PromptSession
from prompt_toolkit.patch_stdout import patch_stdout
from prompt_manager import PromptManager

prompt_manager = PromptManager()

session = PromptSession()

with patch_stdout():
    while True:
        try:
            cmd = session.prompt("> ")
            print(cmd)
            prompt_manager.manage_prompt(cmd)
        except (EOFError, KeyboardInterrupt):
            break