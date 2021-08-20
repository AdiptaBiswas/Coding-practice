'''
* Problem: Weather Observation Station 7
* Platform: HackerRank
* Statement: 
  Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION.
  Your result cannot contain duplicates.
* RDB: MySQL
'''

SELECT DISTINCT CITY FROM STATION WHERE RIGHT(CITY,1) IN ('a','i','e','o','u');
