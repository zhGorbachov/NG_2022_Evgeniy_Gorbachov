from rich.console import Console
import platform
import inquirer
from inquirer.themes import GreenPassion
import psutil

console = Console()
style = "black on #e0cfb1"


def createfile():
    datafile = open("InfoAboutPC.txt", "w")
    datafile.close()
    return datafile


def appendfile(number, function, key):
    datafile = open("InfoAboutPC.txt", "a")
    datafile.write("======================[" + str(key) + "]======================" + "\n")
    datafile.write("[" + str(number) + "] " + str(function) + "\n")
    datafile.write("\n")
    datafile.close()


def find_virtualMemory():
    return psutil.virtual_memory()


def findProcessor():
    return platform.processor()


def findMachine():
    return platform.machine()


def findArchitecture():
    return platform.architecture()


def findPhysicalCoresOfCPU():
    return psutil.cpu_count()


def findLogicalCoresOfCPU():
    return psutil.cpu_count(logical=False)


def findNode():
    return platform.node()


def findSystem():
    return platform.system()


def findVersionOfPython():
    return platform.python_version()


def info(message):
    return console.rule(message, style='#e0cfb1')


def menu():
    action_menu = [inquirer.Checkbox("interests",
            message="What are you interested in?",
            choices=[
                ("CPU", "c"),
                ("Logical cores", 'lc'),
                ("Physical cores", 'pc'),
                ("Architecture", "a"),
                ("Machine", "m"),
                ("Node name", "n"),
                ("System", "s"),
                ("Python version", "pv"),
                ("Virtual memory", "vm")], ), ]

    answer_menu = inquirer.prompt(action_menu, theme=GreenPassion())
    result_menu = []
    for key in answer_menu:
        result_menu = answer_menu[key]
    return result_menu


def process():
    info("Program stated")
    info("[INFO] Choose variant on space, and confirm on enter.")
    createfile()
    result_menu = menu()
    number_of_count = 1
    while True:
        if 'c' in result_menu:
            appendfile(number_of_count, findProcessor(), "Name of CPU")
            result_menu.remove("c")
        elif 'pc' in result_menu:
            appendfile(number_of_count, findPhysicalCoresOfCPU(), "Physical cores")
            result_menu.remove("pc")
        elif 'lc' in result_menu:
            appendfile(number_of_count, findLogicalCoresOfCPU(), "Logical cores")
            result_menu.remove("lc")
        elif 'a' in result_menu:
            appendfile(number_of_count, findArchitecture(), "Architecture")
            result_menu.remove('a')
        elif 'm' in result_menu:
            appendfile(number_of_count, findMachine(), "Name of machine")
            result_menu.remove('m')
        elif 'n' in result_menu:
            appendfile(number_of_count, findNode(), "Node name")
            result_menu.remove('n')
        elif 's' in result_menu:
            appendfile(number_of_count, findSystem(), "Name of system")
            result_menu.remove('s')
        elif 'pv' in result_menu:
            appendfile(number_of_count, findVersionOfPython(), "Python version")
            result_menu.remove('pv')
        elif 'vm' in result_menu:
            appendfile(number_of_count, find_virtualMemory(), "Virtual memory")
            result_menu.remove('vm')
        else:
            break
        number_of_count += 1
    info("Program shuts down.")


def main():
    process()


main()
