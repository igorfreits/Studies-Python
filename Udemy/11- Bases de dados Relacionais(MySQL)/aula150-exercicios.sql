-- Active: 1659878189229@@127.0.0.1@3306@base_de_dados
-- 1) Insira 5 usuários
INSERT into users
(first_name, last_name, email, password_hash) VALUES
('Marcos','Marc','mark|@gmail.com','qwertyuiop'),
('João','Silva','john@email.com','@gmail.com'),
('José','Dado','ze@gmail.com','ze@gmail.com'),
('Vladimir','EspañÇar', 'EspañÇar@gmail.com','vlad'),
('Giovanni','Richeli', 'Richeli@gmail.com', 'richeli');

update users set salary = round(rand() * 10000, 2) where id in
(323,322,321,321,319);
-- 2) Insira 5 perfís para os usuários inseridos
insert into profiles (bio,description,user_id) values
('Uma bio','Uma Description',(select id from users where email = 'Richeli@gmail.com')),
('Uma bio','Uma Description',(select id from users where email = 'EspañÇar@gmail.com')),
('Uma bio','Uma Description',(select id from users where email = 'ze@gmail.com')),
('Uma bio','Uma Description',(select id from users where email = 'john@email.com')),
('Uma bio','Uma Description',(select id from users where email = 'mark|@gmail.com'));
-- 3) Insira permissões (roles) para os usuários inseridos
insert into user_roles(user_id, role_id) values
(
    (select id from users where email = 'Richeli@gmail.com'),
    (select id from roles where name = 'PUT')
),
(
    (select id from users where email = 'Espar@gmail.com'),
    (select id from roles where name = 'POST')
),
(
    (select id from users where email = 'ze@gmail.com'),
    (select id from roles where name = 'GET')
),
(
    (select id from users where email = 'john@email.com'),
    (select id from roles where name = 'DELETE')
),
(
    (select id from users where email = 'mark|@gmail.com'),
    (select id from roles where name = 'SECRETARY')
),
(
    (select id from users where email = 'Richeli@gmail.com'),
    (select id from roles where name = 'DELETE')
),
(
    (select id from users where email = 'mark|@gmail.com'),
    (select id from roles where name = 'PUT')
);
-- 4) Selecione os últimos 5 usuários por ordem decrescente
select * from users
ORDER BY id desc
limit 5;
-- 5) Atualize o último usuário inserido
update users set first_name = 'Giovanni Richeli', last_name = 'Atualizada'
where id = 323;
-- 6) Remova uma permissão de algum usuário
DELETE from user_roles where
user_id = (SELECT id from users where email = 'Richeli@gmail.com')
and role_id = (SELECT id from roles where name = 'DELETE');
-- 7) Remova um usuário que tem a permissão "PUT"
--select u.id as uid, u.first_name, r.name
delete u 
from users u
inner join user_roles ur on u.id = ur.user_id
inner join roles r on ur.role_id = r.id
where r.name = 'PUT' and u.id = 319;
-- 8) Selecione usuários com perfís e permissões (obrigatório)
select u.id as uid, u.first_name, r.name
from users u
inner join user_roles ur on u.id = ur.user_id
inner join roles r on ur.role_id = r.id
inner join profiles p on p.user_id = u.id;
-- 9) Selecione usuários com perfís e permissões (opcional)
select u.id as uid, u.first_name, r.name,p.bio
from users u
left join user_roles ur on u.id = ur.user_id
left join roles r on ur.role_id = r.id
left join profiles p on p.user_id = u.id;
-- 10) Selecione usuários com perfís e permissões ordenando por salário
select u.id as uid, u.first_name, r.name , u.salary
from users u
left join user_roles ur on u.id = ur.user_id
left join roles r on ur.role_id = r.id
left join profiles p on p.user_id = u.id
ORDER BY u.salary desc;

