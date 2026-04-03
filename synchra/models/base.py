from pydantic import BaseModel, ConfigDict

class SynchraBaseModel(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        arbitrary_types_allowed=True,
    )
