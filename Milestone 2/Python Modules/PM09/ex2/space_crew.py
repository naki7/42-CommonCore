from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime


class Rank(Enum):
    cadet = 1
    officer = 2
    lieutenant = 3
    captain = 4
    commander = 5


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10, alias="mem_id")
    name: str = Field(min_length=2, max_length=50)
    rank: Rank = Field(default=Rank.cadet)
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30, alias="spec")
    years_experience: int = Field(ge=0, le=50, alias="exp")
    is_active: bool = Field(default=True, alias="active")


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15, alias="miss_id")
    mission_name: str = Field(min_length=3, max_length=100, alias="miss_name")
    destination: str = Field(min_length=3, max_length=50, alias="place")
    launch_date: datetime = Field(default=datetime.now(), alias="launch")
    duration_days: int = Field(ge=1, le=3650, alias="duration")
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned", alias="status")
    budget_millions: float = Field(ge=1, le=10000, alias="budget")

    @model_validator(mode='after')
    def mission_validator(self) -> None:
        err_str: str = ""

        if self.mission_id.startswith("M") is False:
            err_str = "Mission IDs should start with \'M\'"
            raise ValueError(err_str)

        crew_count: int = 0
        commander_count: int = 0
        captain_count: int = 0
        experienced_count: int = 0

        for member in self.crew:
            crew_count += 1
            if member.is_active is False:
                err_str = "All members in a crew should be active"
                raise ValueError(err_str)
            if member.rank.value == 5:
                commander_count += 1
            elif member.rank.value == 4:
                captain_count += 1
            if member.years_experience >= 5:
                experienced_count += 1

        if (commander_count + captain_count) < 1:
            err_str = "Mission must have at least one Commander or Captain"
            raise ValueError(err_str)
        if self.duration_days > 365:
            if (crew_count/experienced_count) > 2:
                err_str = "Missions longer than a year should be made up of "
                err_str += "half or more experienced crew members (5+ years)"
                raise ValueError(err_str)
        return self


def main() -> None:
    print("\nSpace Mission Crew Validation")
    print("=========================================")

    sarah: CrewMember = CrewMember(
        mem_id="C_SC_2018",
        name="Sarah Connor",
        rank=Rank.commander,
        age=42,
        spec="Mission Command",
        exp=6
        )
    john: CrewMember = CrewMember(
        mem_id="C_JS_2022",
        name="John Smith",
        rank=Rank.lieutenant,
        age=36,
        spec="Navigation",
        exp=2
        )
    alice: CrewMember = CrewMember(
        mem_id="C_AJ_2019",
        name="Alice Johnson",
        rank=Rank.officer,
        age=40,
        spec="Engineering",
        exp=5
        )
    mars: SpaceMission = SpaceMission(
        miss_id="M2024_MARS",
        miss_name="Mars Colony Establishment",
        place="Mars",
        launch="2024-01-16T08:00:00",
        duration=900,
        crew=[sarah, john, alice],
        budget=2500
        )
    print("Valid mission created:")
    print(f"Mission: {mars.mission_name}")
    print(f"ID: {mars.mission_id}")
    print(f"Destination: {mars.destination}")
    print(f"Duration: {mars.duration_days} days")
    print(f"Budget: ${mars.budget_millions}M")
    print(f"Crew size: {len(mars.crew)}")
    print("Crew members:")
    for member in mars.crew:
        print(f"- {member.name} ({member.rank.name})",
              f"- {member.specialization}")

    print("\n=========================================")
    try:
        full_crew: list[CrewMember] = [john, alice]
        try:
            jessica: CrewMember = CrewMember(
                mem_id="C_JP_2018",
                name="Jessica Parker",
                rank=Rank.lieutenant,
                age=42,
                spec="Mission Command",
                exp=6
                )
            full_crew = [jessica, john, alice]
        except ValidationError as alert:
            print("Expected validation error:")
            all_errors: dict = alert.errors()
            for err in all_errors:
                print(f"{err['loc'][0]}: {err['msg']}")
        mercury: SpaceMission = SpaceMission(
            miss_id="M2024_MERCURY",
            miss_name="Mercury Colony Establishment",
            place="Mercury",
            launch="2024-01-16T08:00:00",
            duration=900,
            crew=full_crew,
            budget=2500
            )
        print("Valid mission created:")
        print(f"Mission: {mercury.mission_name}")
        print(f"ID: {mercury.mission_id}")
        print(f"Destination: {mercury.destination}")
        print(f"Duration: {mercury.duration_days} days")
        print(f"Budget: ${mercury.budget_millions}M")
        print(f"Crew size: {len(mercury.crew)}")
        print("Crew members:")
        for member in mercury.crew:
            print(f"- {member.name} ({member.rank.name})",
                  f"- {member.specialization}")
    except ValidationError as alert:
        print("Expected validation error:")
        alert_msg: list = alert.errors()[0]["msg"].split(', ')
        print(alert_msg[1])


if __name__ == "__main__":
    main()
