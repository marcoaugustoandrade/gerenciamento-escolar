create table professores_backup(
id    int          not null,
nome  varchar(200) not null,
email varchar(200) not null,
senha varchar(200) not null
);

create trigger tg_professores_backup
before delete
on professores for each row
insert into professores_backup(id, nome, email, senha) values (OLD.id, OLD.nome, OLD.email, OLD.senha);