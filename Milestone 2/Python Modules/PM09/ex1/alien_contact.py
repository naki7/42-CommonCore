from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing import Optional


class ContactType(Enum):
    radio = 1
    visual = 2
    physical = 3
    telepathic = 4


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15, alias='id')
    timestamp: datetime = Field(default=datetime.now(), alias='time')
    location: str = Field(min_length=3, max_length=100, alias='place')
    contact_type: ContactType = Field(default=ContactType.radio, alias='type')
    signal_strength: float = Field(ge=0, le=10, alias='strength')
    duration_minutes: int = Field(ge=1, le=1440, alias='duration')
    witness_count: int = Field(ge=1, le=100, alias='witnesses')
    message_received: Optional[str] = Field(default="", max_length=500,
                                            alias='message')
    is_verified: bool = Field(default=False, alias='verification')

    @model_validator(mode='after')
    def contact_validator(self) -> None:
        err_str: str = ""
        if self.contact_id.startswith("AC") is False:
            err_str = "Contact ID must start with AC"
            raise ValueError(err_str)
        if self.contact_type == ContactType.physical:
            if self.is_verified is False:
                err_str = "Physical contact should be verified"
                raise ValueError(err_str)
        elif self.contact_type == ContactType.telepathic:
            if self.witness_count < 3:
                err_str = "Telepathic contact requires at least 3 witnesses"
                raise ValueError(err_str)
        if self.signal_strength > 7:
            if self.message_received is None:
                err_str = "Signals above 7.0 should include messages"
                raise ValueError(err_str)
        return self


def main() -> None:
    print("\nAlien Contact Log Validation")
    print("======================================")
    valid_contact: AlienContact = AlienContact(
        id="AC_2024_001",
        time="1978-09-11T16:36:45",
        place="Area 51, Nevada",
        strength=8.5,
        duration=45,
        witnesses=5,
        message="\'Greetings from Zeta Reticuli\'",
        verification=True
    )
    print("Valid contact report:")
    print(f"ID: {valid_contact.contact_id}",
          f"Type: {valid_contact.contact_type.name}",
          f"Location: {valid_contact.location}",
          f"Signal: {valid_contact.signal_strength}/10",
          f"Duration: {valid_contact.duration_minutes} minutes",
          f"Witnesses: {valid_contact.witness_count}",
          f"Message: {valid_contact.message_received}",
          sep="\n")

    print("\n========================================")
    print("Expected validation error:")
    try:
        invalid_contact = AlienContact(
            id="AC_2024_002",
            type=ContactType.telepathic,
            time="1978-12-11T16:36:45",
            place="Area 51, Nevada",
            strength=8.5,
            duration=45,
            witnesses=2,
            message="\'Greetings from Zeta Reticuli\'",
            verification=True
            )
        print(f"ID: {invalid_contact.contact_id}",
              f"Type: {invalid_contact.contact_type.name}",
              f"Location: {invalid_contact.location}",
              f"Signal: {invalid_contact.signal_strength}/10",
              f"Duration: {invalid_contact.duration_minutes} minutes",
              f"Witnesses: {invalid_contact.witness_count}",
              f"Message: {invalid_contact.message_received}",
              sep="\n")
    except ValidationError as alert:
        alert_msg: list = alert.errors()[0]["msg"].split(', ')
        print(alert_msg[1])


if __name__ == "__main__":
    main()
