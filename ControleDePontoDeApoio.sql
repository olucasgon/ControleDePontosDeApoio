CREATE DATABASE `controlepontoapoio`;

create table PontoApoio (
    id int auto_increment primary key,
    nome varchar(100) not null unique,
    latitude decimal(9,6) not null,
    longitude decimal(9,6) not null,
    capacidade int not null
);

create table Pessoa (
    id int auto_increment primary key,
    nome varchar(100) not null,
    cpf varchar(14) not null unique,
    telefone varchar(20),
    pontoapoio_id int,
    foreign key (pontoapoio_id) references PontoApoio(id)
);

create table Recurso (
    id int auto_increment primary key,
    nome varchar(50) not null,
    quantidade int not null,
    pontoapoio_id int not null,
    foreign key (pontoapoio_id) references PontoApoio(id)
);

create table Responsavel (
    id int auto_increment primary key,
    codigo varchar(25) not null unique,
    pessoa_id int not null,
    pontoapoio_id int not null,
    foreign key (pontoapoio_id) references PontoApoio(id),
    foreign key (pessoa_id) references Pessoa(id)
);

create table RegistroEntrada (
    id int auto_increment primary key,
    pessoa_id int not null,
    pontoapoio_id int not null,
    entrada datetime not null,
    saida datetime,
    foreign key (pessoa_id) references Pessoa(id),
    foreign key (pontoapoio_id) references PontoApoio(id)
);

