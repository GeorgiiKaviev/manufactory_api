from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException, status
from typing import List, Dict

from src.db.repo._base_repo import BaseRepo
from src.db.model.place import Place
from src.db.model.camera import Camera
from src.db.model.placecameralink import PlaceCameraLink


class PlaceRepo(BaseRepo):
    model = Place

    @classmethod
    async def get_all(cls, db: AsyncSession) -> List[model]:
        """
        Get all Place records.
        :param db: The database session.
        :return: A list of all Place records.
        """
        try:
            stmt = select(cls.model)
            result = await db.execute(stmt)
            return list(result.scalars().all())
        except SQLAlchemyError as ex:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=str(ex)
            ) from ex

    @classmethod
    async def get_place_by_id(cls, db: AsyncSession, place_id: int) -> Place:
        """
        Get a Place record by ID.
        :param db: The database session.
        :param place_id: The place ID.
        :return: The Place record.
        """
        try:
            stmt = select(cls.model).filter(cls.model.id == place_id)
            result = await db.execute(stmt)
            place = result.scalars().first()

            if not place:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Place with id {place_id} not found"
                )

            return place
        except SQLAlchemyError as ex:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(ex)
            ) from ex

    @classmethod
    async def get_cameras_by_place_id(cls, db: AsyncSession, place_id: int) -> List[Dict]:
        """
        Get all camera_info by place_id.
        :param db: The database session.
        :param place_id: The place ID.
        :return: A list of camera_info dictionaries.
        """
        try:
            stmt = (
                select(Camera)
                .join(PlaceCameraLink, PlaceCameraLink.camera_id == Camera.id)
                .join(cls.model, PlaceCameraLink.place_id == cls.model.id)
                .filter(cls.model.id == place_id)
            )
            result = await db.execute(stmt)
            return result.scalars().all()
        except SQLAlchemyError as ex:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(ex)
            ) from ex
