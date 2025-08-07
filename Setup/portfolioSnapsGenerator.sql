DELIMITER $$

DROP PROCEDURE IF EXISTS InsertDailySnaps$$
CREATE PROCEDURE InsertDailySnaps()
BEGIN
    DECLARE i INT DEFAULT 0;
    DECLARE snap_date DATE;
    DECLARE last_cash_value DECIMAL(12,2) DEFAULT 4500.00;     -- Start with same as invested_value
    DECLARE last_invested_value DECIMAL(12,2) DEFAULT 4500.00; -- Start value
    DECLARE new_cash_value DECIMAL(12,2);
    DECLARE new_invested_value DECIMAL(12,2);
    DECLARE day_of_week INT;

    SET snap_date = DATE_SUB('2025-08-08', INTERVAL 364 DAY); -- Start date = 1 year before 08-08-2025

    WHILE i < 365 DO
        SET day_of_week = DAYOFWEEK(snap_date); -- 1=Sunday, 7=Saturday

        IF day_of_week IN (1,7) THEN
            -- Weekend: values don't change
            SET new_cash_value = last_cash_value;
            SET new_invested_value = last_invested_value;
        ELSE
            -- Weekday: Small random walk for both values
            SET new_invested_value = last_invested_value + ROUND((RAND() - 0.3) * 400, 2);
            SET new_cash_value = last_cash_value + new_invested_value - last_invested_value + ROUND((RAND() - 0.4) * 1000, 2);
        END IF;

        INSERT INTO PortfolioSnaps (portfolio_id, snapshot_date, cash_value, invested_value)
        VALUES (
            1,
            snap_date,
            new_cash_value,
            new_invested_value
        );

        -- Update last values for next day
        SET last_cash_value = new_cash_value;
        SET last_invested_value = new_invested_value;

        SET snap_date = DATE_ADD(snap_date, INTERVAL 1 DAY);
        SET i = i + 1;
    END WHILE;
END$$

DELIMITER ;

-- Call the procedure
CALL InsertDailySnaps();