import sys
import FunctionsForProcessing as FuncForProc
from DefaultProcessing import default_processing
from LibraryProcessing import library_processing
from FindConnections import find_connections


while True:
    # Brief program description
    FuncForProc.print_block("OpenTargets take-home Coding Test (Part B) by Dmitrii Prosovetskii")
    FuncForProc.print_block("This program can be run in tree different modes. First mode - default. "
    "Default mode process file without any libraries. "
    "Second mode process file by using ijson library. Third mode - allows to find how many "
    "target-target pairs share a connection to at least two diseases. Please enter \"d\" for "
    "default mode, \"i\" to start process with \"ijson\" library, \"f\" to find a connections or \"e\" for exit. Thank you!")

    user_input = input("Your choice: ")

    # Process user input
    if user_input == 'd':
        print("Please wait...")
        default_processing()
        break
    elif user_input == 'i':
        FuncForProc.library_check()
        print("Please wait...")
        library_processing()
        break
    elif user_input == 'e':
        sys.exit(0)
    elif user_input == 'f':
        FuncForProc.library_check()
        print("Please wait...")
        find_connections()
        break
    else:
        print("Please enter i, d, f or e (see description)")
        continue
