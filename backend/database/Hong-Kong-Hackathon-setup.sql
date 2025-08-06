CREATE DATABASE IF NOT EXISTS HongKongHackathon; 
USE HongKongHackathon;

CREATE TABLE IF NOT EXISTS Portfolios (
                    portfolio_id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    description TEXT,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                );

CREATE TABLE IF NOT EXISTS Assets(
                    symbol VARCHAR(20) PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    type ENUM('stock', 'crypto', 'etf', 'bond'),
                    current_price DECIMAL(15, 2),
                    opening_price DECIMAL(15, 2),
                    last_updated TIMESTAMP
                );

CREATE TABLE IF NOT EXISTS Holdings (
                    holding_id INT AUTO_INCREMENT PRIMARY KEY,
                    portfolio_id INT NOT NULL,
                    symbol VARCHAR(20) NOT NULL,
                    quantity DECIMAL(15, 6) NOT NULL, 
                    avg_buy_price DECIMAL(15, 2) NOT NULL,
                    FOREIGN KEY (portfolio_id) REFERENCES Portfolios(portfolio_id),
                    FOREIGN KEY (symbol) REFERENCES Assets(symbol)
                );

CREATE TABLE IF NOT EXISTS Transactions (
                    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
                    portfolio_id INT NOT NULL,
                    symbol VARCHAR(20) NOT NULL,
                    type ENUM('buy', 'sell') NOT NULL,
                    quantity DECIMAL(15, 6) NOT NULL,
                    price_per_unit DECIMAL(15, 2) NOT NULL,
                    fee DECIMAL(15, 2) DEFAULT 0,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    notes TEXT,
                    FOREIGN KEY (portfolio_id) REFERENCES Portfolios(portfolio_id),
                    FOREIGN KEY (symbol) REFERENCES Assets(symbol)
                );

CREATE TABLE IF NOT EXISTS PortfolioSnaps (
                    portfolio_id INT NOT NULL,
                    snapshot_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                    cash_value DECIMAL(10, 2) NOT NULL,
                    invested_value DECIMAL(10, 2) NOT NULL,
                    FOREIGN KEY (portfolio_id) REFERENCES Portfolios(portfolio_id),
                    PRIMARY KEY (portfolio_id, snapshot_date)
                );

INSERT INTO Portfolios (name, description)
                VALUES ('Default', "This is the default portfolio");
INSERT INTO Holdings (portfolio_id, symbol, quantity, avg_buy_price)
                VALUES (1, 'AAPL', 10, 150.00);
INSERT INTO PortfolioSnaps (portfolio_id, cash_value, invested_value)
                VALUES (1, 10000.00, 1500.00);
INSERT INTO Transactions (portfolio_id, symbol, type, quantity, price_per_unit, fee, notes)
                VALUES (1, 'AAPL', 'sell', 1, 150.00, 5.00, 'Initial purchase of Apple stock');