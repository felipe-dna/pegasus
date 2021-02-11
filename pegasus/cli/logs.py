import six
from PyInquirer import Token, style_from_dict
from pyfiglet import figlet_format


try:
    import colorama
    colorama.init()
except ImportError:
    colorama = None

try:
    from termcolor import colored
except ImportError:
    colored = None


style = style_from_dict({
    Token.QuestionMark: '#fac731 bold',
    Token.Answer: '#4688f1 bold',
    Token.Instruction: '',  # default
    Token.Separator: '#cc5454',
    Token.Selected: '#0abf5b',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Question: '',
})


def log(
        message: str,
        color: str,
        font: str = "slant",
        figlet: bool = False
) -> None:
    if colored:
        if not figlet:
            six.print_(colored(message, color))
        else:
            six.print_(colored(figlet_format(
                message,
                font=font
            ), color))
    else:
        six.print_(message)
