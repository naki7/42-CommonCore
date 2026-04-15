from pydantic import BaseModel, Field, ValidationError
from typing import Optional
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=30, alias='id')
    name: str = Field(min_length=1, max_length=50, alias='name')
    crew_size: int = Field(ge=1, le=20, alias='crew')
    power_level: float = Field(ge=0, le=100, alias='power')
    oxygen_level: float = Field(ge=0, le=100, alias='oxygen')
    last_maintenance: datetime = Field(default=datetime.now(),
                                       alias='maintenance')
    is_operational: bool = Field(default=True, alias='operational')
    notes: Optional[str] = Field(default='', max_length=200, alias='notes')


def main() -> None:
    print("\nSpace Station Data Validation")
    print("========================================")
    valid_station = SpaceStation(
        id="ISS001",
        name="International Space Station",
        crew=6,
        power=85.5,
        oxygen=92.3,
        maintenance='2077-12-13T20:30:00'
        )
    print("Valid station created:")
    print(f"ID: {valid_station.station_id}",
          f"Name: {valid_station.name}",
          f"Crew: {valid_station.crew_size} people",
          f"Power: {valid_station.power_level}%",
          f"Oxygen: {valid_station.oxygen_level}%",
          sep="\n")
    if valid_station.is_operational is True:
        print("Status: Operational")
    else:
        print("Status: Non-functional")

    print("\n========================================")
    print("Expected validation error:")
    try:
        invalid_station = SpaceStation(
            id="ISS001",
            name="International Space Station",
            crew=25,
            power=85.5,
            oxygen=92.3,
            maintenance='2077-12-13T20:30:00'
            )
        print(f"ID: {invalid_station.station_id}",
              f"Name: {invalid_station.name}",
              f"Crew: {invalid_station.crew_size}",
              f"Power: {invalid_station.power_level}",
              f"Oxygen: {invalid_station.oxygen_level}",
              sep="\n")
        if valid_station.is_operational is True:
            print("Status: Operational")
        else:
            print("Status: Non-functional")
    except ValidationError as alert:
        all_errors: dict = alert.errors()
        for err in all_errors:
            print(f"{err['loc'][0]}: {err['msg']}")


if __name__ == "__main__":
    main()
