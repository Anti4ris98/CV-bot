from info import Summary, Academic, Experience, Contact, Links


class Bot(CmdProvider):
    HELLO_MSG = "Hi, this is your assistant"
    HELLO_HELP_MSG = "write your command ('h|help' for details)"
    BYE_MSG = "Bye!"
    PROMPT_MSG = ">>> "
    INVALID_CMD_MSG = "Invalid command!"

    __cmds_help = (
        ("help", "h|help", "Show this message."),
    )

    def __init__(self, book: Book):
        self.__finish = False
        self.__is_error = False
        self.cmds = {
            "help": self.get_help_message,
            "h": self.get_help_message,
            "exit": self.exit,
            "close": self.exit,
            "q": self.exit,