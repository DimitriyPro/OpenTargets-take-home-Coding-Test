import LibraryProcessing as lp
import sys
import os.path


def get_file_name():
    filename = '17.12_evidence_data.json'
    if os.path.exists(filename):
        return filename
    else:
        print("Sorry... File {} not found".format(filename))
        sys.exit(1)

def _get_json_object_from_line_(l):
    import json
    data = json.loads(l)

    return data


def _get_data_from_json_object_(data):
    targetId_disease_Id = data['target']['id'] + '--' + data['disease']['id']
    score = data['scores']['association_score']

    return targetId_disease_Id, score


def _raw_values_to_list_(dictionary):
    for key in dictionary:
        if type(dictionary[key]) == list:
            continue
        else:
            value = dictionary[key]
            dictionary[key] = [value]

    return dictionary


def _push_to_data_structure_(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = value
    elif type(dictionary[key]) == list:
        dictionary[key].append(value)
    else:
        dictionary[key] = [dictionary[key], value]
    result = _raw_values_to_list_(dictionary)

    return result


def save_results_to_csv(dictionary):
    import csv
    outputf = 'output.csv'
    with open(outputf, 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(dictionary)


def _calc_stat_(List):
    from statistics import median
    SortedTrimList = sorted(List, reverse=True)[:3]
    Mn = median(List)
    SortedTrimList.append(Mn)

    return SortedTrimList


def process_data(dict):
    output = {}
    for key in dict:
        output[key] = _calc_stat_(dict[key])
    result = sorted(output.items(), key=lambda e: e[0][1])

    return result


def process_line(dictionary, line):
    data = _get_json_object_from_line_(line)
    id, score = _get_data_from_json_object_(data)
    _push_to_data_structure_(dictionary, id, score)

    return dictionary


def print_block(text):
    lines = text.splitlines()
    width = max(len(s) for s in lines)
    res = ['┌' + '─' * width + '┐']
    for s in lines:
        res.append('│' + (s + ' ' * width)[:width] + '│')
    res.append('└' + '─' * width + '┘')
    print('\n'.join(res))


def library_check():
    import sys
    import subprocess
    import pkg_resources

    print("Trying to find \"ijson\" library...")

    required = {'ijson'}
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = required - installed

    if missing:
        print('Sorry... You don\'t have \"ijson\" library. Do you want to install it?')
        while True:
            user_input = input("You choice (y/n):")
            if user_input == 'y' or user_input == 'yes':
                print('Please wait...')
                try:
                    python = sys.executable
                    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
                    print("Successfully installed! Start processing")
                    lp.library_processing()
                    break
                except:
                    print("Can't install \"ijson\" library automatically. Please install it manually and try again")
                    sys.exit(0)
            elif user_input == 'n' or user_input == 'no':
                print("If you don't want to install \"ijson\" library, please run program again and choose a default "
                      "mode. Thank you!")
                sys.exit(0)
            else:
                print("Please enter yes or no")
                continue
    else:
        print("Library \"ijson\" found. Continue processing")
