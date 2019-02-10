
CREATE DATABASE downloadmanager;

USE downloadmanager;

CREATE TABLE downloaded (
id INT AUTO_INCREMENT, 
filename VARCHAR(1000), 
url VARCHAR(1000), 
kind VARCHAR(50),
typefile VARCHAR(50),
state VARCHAR(50), PRIMARY KEY (id));


