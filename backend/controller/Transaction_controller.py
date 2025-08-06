from datetime import datetime
from flask import Blueprint, request, jsonify
from backend.models.Transaction import Transaction, TransactionType
from backend.service.Transaction_service import TransactionService

transaction_controller = Blueprint('transaction_controller', __name__)
transaction_service = TransactionService()

@transaction_controller.route('/transactions', methods=['GET'])
def get_all_transactions():
    try:
        transactions = transaction_service.get_all_transactions()
        return jsonify([transaction for transaction in transactions]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@transaction_controller.route('/transactions/<int:transaction_id>', methods=['GET'])
def get_transaction_by_id(transaction_id):
    try:
        transaction = transaction_service.get_transaction_by_id(transaction_id)
        if transaction:
            return jsonify(transaction.to_dict()), 200
        else:
            return jsonify({'message': 'Transaction not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@transaction_controller.route('/transactions', methods=['POST'])
def add_transaction():
    try:
        data = request.get_json()
        data['type'] = TransactionType(data['type'])
        transaction = Transaction(**data)
        new_transaction = transaction_service.add_transaction(transaction)
        if new_transaction:
            return jsonify({'message': 'Transaction added successfully'}), 201
        else:
            return jsonify({'message': 'Transaction not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@transaction_controller.route('/transactions/<int:transaction_id>', methods=['PUT'])
def update_transaction(transaction_id):
    try:
        data = request.get_json()
        data['transaction_id'] == transaction_id
        data['type'] = TransactionType(data['type'])
        transaction = Transaction(**data)
        updated_transaction = transaction_service.update_transaction(transaction)
        if updated_transaction:
            return jsonify({'message': 'Transaction updated successfully'}), 201
        else:
            return jsonify({'message': 'Transaction not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# @transaction_controller.route('/transactions/<int:transaction_id>', methods=['DELETE'])
# def delete_transaction(transaction_id):
#     try:
#         result = transaction_service.delete_transaction(transaction_id)
#         if result:
#             return jsonify({'message': 'Transaction deleted successfully'}), 200
#         else:
#             return jsonify({'message': 'Transaction not found'}), 404
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500