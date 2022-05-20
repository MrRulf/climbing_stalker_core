from typing import List, Optional
from pydantic import BaseModel


class MeasurementBase(BaseModel):
    x_position: int
    y_position: int
    z_position: Optional[int] = None
    x_velocity: Optional[int] = None
    y_velocity: Optional[int] = None
    z_velocity: Optional[int] = None
    x_dimension: Optional[int] = None
    y_dimension: Optional[int] = None
    z_dimension: Optional[int] = None
    timestamp: int

class MeasurementCreate(MeasurementBase):
    pass

class Measurement(MeasurementBase):
    id: int
    set_id: int

    class Config:
        orm_mode = True


class MeasurementsSetBase(BaseModel):
    object_id: int
    complete: bool
    timestamp: int

class MeasurementsSetCreate(MeasurementsSetBase):
    pass

class MeasurementsSet(MeasurementsSetBase):
    id: int
    measurements: List[Measurement] = []

    class Config:
        orm_mode = True