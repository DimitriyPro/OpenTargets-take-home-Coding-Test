import io
import ijson
from datetime import datetime
import FunctionsForProcessing as FuncForProc


def library_processing():

    # Init variables
    d = {}
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
                elif prefix == ('scores.association_score'):
                    aScore = value
            key = tID + '--' + dID
            if key in d:
                d[key].append(float(aScore))
            else:
                d[key] = [float(aScore)]
            cursor += len(line)

    # Process extracted data
    output = FuncForProc.process_data(d)

    # Save results to CSV-file
    FuncForProc.save_results_to_csv(output)

    # Final message
    print("Ready!\nSee output.csv\nProgram finished in: {} sec".format(datetime.now() - start_time))
