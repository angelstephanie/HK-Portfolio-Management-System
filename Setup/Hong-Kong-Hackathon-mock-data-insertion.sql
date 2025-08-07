INSERT INTO Portfolios (name, description)
                VALUES ('Default', "This is the default portfolio");
INSERT INTO Holdings (portfolio_id, symbol, quantity, avg_buy_price)
                VALUES (1, 'AAPL', 10, 150.00);
INSERT INTO PortfolioSnaps (portfolio_id, cash_value, invested_value)
                VALUES (1, 10000.00, 1500.00);
INSERT INTO Transactions (portfolio_id, symbol, type, quantity, price_per_unit, fee, notes)
                VALUES (1, 'AAPL', 'sell', 1, 150.00, 5.00, 'Initial purchase of Apple stock');

DELIMITER $$

DROP PROCEDURE IF EXISTS InsertDailySnaps$$
CREATE PROCEDURE InsertDailySnaps()
BEGIN
    DECLARE i INT DEFAULT 0;
    DECLARE snap_date DATE;
    
    SET snap_date = DATE_SUB('2025-08-08', INTERVAL 364 DAY); -- Start date = 1 year before 08-08-2025

    WHILE i < 365 DO
        INSERT INTO PortfolioSnaps (portfolio_id, snapshot_date, cash_value, invested_value)
        VALUES (
            1,
            snap_date,
            ROUND(8000 + RAND() * 4000, 2),     -- cash_value between 8000 and 12000
            ROUND(1000 + RAND() * 7000, 2)      -- invested_value between 1000 and 8000
        );

        SET snap_date = DATE_ADD(snap_date, INTERVAL 1 DAY);
        SET i = i + 1;
    END WHILE;
END$$

DELIMITER ;

-- Call the procedure
CALL InsertDailySnaps();
