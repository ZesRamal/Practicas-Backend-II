-- Migrations will appear here as you chat with AI

create table sensor1_data (
  id bigint primary key generated always as identity,
  "timestamp" timestamptz not null default now(),
  value numeric not null
);

create table sensor2_data (
  id bigint primary key generated always as identity,
  "timestamp" timestamptz not null default now(),
  value numeric not null
);

create table sensor3_data (
  id bigint primary key generated always as identity,
  "timestamp" timestamptz not null default now(),
  value numeric not null
);

create table sensor4_data (
  id bigint primary key generated always as identity,
  "timestamp" timestamptz not null default now(),
  value numeric not null
);

create table users (
  id bigint primary key generated always as identity,
  name text not null,
  email text unique not null
);

alter table sensor1_data
add column user_id bigint;

alter table sensor2_data
add column user_id bigint;

alter table sensor3_data
add column user_id bigint;

alter table sensor4_data
add column user_id bigint;

alter table sensor1_data
add constraint fk_user1 foreign key (user_id) references users (id);

alter table sensor2_data
add constraint fk_user2 foreign key (user_id) references users (id);

alter table sensor3_data
add constraint fk_user3 foreign key (user_id) references users (id);

alter table sensor4_data
add constraint fk_user4 foreign key (user_id) references users (id);

alter table sensor1_data
add column condition text default 'temperatura';

alter table sensor2_data
add column condition text default 'humedad';

alter table sensor3_data
add column condition text default 'luminosidad';

alter table sensor4_data
add column condition text default 'nivel de nutrientes';

alter table sensor1_data
rename to temperatura_data;

alter table sensor2_data
rename to humedad_data;

alter table sensor3_data
rename to luminosidad_data;

alter table sensor4_data
rename to nutrientes_data;

alter table temperatura_data
drop constraint fk_user1;

alter table humedad_data
drop constraint fk_user2;

alter table luminosidad_data
drop constraint fk_user3;

alter table nutrientes_data
drop constraint fk_user4;

alter table temperatura_data
drop user_id;

alter table humedad_data
drop user_id;

alter table luminosidad_data
drop user_id;

alter table nutrientes_data
drop user_id;

drop table users;

create table torre (
  id bigint primary key generated always as identity,
  location text not null
);

alter table temperatura_data
add column torre_id bigint;

alter table humedad_data
add column torre_id bigint;

alter table luminosidad_data
add column torre_id bigint;

alter table nutrientes_data
add column torre_id bigint;

alter table temperatura_data
add constraint fk_torre1 foreign key (torre_id) references torre (id);

alter table humedad_data
add constraint fk_torre2 foreign key (torre_id) references torre (id);

alter table luminosidad_data
add constraint fk_torre3 foreign key (torre_id) references torre (id);

alter table nutrientes_data
add constraint fk_torre4 foreign key (torre_id) references torre (id);

create table usuario (
  id bigint primary key generated always as identity,
  nombre text not null,
  email text unique not null,
  torre_id bigint,
  constraint fk_torre_usuario foreign key (torre_id) references torre (id)
);