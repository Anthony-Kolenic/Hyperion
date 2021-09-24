from command.base_cmd import BaseCmd

class CommandDelegate():
    id = 0
    @staticmethod
    def execute(command: BaseCmd) -> BaseCmd:
        print(f"{CommandDelegate.id} Executing - {command.__class__.__name__}")
        CommandDelegate.id += 1
        command.execute()
        CommandDelegate.id -= 1
        print(f"{CommandDelegate.id} Completed - {command.__class__.__name__}")
        return command