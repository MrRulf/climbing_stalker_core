from itertools import chain
from sqlalchemy.orm import Session

from . import models

def get_measurements_sets_latest(db: Session):
    latest_timestamp = db.query(models.MeasurementsSet).order_by('timestamp').first().id
    return db.query(models.MeasurementsSet).filter(models.MeasurementsSet.timestamp == latest_timestamp)

def get_measurements_sets_id(db: Session, measurements_sets_id):
    return db.query(models.MeasurementsSet).get(measurements_sets_id)

def get_measurements_sets_id_measurements(db: Session, measurements_sets_id):
    return get_measurements_sets_id(measurements_sets_id).measurements

def get_measurements_sets_object(db: Session, object_id):
    return db.query(models.MeasurementsSet).filter(models.MeasurementsSet.object_id == object_id)

def get_measurements_sets(db: Session):
    return db.query(models.MeasurementsSet)

def get_measurements_latest(db: Session):
    measurements_sets = get_measurements_sets_latest()
    measurements = []
    for set in measurements_sets:
        measurements = chain(measurements, set.measurements)
    return measurements

def get_measurements_object(db: Session, object_id):
    measurements_sets = get_measurements_sets_object(object_id)
    measurements = []
    for set in measurements_sets:
        measurements = chain(measurements, set.measurements)
    return measurements

def get_measurements_id(db: Session, measurements_id: int):
    return db.query(models.Measurement).get(models.Measurement.id == measurements_id)

def get_measurements(db: Session):
    return db.query(models.Measurement)