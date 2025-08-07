INSERT INTO Portfolios (name, description)
                VALUES ('Default', "This is the default portfolio");
INSERT INTO Holdings (portfolio_id, symbol, quantity, avg_buy_price)
                VALUES (1, 'AAPL', 10, 150.00);
INSERT INTO PortfolioSnaps (portfolio_id, cash_value, invested_value)
                VALUES (1, 10000.00, 1500.00);
INSERT INTO Transactions (portfolio_id, symbol, type, quantity, price_per_unit, fee, notes)
                VALUES (1, 'AAPL', 'sell', 1, 150.00, 5.00, 'Initial purchase of Apple stock');