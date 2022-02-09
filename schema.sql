create table employee_table(
employee_id serial primary key,
manager bool not null default(false),
first_name varchar(20) not null,
last_name varchar(20) not null,
login varchar(40) not null,
passcode varchar(20) not null
);


create table reimbursement_table(
reimbursement_id serial primary key,
employee_id int references employee_table(employee_id) on delete cascade,
reimbursement_date timestamp not null default clock_timestamp(),
amount decimal not null,
reason varchar(280) not null,
approval varchar(20) not null default('pending'),
manager_comment varchar(280) not null
);


create table manager_junction_table(
employee_id int references employee_table(employee_id) on delete cascade,
manager_id int references employee_table(employee_id) on delete cascade,
primary key (employee_id, manager_id),
check(employee_id != manager_id)
);