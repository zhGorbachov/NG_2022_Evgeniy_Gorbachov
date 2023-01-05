import platform
import psutil
from dataBase import *


def findVirtualMemory():
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


def process(nameOfBase, list):
    print("Taking info of your PC")
    for element in list:
        match element:
            case 'cpu':
                subtitleName = "Name of CPU"
                writeInformationIntoBase(nameOfBase, subtitleName, findProcessor())
                continue
            case 'pc':
                subtitleName = "Physical cores"
                writeInformationIntoBase(nameOfBase, subtitleName, findPhysicalCoresOfCPU())
                continue
            case 'lc':
                subtitleName = "Logical cores"
                writeInformationIntoBase(nameOfBase, subtitleName, findLogicalCoresOfCPU())
                continue
            case 'm':
                subtitleName = "Name of machine"
                writeInformationIntoBase(nameOfBase, subtitleName, findMachine())
                continue
            case 'n':
                subtitleName = "Node name"
                writeInformationIntoBase(nameOfBase, subtitleName, findNode())
                continue
            case 's':
                subtitleName = "Name of system"
                writeInformationIntoBase(nameOfBase, subtitleName, findSystem())
                continue
            case 'pv':
                subtitleName = "Python version"
                writeInformationIntoBase(nameOfBase, subtitleName, findVersionOfPython())
                continue
            case 'vm':
                subtitleName = "Virtual memory"
                writeInformationIntoBase(nameOfBase, subtitleName, findVirtualMemory())
                continue
            case _:
                break
    print("Info has already taken")
