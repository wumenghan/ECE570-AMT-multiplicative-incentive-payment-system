create table
WORKER(
	id integer primary key autoincrement,
	worker_id text
);


create table 
RESULT(
	id integer primary key autoincrement,
	task_type text,
	results text,
	time_spent datetime
);
