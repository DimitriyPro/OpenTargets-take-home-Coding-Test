import io
import ijson
from datetime import datetime
import FunctionsForProcessing as FuncForProc


def find_connections():
    # Init variables
    d = {}
    result = {}
    filename = FuncForProc.get_file_name()
    start_time = datetime.now()

    # Process file with JSON data
    with open(filename, encoding="UTF-8") as json_file:
        cursor = 0
        for line_number, line in enumerate(json_file):
            line_as_file = io.StringIO(line)
            # Use a new parser for each line
            json_parser = ijson.parse(line_as_file)
            for prefix, type, value in json_parser:
                if prefix == ('target.id'):
                    tID = value
                elif prefix == ('disease.id'):
                    dID = value
            if tID in d:
                d[tID].append(dID)
            else:
                d[tID] = [dID]
            cursor += len(line)

    # Filter data
    for key in d:
        if len(d[key]) >= 2:
            result[key] = d[key]

    # Save results to CSV-file
    FuncForProc.save_results_to_csv(result)

    # Final message
    print("Ready!\nSee output.csv\nProgram finished in: {} sec".format(datetime.now() - start_time))
