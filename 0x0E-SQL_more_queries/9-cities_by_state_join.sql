-- a script that lists all cities contained in the database hbtn_0d_usa.
SELECT cities.id, cities.name, state.name FROM cities INNER JOIN states ON state_id = states.id ORDER BY cities.id;
