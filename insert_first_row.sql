USE squid;

INSERT INTO access (
			time,
			elapse,
			remotehost,
			code,
			bytes,
			method,
			url,
			rfc931,
			hierarchy_peerhost,
			type
		)
	VALUES (
	1382447026.098,
    	605,
       	'127.0.0.1',
       	'TCP_MISS/200',
	1104,
	'CONNECT',
       	'bugzilla.redhat.com:443',
       	'-',
       	'HIER_DIRECT/10.4.127.4',
       	'-'
);

