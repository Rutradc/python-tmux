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

TO GET OUT OF TMUX (DETACH)
Ctrl + B then D
''')
            case 'gather':
                if len(parts) > 4:
                    print(f'{len(parts)} is {len(parts) - 3} too many arguments')
                    return
                if len(parts) < 3:
                    print(f'Not enough arguments !')
                    return
                if parts[1] not in ['Rutradc', 'PoorBulma', 'Jojo', 'Cimeo', 'SosoCheon']:
                    print(f'{parts[1]} is not a valid character_name !')
                    return
                if parts[2] not in ['COPPER', 'IRON', 'ASH_WOOD']:
                    print(f'{parts[2]} is not a valid Resource !')
                    return
                if len(parts) == 4 and parts[3] not in ['True', 'False']:
                    print(f'{parts[3]} is not a valid boolean for crafting !')
                    return
                character_name: str = parts[1]
                resource = parts[2]
                if len(parts) == 4:
                    crafting = parts[3] == 'True'
                    print(f'self.actions_service.gather_ressource({character_name}, {resource}, {crafting})')
                else:
                    print(f'self.actions_service.gather_ressource({character_name}, {resource})')
            case _:
                print(f'{parts[0]} is not a known command\n')