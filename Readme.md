# Email Workers

## Project for sending emails with workers


-------------------------------------------------


# Email Worker Compose 🐳
## Projeto elaborado no curso ***DOCKER - COD3R***

<br>
<p float="left">
 <img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white">
 <img src="https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white">
 <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white">
 <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen">
 <img src="https://img.shields.io/badge/redis-%23DD0031.svg?&style=for-the-badge&logo=redis&logoColor=white">
</p>
<br>

## Ideia: 💡
Criar um projeto capaz de **simular filas** para envios de emails e fazer isso de forma **escalável utilizando docker**

## Funcionalidades:
- Gerenciamento de containers utilizando ***docker compose***;
- Execução escalável;
- Enfileramento utilizando ***REDIS***;
- Simulação de envio utilizando ***Python***.

## Executando o projeto: 🚀
Para executar e visualizar o projeto em **modo de desenvolvimento**, você precisará seguir as próximas etapas.

### Pré-requisitos:
Abaixo estará listada as ferramentas necessárias para o funcionamento do projeto.
- **Docker** 🐳<br>
  [Guia de instalação docker](https://docs.docker.com/get-docker/).
- **Docker Compose** 🐳<br>
  [Guia de instalação docker compose](https://docs.docker.com/compose/install/).
  
### Executando o projeto:
Os scripts abaixo executam a compilação do projeto.
  ```sh
   docker-compose up --scale worker=3
   ```
   ###### Comando para executar o gerenciamento de containers com **docker compose**

---
## Links: 🌐
***Curso Cod3er:***<br>
[<ins>Docker: Ferramenta essencial para Desenvolvedores</ins>](https://www.cod3r.com.br/courses/docker)

***Imagens utilizadas:***<br>
[<ins>Redis image</ins>](https://hub.docker.com/_/redis) 
<br>
[<ins>Python image</ins>](https://hub.docker.com/_/python) 
<br>
[<ins>Nignx image</ins>](https://hub.docker.com/_/nginx)
<br>
[<ins>Postgres image</ins>](https://hub.docker.com/_/postgres)

---
## Licença
Este projeto está licenciado sob a licença [MIT] - consulte o arquivo LICENSE.md para obter detalhes