-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Check all fields where crime_scene_reports is 'Humphrey Street'
SELECT * FROM crime_scene_reports WHERE street = 'Humphrey Street';
-- 295|2023|7|28|Humphrey Street|Theft of the CS50 duck took place at
-- 10:15am at the Humphrey Street bakery. Interviews were conducted today
-- with three witnesses who were present at the time – each of their
-- interview transcripts mentions the bakery.



-- Check interviews for date of crime
SELECT * FROM interviews WHERE day = 28 AND month = 7;
-- 161|Ruth|2023|7|28|Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.
-- 162|Eugene|2023|7|28|I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.
-- 163|Raymond|2023|7|28|As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket.



-- Finding the details for Ruth, Eugene, Raymond
SELECT * FROM people WHERE name = 'Ruth';
-- 430845|Ruth|(772) 555-5770||HZB4129
SELECT * FROM people WHERE name = 'Eugene';
-- 280744|Eugene|(666) 555-5774|9584465633|47592FJ
SELECT * FROM people WHERE name = 'Raymond';
-- 937274|Raymond|(125) 555-8030||Y18DLY3



-- Finding the ATM transactions on Leggett Street
SELECT * FROM atm_transactions WHERE atm_location = 'Leggett Street' AND day = 28;
-- 246|28500762|2023|7|28|Leggett Street|withdraw|48
-- 264|28296815|2023|7|28|Leggett Street|withdraw|20
-- 266|76054385|2023|7|28|Leggett Street|withdraw|60
-- 267|49610011|2023|7|28|Leggett Street|withdraw|50
-- 269|16153065|2023|7|28|Leggett Street|withdraw|80
-- 288|25506511|2023|7|28|Leggett Street|withdraw|20
-- 313|81061156|2023|7|28|Leggett Street|withdraw|30
-- 336|26013199|2023|7|28|Leggett Street|withdraw|35



-- Finding the license plate logged
SELECT * FROM bakery_security_logs WHERE day = 28 AND month = 7 AND year = 2023 AND hour = 10;
-- 260|2023|7|28|10|16|exit|5P2BI95
-- 261|2023|7|28|10|18|exit|94KL13X
-- 262|2023|7|28|10|18|exit|6P58WS2
-- 263|2023|7|28|10|19|exit|4328GD8
-- 264|2023|7|28|10|20|exit|G412CB7
-- 265|2023|7|28|10|21|exit|L93JTIZ
-- 266|2023|7|28|10|23|exit|322W7JE
-- 267|2023|7|28|10|23|exit|0NTHK55
-- 268|2023|7|28|10|35|exit|1106N58



-- Matching plates with people
SELECT * FROM people WHERE license_plate = '5P2BI95';
-- 221103|Vanessa|(725) 555-4692|2963008352|5P2BI95
SELECT * FROM people WHERE license_plate = '94KL13X';
-- 686048|Bruce|(367) 555-5533|5773159633|94KL13X
SELECT * FROM people WHERE license_plate = '6P58WS2';
-- 243696|Barry|(301) 555-4174|7526138472|6P58WS2
SELECT * FROM people WHERE license_plate = '4328GD8';
-- 467400|Luca|(389) 555-5198|8496433585|4328GD8
SELECT * FROM people WHERE license_plate = 'G412CB7';
-- 398010|Sofia|(130) 555-0289|1695452385|G412CB7
SELECT * FROM people WHERE license_plate = 'L93JTIZ';
-- 396669|Iman|(829) 555-5269|7049073643|L93JTIZ
SELECT * FROM people WHERE license_plate = '322W7JE';
-- 514354|Diana|(770) 555-1861|3592750733|322W7JE
SELECT * FROM people WHERE license_plate = '0NTHK55';
-- 560886|Kelsey|(499) 555-9472|8294398571|0NTHK55
SELECT * FROM people WHERE license_plate = '1106N58';
-- 449774|Taylor|(286) 555-6063|1988161715|1106N58



-- Check calls caller and receiver for each person that is logged by reg for that date calls 60 and less than seconds
-- caller
SELECT * FROM phone_calls WHERE caller IN ('(725) 555-4692', '(367) 555-5533', '(301) 555-4174', '(389) 555-5198', '(130) 555-0289', '(829) 555-5269', '(770) 555-1861', '(499) 555-9472', '(286) 555-6063') AND day = 28 AND month = 7 AND duration <= 60;
221|(130) 555-0289|(996) 555-8899|2023|7|28|51
224|(499) 555-9472|(892) 555-8872|2023|7|28|36
233|(367) 555-5533|(375) 555-8161|2023|7|28|45
251|(499) 555-9472|(717) 555-1342|2023|7|28|50
254|(286) 555-6063|(676) 555-6554|2023|7|28|43
255|(770) 555-1861|(725) 555-3243|2023|7|28|49

-- receiver
SELECT * FROM phone_calls WHERE receiver IN ('(725) 555-4692', '(367) 555-5533', '(301) 555-4174', '(389) 555-5198', '(130) 555-0289', '(829) 555-5269', '(770) 555-1861', '(499) 555-9472', '(286) 555-6063') AND day = 28 AND month = 7 AND duration <= 60;
234|(609) 555-5876|(389) 555-5198|2023|7|28|60



-- Checking flights outside of fiftyville airport id 8 for the day 29th
SELECT * FROM flights WHERE origin_airport_id = 8 AND day = 29;
18|8|6|2023|7|29|16|0
23|8|11|2023|7|29|12|15
36|8|4|2023|7|29|8|20   -------------------- earliest   landed new york city id 4
43|8|1|2023|7|29|9|30
53|8|9|2023|7|29|15|20


-- Checking passengers by passport for that specific flight by matching passport ids to the bakery logs of people
SELECT * FROM passengers WHERE flight_id = 36;
36|1695452385|3B
36|5773159633|4A
36|8294398571|6C
36|1988161715|6D
36|8496433585|7B


-- SUSPECT COULD BE THE FOLLOWING
-- 398010|Sofia|(130) 555-0289|1695452385|G412CB7
-- 686048|Bruce|(367) 555-5533|5773159633|94KL13X       ---------------- selected
-- 560886|Kelsey|(499) 555-9472|8294398571|0NTHK55
-- 449774|Taylor|(286) 555-6063|1988161715|1106N58
-- 467400|Luca|(389) 555-5198|8496433585|4328GD8
