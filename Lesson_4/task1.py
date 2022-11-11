from rich.console import Console
import platform
import inquirer
from inquirer.themes import GreenPassion


console = Console()
style = "black on #e0cfb1"


def createfile():
    datafile = open("InfoAboutPC.txt", "w")
    datafile.close()
    return datafile


def appendfile(message, function):
    datafile = open("InfoAboutPC.txt", "a")
    datafile.write(message + str(function) + "\n")
    datafile.close()


def findProcessor():
    return platform.processor()


def findMachine():
    return platform.machine()


def findArchitecture():
    return platform.architecture()


def findNode():
    return platform.node()


def findSystem():
    return platform.system()


def findVersionOfPython():
    return platform.python_version()


def info():
    console.print("Program started", style=style, justify="left")
    console.print("[INFO] Choose variant on space, and confirm on enter.", style='black on #e0cfb1', justify='left')


def menu():
    action_menu = [inquirer.Checkbox("interests",
            message="What are you interested in?",
            choices=[
                ("CPU", "c"),
                ("Architecture", "a"),
                ("Machine", "m"),
                ("Node name", "n"),
                ("System", "s"),
                ("Python version", "pv")], ), ]

    answer_menu = inquirer.prompt(action_menu, theme=GreenPassion())
    result_menu = []
    for key in answer_menu:
        result_menu = answer_menu[key]
    return result_menu


def process():
    info()
    createfile()
    result_menu = menu()
    while True:
        if 'c' in result_menu:
            appendfile("Name of CPU: ", findProcessor())
            result_menu.remove("c")
        elif 'a' in result_menu:
            appendfile("Architecture of PC: ", findArchitecture())
            result_menu.remove('a')
        elif 'm' in result_menu:
            appendfile("Name of machine: ", findMachine())
            result_menu.remove('m')
        elif 'n' in result_menu:
            appendfile("Node name: ", findNode())
            result_menu.remove('n')
        elif 's' in result_menu:
            appendfile("Name of system: ", findSystem())
            result_menu.remove('s')
        elif 'pv' in result_menu:
            appendfile("Version of python: ", findVersionOfPython())
            result_menu.remove('pv')
        else:
            break
    console.print("Program shuts down.", style="black on #e0cfb1", justify='left')


def main():
    process()


main()
