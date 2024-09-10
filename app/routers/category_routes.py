import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models import Category
from app.schemas.category_schema import CategoryReturn, CategoryCreate
from app.db_connection import SessionLocal, get_db_session
from app.utils.category_utils import check_existing_category

router = APIRouter()
db = SessionLocal()
logger = logging.getLogger(__name__)


@router.post("/", response_model=CategoryReturn, status_code=201)
def create_category(category_data: CategoryCreate, db: Session = Depends(get_db_session)):



    try:
        check_existing_category(db, category_data)
        new_category = Category(**category_data.model_dump())
        db.add(new_category)
        db.commit()
        db.refresh(new_category)
        return new_category
    except HTTPException:
        raise

    except Exception as e:
        db.rollback()
        logger.error(f"unexpected error while creating category: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")



