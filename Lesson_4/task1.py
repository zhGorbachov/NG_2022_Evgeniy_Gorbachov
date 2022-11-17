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
    return answer_menu


def process():
    info("Program stated")
    info("[INFO] Choose variant on space, and confirm on enter.")
    createfile()
    result_menu = menu()
    number_of_count = 0
    for element in result_menu["interests"]:
        number_of_count += 1
        match element:
            case 'c':
                appendfile(number_of_count, findProcessor(), "Name of CPU")
                continue
            case 'pc':
                appendfile(number_of_count, findProcessor(), "Physical cores")
                continue
            case 'lc':
                appendfile(number_of_count, findProcessor(), "Logical cores")
                continue
            case 'a':
                appendfile(number_of_count, findProcessor(), "Architecture")
                continue
            case 'm':
                appendfile(number_of_count, findProcessor(), "Name of machine")
                continue
            case 'n':
                appendfile(number_of_count, findProcessor(), "Node name")
                continue
            case 's':
                appendfile(number_of_count, findProcessor(), "Name of system")
                continue
            case 'pv':
                appendfile(number_of_count, findProcessor(), "Python version")
                continue
            case 'vm':
                appendfile(number_of_count, findProcessor(), "Virtual memory")
                continue
            case _:
                print("hello")
                break
    info("Program shuts down.")


def main():
    process()


main()
