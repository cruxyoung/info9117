drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  title text not null,
  text text not null
);

drop table if exists user;
create table user (
  user_id integer primary key autoincrement,
  username text not null,
  
  passwd text not null
);

insert into user values (999, 'yang', 'yang');
insert into user values (1000, '123', '123');
insert into user values (1562, '111', '111');

