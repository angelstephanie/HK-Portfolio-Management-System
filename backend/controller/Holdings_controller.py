from flask import Blueprint, request, jsonify
from backend.models.Holdings import Holdings
from backend.service.Holdings_service import HoldingsService

holdings_controller = Blueprint('holdings_controller', __name__)
holdings_service = HoldingsService()

@holdings_controller.route('/holdings', methods=['GET'])
def get_all_holdings():
    try:
        holdings = holdings_service.get_all_holdings()
        return jsonify([holding.to_dict() for holding in holdings]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@holdings_controller.route('/holdings/<int:portfolio_id>', methods=['GET'])
def get_holdings_by_id(portfolio_id):
    try:
        holdings = holdings_service.get_holdings_by_id(portfolio_id)
        if holdings:
            return jsonify([holding.to_dict() for holding in holdings]), 200
        else:
            return jsonify({'message': 'Portfolio not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@holdings_controller.route('/holdings', methods=['POST'])
def add_holding():
    try:
        data = request.get_json()
        holding = Holdings(**data)
        new_holding = holdings_service.add_holding(holding)
        if new_holding:
            return jsonify({'message': 'Holding added successfully'}), 201
        else:
            return jsonify({'message': 'Holding not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@holdings_controller.route('/holdings/<int:holding_id>', methods=['DELETE'])
def delete_holding(holding_id):
    try:
        result = holdings_service.delete_holding(holding_id)
        if result:
            return jsonify({'message': 'Holding deleted successfully'}), 200
        else:
            return jsonify({'message': 'Holding not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@holdings_controller.route('/holdings', methods=['PUT'])
def update_holding():
    try:
        holding_data = request.json
        holding = Holdings(**holding_data)
        updated_holding = holdings_service.update_holding(holding)
        if updated_holding:
            return jsonify({'message': 'Holding updated successfully'}), 200
        else:
            return jsonify({'message': 'Holding not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500