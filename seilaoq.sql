/* Inserindo informações na tabela autor */
insert into Autor(nome, data_de_nascimento)
values(1,'Eva Heller', '1948-08-08'), /*psicologia das cores*/
(2, 'Andrew Stuart Tanenbaum', '1944-03-16'),/* Sistemas Operativos Modernos*/
(3, 'Charles Duhigg', '1974'), /*o poder do hábito*/
(4, 'Stephen Hawking', '1942-01-08'), /*uma breve história do tempo*/
(5, 'Karl Marx', '1818-05-05'); /* O capital*/

/* Inserindo informações na tabela livro*/
insert into Livro(ISBN, editora, numero_da_edicao, titulo, classificacao_por_assunto)
values('978-3-17-418129-1', 'Pearson' , 4, 'Sistemas Operativos Modernos', 'tecnologia');
/* Inseridos sem a edição*/
insert into Livro(ISBN, editora, titulo, classificacao_por_assunto)
values(518-6-16-148750-0, 'olhares', 'Psicologia das cores', 'designer' ),
(759-3-15-475129-1, 'objetiva', 'O poder do hábito', 'psicologia'),
(083-3-93-473459-0, 'intrinsace', 'Uma Breve História do Tempo', 'física'),
(453-4-23-203453-0, 'Veneta', 'O capital','sociologia' );

/* Inserindo informações na tabela Exemplar*/
insert into Livro(cod_exemplar, quantidade, ISBN_livro)
values(02946, 20, 518-6-16-148750-0), /*Psicologia das cores*/
(01298, 10, 978-3-17-418129-1),/*Sistemas Operativos Modernos*/
(68460, 40, 759-3-15-475129-1),/*O poder do hábito*/
(47420, 21, 083-3-93-473459-0), /*Uma breve história do tempo*/ 
(07213, 13, 453-4-23-203453-0);/*O capital*/

/* Inserindo informações na tabela Escrito_por*/
insert into Escrito_por(cod_autor, ISBN_livro)
values(1, 02946), /*Psicologia das cores*/
(2, 01298),/*Sistemas Operativos Modernos*/
(3, 68460),/*O poder do hábito*/
(4, 47420), /*Uma breve história do tempo*/ 
(5, 07213);/*O capital*/

/* Inserindo informações na tabela Usuario */
insert into Usuario(matricula, nome, data_de_nascimento, rua, UF, CEP, cidade, bairro, numero, foto, data_de_validade, qr_code)
values(20221370059, 'Vanessa Silva', 2000-09-31, 'Avenida Coremas','PB', 58013-430, 'João Pessoa','Centro',561 , load_file('imagem.png'), 2024-12-31, load_file('imagem.png')),
(20221370086, 'Rita Clara', 2001-11-0, 'Rua Comerciário Antônio Manoel de Sousa','PB', 58071-585, 'João Pessoa','Cristo Redentor',20 , load_file('imagem.png'), 2022-12-31, load_file('imagem.png')),
(20221370077, 'Laís Epifanio Machado', 2002-10-10, 'Rua Osvaldo Travassos Campos','PB', 58080-540, 'João Pessoa','Ernani Sátiro',16 , load_file('imagem.png'), 2023-12-31, load_file('imagem.png')),
(20221370029, 'Cleiton Bernadino', 2001-11-08, 'Conjunto Jacinto Medeiros','PB', 58026-080, 'João Pessoa','Treze de Maio',120 , load_file('imagem.png'), 2022-12-31, load_file('imagem.png')),
(20221370002, 'Raimundo de Moraes', 2004-03-23, 'Rua Guadalupe','PB', 58079-806, 'João Pessoa','Grotão', 777, load_file('imagem.png'), 2024-12-31, load_file('imagem.png'));

/*Inserindo informações na tabela email*/
insert into Email(email, matricula_usuario)
values('Silva.Vanessa@academico.ifpb.edu.br', 20221370059),
('Silva.Rita@academico.ifpb.edu.br', 20221370086),
('Lais.Machado@academico.ifpb.edu.br', 20221370077),
('Cleiton.Bernadito@academico.ifpb.edu.br', 20221370029),
('Mores.Santos@academico.ifpb.edu.br', 20221370002);

