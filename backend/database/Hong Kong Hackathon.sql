USE HongKongHackathon;

CREATE TABLE Portfolios (
    portfolio_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Assets (
    symbol VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    type ENUM('stock', 'crypto', 'etf', 'bond'),
    current_price DECIMAL(15, 2),
    last_updated TIMESTAMP
);

CREATE TABLE Holdings (
    holding_id INT AUTO_INCREMENT PRIMARY KEY,
    portfolio_id INT NOT NULL,
    symbol VARCHAR(20) NOT NULL,
    quantity DECIMAL(15, 6) NOT NULL, 
    avg_buy_price DECIMAL(15, 2) NOT NULL,
    FOREIGN KEY (portfolio_id) REFERENCES Portfolios(portfolio_id),
    FOREIGN KEY (symbol) REFERENCES Assets(symbol)
);

CREATE TABLE Transactions (
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
