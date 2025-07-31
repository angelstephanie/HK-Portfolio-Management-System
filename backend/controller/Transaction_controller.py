from flask import Blueprint, request, jsonify
from backend.models.Transaction import Transaction
from backend.service.Transaction_service import TransactionService

transaction_controller = Blueprint('transaction_controller', __name__)
transaction_service = TransactionService()

@transaction_controller.route('/transactions', methods=['GET'])
def get_all_transactions():
    try:
        transactions = transaction_service.get_all_transactions()
        return jsonify(transactions), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@transaction_controller.route('/transactions/<int:transaction_id>', methods=['GET'])
def get_transaction_by_id(transaction_id):
    try:
        transaction = transaction_service.get_transaction_by_id(transaction_id)
        if transaction:
            return jsonify(transaction), 200
        else:
            return jsonify({'message': 'Transaction not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@transaction_controller.route('/transactions', methods=['POST'])
def add_transaction():
    try:
        data = request.get_json()
        transaction = Transaction(**data)
        new_transaction = transaction_service.add_transaction(transaction)
        return jsonify(new_transaction), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@transaction_controller.route('/transactions/<int:transaction_id>', methods=['DELETE'])
def delete_transaction(transaction_id):
    try:
        result = transaction_service.delete_transaction(transaction_id)
        if result:
            return jsonify({'message': 'Transaction deleted successfully'}), 200
        else:
            return jsonify({'message': 'Transaction not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500