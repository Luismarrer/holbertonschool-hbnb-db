"""
Amenity controller module
"""

from flask import abort, request
from src.models.amenity import Amenity
from flask_jwt_extended import jwt_required
from .login import check_admin

@jwt_required()
def get_amenities():
    """Returns all amenities"""
    amenities: list[Amenity] = Amenity.get_all()

    return [amenity.to_dict() for amenity in amenities]

@jwt_required()
def create_amenity():
    """Creates a new amenity"""
    if check_admin():
        data = request.get_json()

        try:
            amenity = Amenity.create(data)
        except KeyError as e:
            abort(400, f"Missing field: {e}")
        except ValueError as e:
            abort(400, str(e))

        return amenity.to_dict(), 201
    else:
        return "You do not have permission to create an amenity", 403


def get_amenity_by_id(amenity_id: str):
    """Returns a amenity by ID"""
    amenity: Amenity | None = Amenity.get(amenity_id)

    if not amenity:
        abort(404, f"Amenity with ID {amenity_id} not found")

    return amenity.to_dict()

@jwt_required()
def update_amenity(amenity_id: str):
    """Updates a amenity by ID"""
    if check_admin():
        data = request.get_json()

        updated_amenity: Amenity | None = Amenity.update(amenity_id, data)

        if not updated_amenity:
            abort(404, f"Amenity with ID {amenity_id} not found")

        return updated_amenity.to_dict()
    else:
        return "You do not have permission to update an amenity", 403

@jwt_required()
def delete_amenity(amenity_id: str):
    """Deletes a amenity by ID"""
    if check_admin():
        if not Amenity.delete(amenity_id):
            abort(404, f"Amenity with ID {amenity_id} not found")

        return "", 204
    else:
        return "You do not have permission to delete an amenity", 403
