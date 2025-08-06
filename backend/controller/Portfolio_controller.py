from flask import Blueprint, request, jsonify
from backend.service.Portfolio_service import PortfolioService

portfolio_controller = Blueprint('portfolio_controller', __name__)
portfolio_service = PortfolioService()

@portfolio_controller.route('/portfolios', methods=['GET'])
def get_all_portfolios():
    try:
        portfolios = portfolio_service.get_all_portfolios()
        return jsonify([portfolio.to_dict() for portfolio in portfolios]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@portfolio_controller.route('/portfolios/<int:portfolio_id>', methods=['GET'])
def get_portfolio_by_id(portfolio_id):
    try:
        portfolio = portfolio_service.get_portfolio_by_id(portfolio_id)
        if portfolio:
            return jsonify(portfolio.to_dict()), 200
        else:
            return jsonify({'message': 'Portfolio not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@portfolio_controller.route('/portfolios/<int:portfolio_id>', methods=['PUT'])
def update_portfolio(portfolio_id):
    try:
        data = request.get_json()
        updated_portfolio = portfolio_service.update_portfolio(portfolio_id, data)
        if updated_portfolio:
            return jsonify({'message': 'Portfolio updated successfully'}), 200
        else:
            return jsonify({'message': 'Portfolio not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500