/* Inserindo informações na tabela telefone*/
insert into Telefone(telefone, matricula_usuario)
values(98854-1234, 20221370059),
(94002-8922, 20221370086),
(92034-9933, 20221370077),
(91234-5678, 20221370029),
(98765-4321, 20221370002);

/*Inserindo informações na tabela empréstimo*/
insert into Empréstimo(matricula_usuario, cpf_funcionario, cod_exemplar,data_de_emprestimo, data_de_devolucao)
value(20221370059, 111111111-11 ,02946, 2022-11-20, 2022-12-20), /* Vanessa fez um empréstimo livro "Psicologia das cores"*/
(20221370086, 111111111-11 ,02946, 2022-11-30, 2022-12-30), /* Rita fez um empréstimo livro "Psicologia das cores"*/
(20221370077, 111111111-11 ,47420, 2022-11-06, 2022-12-06), /* Laís fez um empréstimo livro "Uma breve história do tempo"*/
(20221370029, 111111111-11 ,07213, 2022-11-20, 2022-12-20), /* Cleiton fez um empréstimo livro "O capital"*/
(20221370002, 111111111-11 ,01298, 2022-11-28, 2022-12-28); /* Raimundo fez um empréstimo livro "Sistemas Operativos Modernos"*/

insert into Funcionário(cpf, nome, telefone, data_de_nascimento, rua, uf, cep,
 cidade, bairro,numero, cpf_responsavel_cadastro, login, senha)
value(102748293-51,'Caetano Veloso', 98867-1235, 1975-10-05, 'Avenida Coremas','PB', 58013-430, 'João Pessoa','Centro',565 , 156248293-61, 'CaetanoV', 'whereareyounow123'),
(156248293-61,'Alcione', 99357-1251, 1955-11-13, 'Rua Guadalupe','PB', 58079-806, 'João Pessoa','Grotão', 777, 129248629-65, 20221370008,'Alcione', 'Youmetiradosério33'),
(129248629-65,'Renata Costa', 98887-1235, 1975-03-05, 'Rua Comerciário Antônio Manoel de Sousa','PB', 58071-585, 'João Pessoa','Cristo Redentor',18 , 102748293-51, 'RenataC', '1RenatasóRenata'),
(102520493-67,'Catarina Rios', 98868-3215, 1985-10-10, 'Conjunto Jacinto Medeiros','PB', 58026-080, 'João Pessoa','Treze de Maio',122 , 129248629-65, 'CatarinaR', 'RiozinhoBB56'),
(412748299-54,'Felipe Neto', 98867-1235, 1984-04-11, 'Rua Osvaldo Travassos Campos','PB', 58080-540, 'João Pessoa','Ernani Sátiro',19, 102748293-51, 'FelipeN', 'CriativonoMINEgamemod1');
/*Inserindo informações na tabela de Atendentes*/
insert into Funcionário(cpf, nome, telefone, data_de_nascimento, rua, uf, cep,
 cidade, bairro,numero, cpf_responsavel_cadastro)
 value(410258299-14, 'Clarice Laís', 96485-9274, 1990-04-18, 'Rua Luiz Moreira Gomes', 'PB', 58052-295, 'João Pessoa', 'Água Fria', 32, 102748293-51),
 (180258829-12, 'Anônio Silva', 96301-8874, 1970-05-20, 'Rua Comerciário Ademy Batista da Silva', 'PB', 58076-349, 'João Pessoa', 'Água Fria', 12, 129248629-65),
 (410258299-14, 'Luís Rodrirgues', 91185-8854, 1989-04-30, 'Avenida Presidente Epitácio Pessoa', 'PB', 58030-001, 'João Pessoa', 'Estados', 180, 102748293-51),
 (920263819-67, 'Vanessa da Mata', 96487-9874, 1970-07-18, 'Rua Rio Grande do Sul', 'PB', 58030-021, 'João Pessoa', 'Bairro dos Estados', 32, 412748299-54),
 (900254529-64, 'Ronaldo Luiz', 96485-9274, 1984-10-31, 'Rua Irineu Joffily', 'PB', 58011-110, 'João Pessoa', 'Centro', 100, 156248293-61);
 