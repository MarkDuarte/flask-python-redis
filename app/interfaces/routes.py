from flask import Blueprint, request, jsonify
from app.domain.models import UserSession
from app.domain.services import SessionService

routes = Blueprint("routes", __name__)

def create_routes(session_service: SessionService):
  @routes.route("/session", methods=["POST"])
  def create_session():
    data = request.json
    session = UserSession(**data)
    session_service.create_session(session)
    return jsonify({"message": "Session created"}), 201
  
  @routes.route("/session/<user_id>", methods=["GET"])
  def get_session(user_id: str):
    session_data = session_service.get_session(user_id)
    if session_data:
      return jsonify({"session_data": session_data}), 200
    return jsonify({"message": "Session not found"}), 404
  
  @routes.route("/session/<user_id>", methods=["DELETE"])
  def delete_session(user_id: str):
    session_service.delete_session(user_id)
    return jsonify({"message": "Session deleted"}), 200
  
  return routes