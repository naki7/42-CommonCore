from typing import TextIO, Union, Any
from pydantic import BaseModel, Field, field_validator, ValidationInfo
from pydantic import model_validator


def string_splitter(line: str) -> dict:
    result_arr: list = []
    dict_set: dict = {}

    result_arr = line.split(': ')
    try:
        dict_set = {result_arr[0]: int(result_arr[1])}
    except IndexError:
        print('invalid input for keys and pairs')
        raise ValueError(f'{line}')
    return dict_set


class HubStruct(BaseModel):
    name: str = Field(min_length=1)
    x: int = Field()
    y: int = Field()
    zone: Union[str, None] = Field(default='normal')
    color: Union[str, None] = Field(default='none')
    max_drones: Union[int, None] = Field(ge=0, default=1)

    @field_validator('zone', 'color', 'max_drones')
    @classmethod
    def set_defaults(cls, value: str, info: ValidationInfo) -> Any:
        if value is None:
            return cls.model_fields[info.field_name].get_default()
        return value

    @model_validator(mode='after')
    def values_validator(self) -> Any:
        zone_arr: list = ['normal', 'blocked', 'restricted', 'priority']
        if zone_arr.count(self.zone) != 1:
            print('invalid zone inserted')
            raise ValueError(f'{self.zone}')
        return self


def hub_handler(config_arr: list) -> dict:
    hub_dict: dict = {
        'start_hub': {},
        'end_hub': {}
    }
    hub_arr: list = [line for line in config_arr if
                     line.startswith("hub") is True
                     or line.startswith("start_hub") is True
                     or line.startswith("end_hub") is True]
    start_hub: list = [line for line in config_arr if
                       line.startswith("start_hub") is True]
    end_hub: list = [line for line in config_arr if
                     line.startswith("end_hub") is True]
    name_arr: list = []

    # check for valid num of start and end hubs (1 each)
    if len(start_hub) != 1:
        print('Incorrect number of start_hubs')
        if len(start_hub) < 1:
            raise ValueError('no start_hubs')
        else:
            raise ValueError(f'{start_hub[1]}')
    elif len(end_hub) != 1:
        print('Incorrect number of end_hubs')
        if len(start_hub) < 1:
            raise ValueError('no start_hubs')
        else:
            raise ValueError(f'{start_hub[1]}')

    # validate and assign each line/hub
    for line in hub_arr:
        temp_arr: list = line.split(' ')
        extras_arr: list = [value for value in temp_arr if
                            value.count('zone') != 0 or
                            value.count('color') != 0 or
                            value.count('max_drones') != 0]

        # check names are all different
        if name_arr.count(temp_arr[1]) == 0:
            name_arr.append(temp_arr[1])
        else:
            print('multiple hubs with the same name')
            raise ValueError(f'{line}')

        zone: str = None
        color: str = None
        max_drones: int = None
        for item in extras_arr:
            stripped: str = item.strip('[]')
            temp_extra: list = stripped.split('=')

            # check if the zone's name has a dash
            if temp_arr[1].count('-') != 0:
                print('dash in zone name')
                raise ValueError(f'{item}')

            # handle metadata first
            if temp_extra[0] == 'zone':
                if zone is None:
                    zone = temp_extra[1]
                else:
                    print('More than 1 zone')
                    raise ValueError(f'{item}')
            elif temp_extra[0] == 'color':
                if color is None:
                    color = temp_extra[1]
                else:
                    print('More than 1 color')
                    raise ValueError(f'{item}')
            elif temp_extra[0] == 'max_drones':
                if max_drones is None:
                    max_drones = int(temp_extra[1])
                else:
                    print('More than 1 max_drones')
                    raise ValueError(f'{item}')
            elif len(extras_arr) != 0:
                raise ValueError(temp_extra)

        # passing input into specific hub definer
        if temp_arr[0] == 'start_hub:':
            hub_dict["start_hub"] = HubStruct(
                name=temp_arr[1],
                x=int(temp_arr[2]),
                y=int(temp_arr[3]),
                zone=zone,
                color=color,
                max_drones=max_drones
                )
        elif temp_arr[0] == 'end_hub:':
            hub_dict["end_hub"] = HubStruct(
                name=temp_arr[1],
                x=int(temp_arr[2]),
                y=int(temp_arr[3]),
                zone=zone,
                color=color,
                max_drones=max_drones
                )
        elif temp_arr[0] == 'hub:':
            hub_dict[f"{temp_arr[1]}_hub"] = HubStruct(
                name=temp_arr[1],
                x=int(temp_arr[2]),
                y=int(temp_arr[3]),
                zone=zone,
                color=color,
                max_drones=max_drones
                )
    return hub_dict


