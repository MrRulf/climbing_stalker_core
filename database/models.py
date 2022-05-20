from sqlalchemy import DECIMAL, Boolean, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from time import time
from .database import Base


class MeasurementsSet(Base):
    __tablename__ = "measurements_sets"
    id = Column(Integer, primary_key=True, index=True)
    object_id = Column(Integer, nullable=False)
    complete = Column(Boolean, nullable=False, default=False)
    timestamp = Column(Integer, nullable=False, default=time().__floor__())
    measurements = relationship("Measurement", back_populates="set")


class Measurement(Base):
    __tablename__ = "measurements"
    id = Column(Integer, primary_key=True, index=True)
    x_position = Column(DECIMAL, nullable=False)
    y_position = Column(DECIMAL, nullable=False)
    z_position = Column(DECIMAL)
    x_velocity = Column(DECIMAL)
    y_velocity = Column(DECIMAL)
    z_velocity = Column(DECIMAL)
    x_dimension = Column(DECIMAL)
    y_dimension = Column(DECIMAL)
    z_dimension = Column(DECIMAL)
    timestamp = Column(Integer, nullable=False, default=(time() * 1000).__floor__())
    set_id = Column(Integer, ForeignKey("measurements_sets.id"), nullable=False)
    set = relationship("MeasurementsSet", back_populates="measurements")