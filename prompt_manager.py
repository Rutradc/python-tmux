import asyncio


class PromptManager:
    def manage_prompt(self, prompt: str):
        parts: list[str]= prompt.split()
        match parts[0].lower():
            case 'help':
                print(
'''
TO STOP ACTION FROM A CHARACTER
stop {character_name: str}

TO GATHER RESSOURCES
gather {character_name: str} {ressource: Resource} {crafting : bool (optionnal)}

TO ATTACK WHERE THE CHARACTER IS
attack {character_name: str}

TO GET HELP (THIS PANEL)
help
''')
            case 'gather':
                print(f'Gather command with {parts[0]}')
            case _:
                print(f'{parts[0]} is not a known command\n')