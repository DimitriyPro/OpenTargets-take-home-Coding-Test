# import functions for processing data without any additional libraries
import FunctionsForProcessing as FuncForProc
# import datetime library for measure program execution speed
from datetime import datetime


def default_processing():

    # Init variables
    result = {}
    f = FuncForProc.get_file_name()
    start_time = datetime.now()

    # Process file with JSON data
    with open(f) as file:
        for line in file:
            FuncForProc.process_line(result, line)

    # Process extracted data
    output = FuncForProc.process_data(result)

    # Save results to CSV-file
    FuncForProc.save_results_to_csv(output)

    # Final message
    print("Ready!\nSee output.csv\nProgram finished in: {} sec".format(datetime.now() - start_time))
    
