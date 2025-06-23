CREATE DATABASE controlepontoapoio;

CREATE TABLE "PontoApoio" (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL UNIQUE,
    latitude DECIMAL(9,6) NOT NULL,
    longitude DECIMAL(9,6) NOT NULL,
    capacidade INT NOT NULL
);

CREATE TABLE "Pessoa" (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) NOT NULL UNIQUE,
    telefone VARCHAR(20),
    pontoapoio_id INT,
    CONSTRAINT "Pessoa_PontoApoio_fk" FOREIGN KEY (pontoapoio_id) REFERENCES "PontoApoio"(id)
);

CREATE TABLE "Recurso" (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    quantidade INT NOT NULL,
    pontoapoio_id INT NOT NULL,
    CONSTRAINT "Recurso_PontoApoio_fk" FOREIGN KEY (pontoapoio_id) REFERENCES "PontoApoio"(id)
);

CREATE TABLE "Responsavel" (
    id SERIAL PRIMARY KEY,
    codigo VARCHAR(25) NOT NULL UNIQUE,
    pessoa_id INT NOT NULL,
    pontoapoio_id INT NOT NULL,
    CONSTRAINT "Responsavel_PontoApoio_fk" FOREIGN KEY (pontoapoio_id) REFERENCES "PontoApoio"(id),
    CONSTRAINT "Responsavel_Pessoa_fk" FOREIGN KEY (pessoa_id) REFERENCES "Pessoa"(id)
);

CREATE TABLE "RegistroEntrada" (
    id SERIAL PRIMARY KEY,
    pessoa_id INT NOT NULL,
    pontoapoio_id INT NOT NULL,
    entrada TIMESTAMP NOT NULL,
    saida TIMESTAMP,
    CONSTRAINT "RegistroEntrada_Pessoa_fk" FOREIGN KEY (pessoa_id) REFERENCES "Pessoa"(id),
    CONSTRAINT "RegistroEntrada_PontoApoio_fk" FOREIGN KEY (pontoapoio_id) REFERENCES "PontoApoio"(id)
);