def connection_handler(config_arr: list, hub_names: list) -> dict:
    connect_dict: dict = {}
    connect_arr: list = [line.split(': ') for line in config_arr if
                         line.startswith("connection") is True]
    link_arr: list = [line[1].split(' ') for line in connect_arr if
                      line[1].find('max_link_capacity') != -1]
    hub_dict: dict = {}

    # removes all extra text so just the connections themselves remain
    connect_arr = [line[1] for line in connect_arr]

    # loops over each connection to split the connections based on '-'
    for i in range(0, len(connect_arr)):
        connect_dict[i] = connect_arr[i].split('-')

        # checks for extra criteria to then append for later usage
        if connect_dict[i][1].find('max_link_capacity') != -1:
            connect_dict[i][1] = connect_dict[i][1].split(' ')
            connect_dict[i][1] = connect_dict[i][1][0]

    # goes over each connection to make sure that there are no errors
    for i in range(0, len(connect_dict)):
        if connect_dict[i][0] == connect_dict[i][1]:
            print('waypoints in connection are the same')
            raise ValueError(f'{connect_dict[i][0]}-{connect_dict[i][1]}')
        if hub_names.count(connect_dict[i][0]) != 1:
            print('waypoint in connection not predefined')
            raise ValueError(f'{connect_dict[i][0]}')
        if hub_names.count(connect_dict[i][1]) != 1:
            print('waypoint in connection not predefined')
            raise ValueError(f'{connect_dict[i][1]}')
        # checks to see if the connection has been used before
        if hub_dict.get(connect_dict[i][0]) is None:
            if hub_dict.get(connect_dict[i][1]) is None:
                hub_dict[connect_dict[i][0]] = {connect_dict[i][1]}
            else:
                try:
                    hub_dict[connect_dict[i][1]].remove(connect_dict[i][0])
                    print('connection was already defined before')
                    temp_error = f'{connect_dict[i][0]}-{connect_dict[i][1]}'
                    raise ValueError(temp_error)
                except KeyError:
                    hub_dict[connect_dict[i][0]].add(connect_dict[i][1])
        else:
            try:
                hub_dict[connect_dict[i][0]].remove(connect_dict[i][1])
                print('connection was already defined before')
                raise ValueError(f'{connect_dict[i][0]}-{connect_dict[i][1]}')
            except KeyError:
                hub_dict[connect_dict[i][0]].add(connect_dict[i][1])

    # parse max_link_capacity
    for connection in link_arr:
        connection.append(int(connection[1].strip('[max_link_capacity=]')))
        temp_connections = connection[0].split('-')
        connection[1] = temp_connections[1]
        connection[0] = temp_connections[0]
        for link in connect_dict:
            if connect_dict[link][0] == connection[0]:
                if connect_dict[link][1] == connection[1]:
                    if connection[2] < 1:
                        print('invalid max_link_capacity used')
                        raise ValueError(f'max_link_capacity={connection[2]}')
                    else:
                        connect_dict[link].append(connection[2])
    # add the default to connections without a specified criteria
    for connection in connect_dict:
        if len(connect_dict[connection]) != 3:
            connect_dict[connection].append(1)

    return connect_dict


def parser(origin_arr: list) -> dict:
    config_arr: list = []
    config_dict: dict = {}
    hub_dict: dict = {}
    hub_names: list = []
    connections_dict: dict = {}

    # remove comments and blank lines
    config_arr = [line for line in origin_arr if line.startswith('#') is False
                  and line != '']

    # parses the number of drones
    if config_arr[0].startswith('nb_drones:') is False:
        raise ValueError("nb_drones")
    else:
        config_dict.update(string_splitter(config_arr[0]))

    # parses the hubs
    hub_dict = hub_handler(config_arr)
    config_dict['hubs'] = {}
    for key in hub_dict:
        config_dict['hubs'][key] = hub_dict[key]

    # parses the connections
    hub_names = [hub_dict[key].name for key in hub_dict if key != 'nb_drones']
    connections_dict = connection_handler(config_arr, hub_names)
    # instead of printing add to main dict
    config_dict['connections'] = {}
    for key in connections_dict:
        config_dict['connections'][key] = connections_dict[key]
    return config_dict


def parser_main(config_file: TextIO) -> dict:
    text: str = ""
    origin_arr: list = []
    parse_result: dict = {}

    # Read file, and then split the file from newlines into subscriptable list
    try:
        with open(config_file, "rt") as file:
            text = file.read()
    except FileNotFoundError:
        print("Config file could not be found")
    except PermissionError:
        print("Config file permission do not allow access")
    origin_arr = text.split('\n')

    try:
        parse_result = parser(origin_arr)
        return parse_result
    except ValueError as alert:
        if f'{alert}' == 'nb_drones':
            print(f'Error: {alert} not on first line\n    Found on line 1')
        elif f'{alert}' == 'no start' or alert == 'no end':
            print(f'Error: {alert}_hubs\n   Found in lines 1 to ',
                  f'{len(origin_arr)}')
        else:
            for i in range(0, len(origin_arr)):
                if origin_arr[i].find(f'{alert}') != -1:
                    print(f"Error: {alert}\n    Found on line {i + 1}",
                          f"of {config_file}")
