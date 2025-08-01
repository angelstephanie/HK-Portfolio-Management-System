from flask import Blueprint, request, jsonify
from backend.models.PortfolioSnap import PortfolioSnap
from backend.service.PortfolioSnap_service import PortfolioSnapService

portfolio_snap_controller = Blueprint('portfolio_snap_controller', __name__)
portfolio_snap_service = PortfolioSnapService()

@portfolio_snap_controller.route('/portfolio_snaps', methods=['GET'])
def get_all_portfolio_snaps():
    try:
        snaps = portfolio_snap_service.get_all_portfolio_snaps()
        return jsonify(snaps), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@portfolio_snap_controller.route('/portfolio_snaps/<int:snap_id>/<string:snap_date>', methods=['GET'])
def get_portfolio_snap_by_id(snap_id, snap_date):
    try:
        snap = portfolio_snap_service.get_portfolio_snap_by_id(snap_id, snap_date)
        if snap:
            return jsonify(snap), 200
        else:
            return jsonify({'message': 'Portfolio Snap not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500  
 
@portfolio_snap_controller.route('/portfolio_snaps', methods=['POST'])
def add_portfolio_snap():
    try:
        snap_data = request.json
        portfolio_snap = PortfolioSnap(**snap_data)
        portfolio_snap_service.add_portfolio_snap(portfolio_snap)
        return jsonify({'message': 'Portfolio Snap added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@portfolio_snap_controller.route('/portfolio_snaps', methods=['PUT'])
def update_portfolio_snap():
    try:
        snap_data = request.json
        portfolio_snap = PortfolioSnap(**snap_data)
        updated_snap = portfolio_snap_service.update_portfolio_snap(portfolio_snap)
        if updated_snap:
            return jsonify({'message': 'Portfolio Snap updated successfully'}), 200
        else:
            return jsonify({'message': 'Portfolio Snap not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500