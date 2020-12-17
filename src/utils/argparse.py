from argparse import ArgumentParser
from .ui import Cli, QT

def ui_chooser():
    parser = ArgumentParser(
        prog="src/play.py",
        description="awesome othello AI",
        epilog="enjoy playing :D"
    )
    parser.add_argument("ui", choices=["cli", "gui"])
    if parser.parse_args().ui == "cli":
        return Cli()
    else:
        return QT()
