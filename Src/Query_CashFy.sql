CREATE DATABASE IF NOT EXISTS cashfy_db;
USE cashfy_db;

-- Estrutura das Tabelas
CREATE TABLE IF NOT EXISTS USUARIO (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    senha VARCHAR(255),
    data_criacao DATE
);

CREATE TABLE IF NOT EXISTS CATEGORIA (
    id_categoria INT PRIMARY KEY,
    nome VARCHAR(50),
    tipo VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS RECEITA (
    id_receita INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(100),
    valor DECIMAL(10,2),
    data_recebimento DATE,
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES USUARIO(id_usuario)
);

CREATE TABLE IF NOT EXISTS DESPESA (
    id_despesa INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(100),
    valor DECIMAL(10,2),
    data_gasto DATE,
    id_categoria INT,
    id_usuario INT,
    FOREIGN KEY (id_categoria) REFERENCES CATEGORIA(id_categoria),
    FOREIGN KEY (id_usuario) REFERENCES USUARIO(id_usuario)
);

CREATE TABLE IF NOT EXISTS META_FINANCEIRA (
    id_meta INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(100),
    valor_meta DECIMAL(10,2),
    valor_atual DECIMAL(10,2),
    data_limite DATE,
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES USUARIO(id_usuario)
);

-- Popular Dados Iniciais Necessários
INSERT IGNORE INTO CATEGORIA (id_categoria, nome, tipo) VALUES 
(1, 'Essencial', 'fixa'), 
(2, 'Educação', 'variavel'), 
(3, 'Lazer', 'variavel'), 
(4, 'Dívida', 'variavel');

-- Limpar dados antigos para evitar duplicidade
SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE META_FINANCEIRA;
TRUNCATE TABLE DESPESA;
TRUNCATE TABLE RECEITA;
TRUNCATE TABLE USUARIO;
SET FOREIGN_KEY_CHECKS = 1;

-- Limpar dados antigos para evitar duplicidade
SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE META_FINANCEIRA;
TRUNCATE TABLE DESPESA;
TRUNCATE TABLE RECEITA;
TRUNCATE TABLE USUARIO;
SET FOREIGN_KEY_CHECKS = 1;

-- Limpar dados antigos para evitar duplicidade
SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE META_FINANCEIRA;
TRUNCATE TABLE DESPESA;
TRUNCATE TABLE RECEITA;
TRUNCATE TABLE USUARIO;
SET FOREIGN_KEY_CHECKS = 1;

-- Criar os 3 Perfis Oficiais
INSERT INTO USUARIO (id_usuario, nome, email, senha, data_criacao) VALUES 
(1, 'Caio Estagiário', 'caio@email.com', '123', '2026-05-10'),
(2, 'Pedro Inadimplente', 'pedro@email.com', '123', '2026-05-10'),
(3, 'Rafael Desorganizado', 'rafael@email.com', '123', '2026-05-10');