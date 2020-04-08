import json
import sys
import subprocess
import statistics
import urllib.request

# init variables
target_score = []
disease_score = []
all_targets = []
all_diseases = []


def greetings():
    text = 'OpenTargets take-home Coding Test (Part A) by Dmitrii Prosovetskii'
    print(text)


def _target_analysis_(target_name, target_list):
    target_stddev, target_mean, target_max, target_min = stand_dev(target_list)
    result = "Standart deviation for target {0} = {1}\nMean for target {0} = {2}\nMax for target {0} = {3}\nMin for " \
             "target {0} = {4}".format(target_name, target_stddev, target_mean, target_max, target_min)
    print(result)


def _disease_analysis_(disease_name, disease_list):
    disease_stddev, disease_mean, disease_max, disease_min = stand_dev(disease_list)
    result = "Standart deviation for disease {0} = {1}\nMean for disease {0} = {2}\nMax for disease {0} = {3}\nMin for " \
             "disease {0} = {4}".format(disease_name, disease_stddev, disease_mean, disease_max, disease_min)
    print(result)


def _get_data_():
    try:
        url = 'https://platform-api.opentargets.io/v3/platform/public/association/filter'
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())

        return data
    except:
        result = 'Sorry... Server is not available at this moment. Please check you network settings or try ' \
                 'again later '
        print(result)
        sys.exit(1)


data = _get_data_()


def _get_all_targets_and_diseases_():
    for value in data['data']:
        all_targets.append(value['target']['id'])
        all_diseases.append(value['disease']['id'])


_get_all_targets_and_diseases_()


def stand_dev(val):
    stddev_val = statistics.stdev(val)
    mean_val = statistics.mean(val)
    max_val = max(val)
    min_val = min(val)
    return stddev_val, mean_val, max_val, min_val


def _append_to_list_(list, value):
    list.append(value)


def _process_values_():
    for value in data['data']:
        print(json.dumps(value['id'], indent=4, sort_keys=True))


def _i_suggest_disease_(disease):
    filtered_disease = []
    filtered_disease = list(filter(lambda x: x.startswith(disease[0]), all_diseases))
    try:
        if len(filtered_disease) > 1:
            # Deal with more that one disease.
            print('There are more than one disease starting with "{0}". You could try this one:'.format(disease[0]))
            for index, name in enumerate(filtered_disease):
                print("{0}: {1}".format(index, name))
        else:
            # Only one disease found, so print that team.
            print(filtered_disease[0])
    except IndexError:
        print()


def _i_suggest_target_(target):
    filtered_target = []
    filtered_target = list(filter(lambda x: x.startswith(target[0]), all_targets))
    try:
        if len(filtered_target) > 1:
            # Deal with more that one disease.
            print('There are more than one target starting with "{0}". You could try this one:'.format(target[0]))
            for index, name in enumerate(filtered_target):
                print("{0}: {1}".format(index, name))
        else:
            # Only one target found, so print that target.
            print(filtered_target[0])
    except IndexError:
        print()


def _find_target_(target):
    target_list = []
    for value in data['data']:
        if value['target']['id'] == target:
            _append_to_list_(target_list, value['association_score']['overall'])
    if not target_list:
        print("Sorry... Nothing found. Please try again")
        _i_suggest_target_(target)
        sys.exit(0)
    return target_list


def _find_disease_(disease):
    disease_list = []
    for value in data['data']:
        if value['disease']['id'] == disease:
            _append_to_list_(disease_list, value['association_score']['overall'])
    if not disease_list:
        print("Sorry... Nothing found. Please try again")
        _i_suggest_disease_(disease)
        sys.exit(0)
    return disease_list


def _default_analysis_():
    print("Score overall:")
    general_list = []
    for value in data['data']:
        _append_to_list_(general_list, value['association_score']['overall'])
    return general_list


def _all_file_analyze_():
    general_list = _default_analysis_()
    stddev_value, mean_value, max_value, min_value = stand_dev(general_list)
    result = "Standard deviation = {0}\nMean = {1}\nMax = {2}\nMin = {3}".format(stddev_value, mean_value, max_value, min_value)
    print(result)


def check_parametrs():
    if len(sys.argv) > 3:
        print("Warning: Too many parameters, please try again...")
        sys.exit(1)
    else:
        if len(sys.argv) == 1:
            print("DEFAULT CONFIG")
            _all_file_analyze_()
        elif len(sys.argv) == 2:
            param_name = sys.argv[1]
            if param_name == "--test":
                print("Run tests!")
                subprocess.run(["python", "test_Solution_A.py"])
            else:
                print("Undefined parameter. Please use -t for run a target analysis or -d for run disease analysis")
        elif len(sys.argv) == 3:
            param_name = sys.argv[1]
            param_value = sys.argv[2]
            if param_name == "-t":
                print("Target analysis for {}".format(param_value))
                target_list = _find_target_(param_value)
                _target_analysis_(param_value, target_list)
            elif param_name == "-d":
                print("Disease analysis for {}".format(param_value))
                disease_list = _find_disease_(param_value)
                _disease_analysis_(param_value, disease_list)
            else:
                print("Undefined parameter. Please use -t for run a target analysis or -d for run disease analysis")
                sys.exit(1)
