-- Keep a log of any SQL queries you execute as you solve the mystery.

-- The theft took place on July 28, 2021 on Humphrey Street.


-- /* Thief */
SELECT name as 'thief' FROM people WHERE passport_number = (
    SELECT p.passport_number
    FROM passengers as p
    INNER JOIN flights as f
        ON p.flight_id = f.id
    INNER JOIN airports as a
        ON f.origin_airport_id = a.id
    /* Find passport from caller,exit time and atm */
    WHERE p.passport_number IN(SELECT passport_number
                            FROM people
                            /* phone call with some duration */
                            WHERE phone_number IN(SELECT caller
                                                    FROM phone_calls
                                                    WHERE year = 2021
                                                    AND month = 7
                                                    AND day = 28
                                                    AND duration BETWEEN 0 AND 60)
                                /* exit time from bakery */
                                AND license_plate IN(SELECT license_plate
                                                    FROM bakery_security_logs
                                                    WHERE year = 2021
                                                        AND month = 7
                                                        AND day = 28
                                                        AND (hour = 10 AND minute BETWEEN 15 AND 30
                                                            AND activity = 'exit')))
        /* atm transaction */
        AND p.passport_number IN (SELECT p.passport_number
                                FROM people as p
                                INNER JOIN bank_accounts as ba
                                    ON p.id = ba.person_id
                                WHERE ba.account_number IN(SELECT account_number
                                                            FROM atm_transactions
                                                            WHERE year = 2021
                                                            AND month = 7
                                                            AND day = 28
                                                            AND transaction_type = 'withdraw'
                                                            AND atm_location = 'Leggett Street'))
        /* flight */
        AND a.abbreviation = (SELECT abbreviation
                                FROM airports
                                WHERE city = 'Fiftyville')
        AND f.year = 2021
        AND f.month = 7
        AND f.day = 29
    ORDER BY f.hour, f.minute asc
    LIMIT 1
    );

/* Destination */
SELECT city as 'destination' FROM airports WHERE id = (
    SELECT f.destination_airport_id
    FROM passengers as p
    INNER JOIN flights as f
        ON p.flight_id = f.id
    INNER JOIN airports as a
        ON f.origin_airport_id = a.id
    /* Find passport from caller,exit time and atm */
    WHERE p.passport_number IN(SELECT passport_number
                            FROM people
                            /* phone call with some duration */
                            WHERE phone_number IN(SELECT caller
                                                    FROM phone_calls
                                                    WHERE year = 2021
                                                    AND month = 7
                                                    AND day = 28
                                                    AND duration BETWEEN 0 AND 60)
                                /* exit time from bakery */
                                AND license_plate IN(SELECT license_plate
                                                    FROM bakery_security_logs
                                                    WHERE year = 2021
                                                        AND month = 7
                                                        AND day = 28
                                                        AND (hour = 10 AND minute BETWEEN 15 AND 30
                                                            AND activity = 'exit')))
        /* atm transaction */
        AND p.passport_number IN (SELECT p.passport_number
                                FROM people as p
                                INNER JOIN bank_accounts as ba
                                    ON p.id = ba.person_id
                                WHERE ba.account_number IN(SELECT account_number
                                                            FROM atm_transactions
                                                            WHERE year = 2021
                                                            AND month = 7
                                                            AND day = 28
                                                            AND transaction_type = 'withdraw'
                                                            AND atm_location = 'Leggett Street'))
        /* flight */
        AND a.abbreviation = (SELECT abbreviation
                                FROM airports
                                WHERE city = 'Fiftyville')
        AND f.year = 2021
        AND f.month = 7
        AND f.day = 29
    ORDER BY f.hour, f.minute asc
    LIMIT 1
    );

SELECT name as 'accomplice' FROM people WHERE phone_number = (
    SELECT receiver FROM phone_calls WHERE caller = (
        SELECT phone_number FROM people WHERE passport_number = (
        SELECT p.passport_number
        FROM passengers as p
        INNER JOIN flights as f
            ON p.flight_id = f.id
        INNER JOIN airports as a
            ON f.origin_airport_id = a.id
        /* Find passport from caller,exit time and atm */
        WHERE p.passport_number IN(SELECT passport_number
                                FROM people
                                /* phone call with some duration */
                                WHERE phone_number IN(SELECT caller
                                                        FROM phone_calls
                                                        WHERE year = 2021
                                                        AND month = 7
                                                        AND day = 28
                                                        AND duration BETWEEN 0 AND 60)
                                    /* exit time from bakery */
                                    AND license_plate IN(SELECT license_plate
                                                        FROM bakery_security_logs
                                                        WHERE year = 2021
                                                            AND month = 7
                                                            AND day = 28
                                                            AND (hour = 10 AND minute BETWEEN 15 AND 30
                                                                AND activity = 'exit')))
            /* atm transaction */
            AND p.passport_number IN (SELECT p.passport_number
                                    FROM people as p
                                    INNER JOIN bank_accounts as ba
                                        ON p.id = ba.person_id
                                    WHERE ba.account_number IN(SELECT account_number
                                                                FROM atm_transactions
                                                                WHERE year = 2021
                                                                AND month = 7
                                                                AND day = 28
                                                                AND transaction_type = 'withdraw'
                                                                AND atm_location = 'Leggett Street'))
            /* flight */
            AND a.abbreviation = (SELECT abbreviation
                                    FROM airports
                                    WHERE city = 'Fiftyville')
            AND f.year = 2021
            AND f.month = 7
            AND f.day = 29
        ORDER BY f.hour, f.minute asc
        LIMIT 1)
        )
        AND year = 2021
        AND month = 7
        AND day = 28
        AND duration BETWEEN 0 AND 60
        );