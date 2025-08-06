from flask import Blueprint, request, jsonify
from backend.models.Asset import Asset
from backend.service.Asset_service import AssetService

asset_controller = Blueprint('asset_controller', __name__)
asset_service = AssetService()

@asset_controller.route('/assets', methods=['GET'])
def get_all_assets():
    try:
        assets = asset_service.get_all_assets()
        return jsonify([asset.to_dict() for asset in assets]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@asset_controller.route('/assets/<string:symbol>', methods=['GET'])
def get_asset_by_symbol(symbol):
    print("Symbol: ", symbol)
    try:
        asset = asset_service.get_asset_by_symbol(symbol)
        if asset:
            return jsonify(asset.to_dict()), 200
        else:
            return jsonify({'message': 'Asset not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@asset_controller.route('/assets', methods=['POST'])
def add_asset():
    try:
        asset_data = request.json
        asset = Asset(**asset_data)
        added_asset = asset_service.add_asset(asset)
        if added_asset:
            return jsonify({'message': 'Asset added successfully'}), 201
        else:
            return jsonify({'message': 'Asset not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@asset_controller.route('/assets/<string:symbol>', methods=['PUT'])
def update_asset(symbol):
    try:
        asset_data = request.json
        asset_data['symbol'] = symbol
        asset = Asset(**asset_data)
        updated_asset = asset_service.update_asset(asset)
        if updated_asset:
            return jsonify({'message': 'Asset updated successfully'}), 200
        else:
            return jsonify({'message': 'Asset not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@asset_controller.route('/assets/<string:symbol>/historicprice/<string:date>', methods=['GET'])
def get_price_by_range(symbol, date):
    try:
        price = asset_service.get_price_by_range(symbol, date)
        if price:
            return jsonify(price), 200
        else:
            return jsonify({'message': 'Historic price could not be fetched'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@asset_controller.route('/assets/<string:symbol>/historicprice/<int:period>', methods=['GET'])
def get_price_within_day(symbol, period):
    try:
        price = asset_service.get_price_within_day(symbol, period)
        if price:
            return jsonify(price), 200
        else:
            return jsonify({'message': 'Historic price could not be fetched'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500