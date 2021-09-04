from .command.base_cmd import BaseCmd

class CommandDelegate():

    @staticmethod
    def execute(command: BaseCmd) -> BaseCmd:
        print(f"Executing - {command.__class__.__name__}")
        command.execute()
        return command