CREATE DATABASE squid;
USE squid;

CREATE TABLE access (
	id INT NOT NULL AUTO_INCREMENT,
	uid VARCHAR(32),
	time FLOAT,
	timeh VARCHAR(26),
	elapse FLOAT,
	remotehost VARCHAR(16),
	code VARCHAR(12),
	bytes INT,
	method VARCHAR(12),
	url VARCHAR(2083),
	rfc931 VARCHAR(12),
	hierarchy_peerhost VARCHAR(32),
	type VARCHAR(12),
	PRIMARY KEY (id)
);
