from flask import Blueprint, request, jsonify
from backend.service.Asset_service import AssetService

asset_controller = Blueprint('asset_controller', __name__)
asset_service = AssetService()

@asset_controller.route('/assets', methods=['GET'])
def get_all_assets():
    try:
        assets = asset_service.get_all_assets()
        return jsonify(assets), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@asset_controller.route('/assets/<string:symbol>', methods=['GET'])
def get_asset_by_symbol(symbol):
    try:
        asset = asset_service.get_asset_by_symbol(symbol)
        if asset:
            return jsonify(asset), 200
        else:
            return jsonify({'message': 'Asset not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500