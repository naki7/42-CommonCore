from in_out_handler import json_to_obj, obj_to_json
from typing import Any
import sys


def main() -> None:
    obj_data: dict[Any, Any] = {}

    if len(sys.argv) == 2:
        obj_data = json_to_obj(sys.argv[1])
        obj_to_json(obj_data)

    print(obj_data)


if __name__ == '__main__':
    main()
