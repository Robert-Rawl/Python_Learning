SELECT * 
FROM countries;

SELECT countries.name AS Country_Name, languages.language AS Language, languages.percentage AS Percent_Spoken
FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.language = 'Slovene'
ORDER BY languages.percentage DESC;

SELECT countries.name AS Country_Name,  COUNT(cities.name) AS Total_Num_Cities
FROM countries
LEFT JOIN cities ON countries.id = cities.country_id
GROUP BY countries.name
ORDER BY Total_Num_Cities DESC;

SELECT name, population, country_id
FROM cities
WHERE cities.population > 500000
AND cities.country_id = (SELECT id FROM countries WHERE countries.name = 'Mexico')
ORDER BY population DESC;

SELECT countries.name AS Name, languages.language AS Language, languages.percentage AS Percentage
FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.percentage > 89
ORDER BY languages.percentage DESC;

SELECT name, surface_area, population
FROM countries
WHERE countries.surface_area < 501
AND countries.population >100000;

SELECT name, government_form, capital, life_expectancy
FROM countries
WHERE countries.government_form = "Constitutional Monarchy"
AND countries.capital > 200
AND countries.life_expectancy > 75;

SELECT countries.name AS Country, cities.name AS City, cities.district AS District, cities.population AS Population
FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE cities.district = "Buenos Aires"
AND cities.population > 500000;

SELECT countries.region AS Region, COUNT(countries.name) AS Countries
FROM countries
GROUP BY countries.region
ORDER BY countries DESC;




