/*
a) When I open up actor and then expand columns, the actor id, first name, last name and last update populate
b) When I open up film and expand columns, I get film id, title, description, release year, language id, original language, rental duration, rental rate, length, replacement cost, rating, special features, last update
c) Under film_actor, there is also actor id and film id. Film category also had film id. Film text has film id too. Inveentory also had film id. 
d) The numbers are hard to read. However, the fields that are there are: rental date, inventory ID, customer ID, return date, staff ID, and last update
e) The inventory includes: inventory ID, film ID, store ID, and last update
f) In order to understand the name of films rented on specific dates, you would need to go to the tables: inventory table and see film ID, then go to rental table and see rental date because it has inventory ID. They connect from rental bc it has inventory from film ID to rental which has the inventory ID as well 
*/

SELECT inventory_id, rental_date FROM rental;
SELECT inventory_id, film_id FROM inventory;
SELECT film_id, title FROM film
