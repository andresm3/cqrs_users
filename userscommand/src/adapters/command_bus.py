
class CommandBus:
    def __init__(self):
        self.handlers = {}

    def register_handler(self, command_type, handler):
        """
        Registra un manejador para un tipo de comando específico.
        """
        self.handlers[command_type] = handler

    def dispatch(self, command):
        """
        Despacha el comando al manejador registrado.
        """
        command_type = type(command)
        handler = self.handlers.get(command_type)
        
        if handler:
            handler.handle(command)
        else:
            raise ValueError(f"No handler registered for command type {command_type}")
