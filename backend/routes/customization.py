from flask import Blueprint, request, jsonify

customization_bp = Blueprint('customization_bp', __name__)

@customization_bp.route('/design', methods=['POST'])
def design():
    data = request.json
    return jsonify({"message": "Design saved successfully", "data": data})
