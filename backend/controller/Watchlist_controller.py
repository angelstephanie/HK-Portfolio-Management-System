from flask import Blueprint, request, jsonify
from backend.models.Watchlist import Watchlist
from backend.service.Watchlist_service import WatchlistService

watchlist_controller = Blueprint('watchlist_controller', __name__)
watchlist_service = WatchlistService()

@watchlist_controller.route('/watchlist', methods=['GET'])
def get_watchlist():
    try:
        watchlist = watchlist_service.get_watchlist()
        return jsonify([asset.to_dict() for asset in watchlist]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@watchlist_controller.route('/watchlist', methods=['POST'])
def add_asset_to_watchlist():
    try:
        watchlist_data = request.json
        watchlist = Watchlist(**watchlist_data)
        added_watchlist = watchlist_service.add_asset_to_watchlist(watchlist)
        if added_watchlist:
            return jsonify({'message': 'Asset added to watchlist successfully'}), 201
        else:
            return jsonify({'message': 'Asset not found or already in watchlist'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@watchlist_controller.route('/watchlist/<string:symbol>', methods=['DELETE'])
def remove_asset_from_watchlist(symbol):
    try:
        result = watchlist_service.remove_asset_from_watchlist(symbol)
        if result:
            return jsonify({'message': 'Asset removed from watchlist successfully'}), 200
        else:
            return jsonify({'message': 'Asset not found in watchlist'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

