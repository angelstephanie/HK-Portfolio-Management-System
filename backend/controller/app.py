from flask import Flask
from backend.controller.Asset_controller import asset_controller
from backend.controller.Holdings_controller import holdings_controller
from backend.controller.Portfolio_controller import portfolio_controller
from backend.controller.Transaction_controller import transaction_controller
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(asset_controller)
app.register_blueprint(holdings_controller)
app.register_blueprint(portfolio_controller)   
app.register_blueprint(transaction_controller)

if __name__ == '__main__':
    app.run(debug=True)
