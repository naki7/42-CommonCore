from typing import TextIO


def string_splitter(line: str) -> dict:
    result_arr: list = []
    dict_set: dict = {}

    result_arr = line.split(': ')
    dict_set = {result_arr[0]: int(result_arr[1])}
    return dict_set


def hub_handler(config_arr: list) -> dict:
    hub_dict: dict = {
        'start_hub': '',
        'end_hub': ''
    }
    hub_arr: list = [line for line in config_arr if
                     line.startswith("hub") is True
                     or line.startswith("start_hub") is True
                     or line.startswith("end_hub") is True]
    # edit this section, count doesnt check start_hub as a start
    if hub_arr.count('start_hub') != 1:
        raise ValueError("Incorrect number of start_hubs")
    elif hub_arr.count('end_hub') != 1:
        raise ValueError("Incorrect number of end_hubs")
    print(hub_arr)
    return hub_dict


def parser(config_file: TextIO) -> None:
    text: str = ""
    origin_arr: list = []
    config_arr: list = []
    config_dict: dict = {}
    hub_dict: dict = {}

    try:
        with open(config_file, "rt") as file:
            text = file.read()
    except FileNotFoundError:
        print("Config file could not be found")
    except PermissionError:
        print("Config file permission do not allow access")

    # turn string into list and remove comments
    origin_arr = text.split('\n')
    config_arr = [line for line in origin_arr if line.startswith('#') is False
                  and line != '']

    # parse the number of drones
    if config_arr[0].startswith('nb_drones:') is False:
        raise ValueError("First line not nb_drones")
    else:
        config_dict.update(string_splitter(config_arr[0]))
        print(config_dict)
    hub_dict = hub_handler(config_arr)
    print(hub_dict)
    print(config_arr)


try:
    parser("./maps/easy/01_linear_path.txt")
except ValueError as alert:
    print(alert)
