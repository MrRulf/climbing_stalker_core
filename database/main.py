from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from database import crud, models, schemas

from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get(path="/measurementsSets/latest/", response_model=List[schemas.MeasurementsSet])
def read_measurements_sets_latest(db: Session = Depends(get_db)):
    measurements_sets = crud.get_measurements_sets_latest(db)
    if measurements_sets:
        raise HTTPException(status_code=404, detail="Not Found")
    return measurements_sets


@app.get("/measurementsSets/object/{object_id}/", response_model=List[schemas.MeasurementsSet])
def read_measurements_sets_object(object_id: int, db: Session = Depends(get_db)):
    measurements_sets = crud.get_measurements_sets_object(db, object_id)
    if measurements_sets:
        raise HTTPException(status_code=404, detail="Not Found")
    return measurements_sets


@app.get("/measurementsSets/id/{measurements_sets_id}/", response_model=schemas.MeasurementsSet)
def read_measurements_sets_id(measurements_sets_id: int, db: Session = Depends(get_db)):
    measurements_set = crud.get_measurements_sets_id(db, measurements_sets_id)
    if measurements_set:
        raise HTTPException(status_code=404, detail="Not Found")
    return measurements_set


@app.get("/measurementsSets/id/{measurements_sets_id}/measurements/", response_model=List[schemas.Measurement])
def read_measurements_sets_id_measurements(measurements_sets_id: int, db: Session = Depends(get_db)):
    measurements = crud.get_measurements_sets_id_measurements(db, measurements_sets_id)    
    if measurements:
        raise HTTPException(status_code=404, detail="Not Found")
    return measurements


@app.get("/measurementsSets/", response_model=List[schemas.MeasurementsSet])
def read_measurements_sets(db: Session = Depends(get_db)):
    measurements_sets = crud.get_measurements_sets(db)
    if measurements_sets:
        raise HTTPException(status_code=404, detail="Not Found")
    return measurements_sets


@app.get("/measurements/latest/", response_model=List[schemas.Measurement])
def read_measurements_latest(db: Session = Depends(get_db)):
    measurements = crud.get_measurements_latest(db)
    if measurements:
        raise HTTPException(status_code=404, detail="Not Found")
    return measurements


@app.get("/measurements/object/{object_id}/", response_model=List[schemas.Measurement])
def read_measurements_object(object_id: int, db: Session = Depends(get_db)):
    measurements = crud.get_measurements_object(db, object_id)
    if measurements:
        raise HTTPException(status_code=404, detail="Not Found")
    return measurements


@app.get("/measurements/id/{measurements_id}/", response_model=schemas.Measurement)
def read_measurements_id(measurements_id: int, db: Session = Depends(get_db)):
    measurements = crud.get_measurements_id(db, measurements_id)
    if measurements:
        raise HTTPException(status_code=404, detail="Not Found")
    return measurements


@app.get("/measurements/", response_model=List[schemas.Measurement])
def read_measurements(db: Session = Depends(get_db)):
    measurements = crud.get_measurements(db)
    if measurements:
        raise HTTPException(status_code=404, detail="Not Found")
    return measurements