# :books:  PACC - Programa Avaliativo  de Conhecimento em Computação
<div align="center" display="flex" style="justify-content:flex-start;">
      <img align="center" alt="js" height="60" width="60" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original-wordmark.svg" />
</div>

<p align="center">
 <a href="#desc">Descrição</a> •
 <a href="#about">Objetivo</a> •
 <a href="#tecnologias">Tecnologias</a> • 
 <a href="#prerequisitos">Pré-requisitos</a> • 
 <a href="#executando">Executar o projeto</a> • 
 <a href="#autor">Autor</a>
</p>

<div id="desc"/>

## 📝 Descrição
Este projeto é uma API Restful desenvolvida utilizando o framework Spring Boot, na linguagem de programação java. <br>
O intuito de sua produção é para que fique disponível para que sejam efetuados testes de API Restful. <br>
O link de acesso ao Heroku pode ser acessado [aqui](https://api-course-test-automatized.herokuapp.com) <br>
A documentação SWAGGER da aplicação está disponível nesse [link](https://api-course-test-automatized.herokuapp.com/swagger-ui.html)

<div id="about"/>

## ⚙️ O que a API faz?
A API Restful da suporte a aplicações de postagens. <br>
Consiste em dois módulos: usuário e publicações (posts), onde um usuário cria pode criar uma ou várias publicações <br>
Para cadastrar um usuário é necessário ter: nome, email e senha como campos obrigatórios e, caso deseje, biografia, site e imagem de perfil (url)<br>
Para cadastrar uma publicação é necessário ter: titulo e texto <br>

<div id="exemplos"/>

## 📑 Exemplos
##### JSON para criação de usuário: <br>
![User](user_create.png)

##### JSON para criação de post: <br>
![Post](post_create.png)

<div id="rotas" />

## :busstop: Rotas
#### Login
- [ ] POST /auth/login
#### Usuário
- [ ] POST /api/users
- [ ] GET /api/users
- [ ] GET /api/users/details
- [ ] PUT /api/users
#### Publicações
- [ ] GET /api/posts
- [ ] GET /api/posts/id
- [ ] POST /api/posts
- [ ] PUT /api/posts/id
- [ ] DELETE /api/posts/id


<div id="tecnologias"/>

## ✨ Tecnologias

-   [ ] [Java](https://www.java.com/pt-BR/)
-   [ ] [Spring Boot](https://spring.io/)
-   [ ] [Thymeleaf](https://www.thymeleaf.org/)
-   [ ] [PostgreSQL](https://www.postgresql.org/)
-   [ ] [Project Lombok](https://projectlombok.org/)
-   [ ] [Spring Data JPA](https://spring.io/projects/spring-data-jpa)
-   [ ] [Swagger](https://swagger.io/)
-   [ ] [Json Web Token](https://jwt.io/)
-   [ ] [Hibernate](https://hibernate.org/)
-   [ ] [Model Mapper](http://modelmapper.org/)

<div id="prerequisitos"/>

## 📑 Pré requisitos

Para executar o projeto localmente, é necessário ter:
1. PostgreSQL instalado
2. Banco criado
3. Java 11
4. Arquivo `application.properties` alterado com credenciais corretas
   1. `spring.datasource.url=` nome do banco criado
   2. `spring.datasource.username=` usuário do administrador do banco de dados
   3. `spring.datasource.password=` senha do administrador
  
<div id="executando" />

## ▶️ Executando o projeto

Para acessar a API Restful remotamente, basta clicar [aqui](https://api-course-test-automatized.herokuapp.com) <br>
> NOTE: Normalmente, a aplicação demora uns minutos para inciar

Para executar localmente, siga os passos:
```sh
$ git clone https://github.com/MarcosLudgerio/api-automation-test.git
$ cd api-automation-test
$ ./mvnw install
$ ./mvnw spring-boot:run
```

<div id="autor" />

## 👩‍💻 Autor 

<table>
   <tr>
     <td align="center">
        <a href="https://github.com/MarcosLudgerio">
         <img style="border-radius: 50%;" src="https://avatars0.githubusercontent.com/u/43012976?s=460&u=1163c04d9f35b577063b3f6550ae520c4dd2f866&v=4" width="100px;" alt=""/>
        </a>
        <br/><sub><b>Marcos Ludgério</b></sub>
     </td>
   </tr>
</table>
