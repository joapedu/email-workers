# Email Workers

## Project for sending emails with workers 🐳

<p float="left">
 <img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white">
 <img src="https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white">
 <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white">
 <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen">
 <img src="https://img.shields.io/badge/redis-%23DD0031.svg?&style=for-the-badge&logo=redis&logoColor=white">
</p>

## Ideia: 💡
Criar um projeto capaz de **simular filas** para envios de emails e fazer isso de forma **escalável utilizando docker**.

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
Os scripts abaixo executam a compilação do projeto:
  ```sh
   docker-compose up --scale worker=3
   ```
   ###### Comando para executar o gerenciamento de containers com **docker compose**.

---
## Links: 🌐
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
Este projeto está licenciado sob a licença [MIT] - consulte o arquivo LICENSE.md para obter detalhes.

## Contribuição 
 Para toda e qualquer contribuição de código vide [CONTRIBUTING.md](https://github.com/joapedu/email-workers/blob/v0.1.1/CONTRIBUTING.md).

<br>
 <h3 align="center"> 👾 <a href="https://github.com/joapedu"><strong>@joapedu</strong></a> <br />João Eduardo Braga</h3>
<h4 align="center">:phone: <i>C O N T A T O S</i> :phone:</h4>
<div align="center">
    <a href = "mailto:joaoeduardobraga2@gmail.com"><img src="https://img.shields.io/badge/-Gmail-F80000?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
    <a href="https://www.linkedin.com/in/joão-eduardo-braga/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>
    <a href="https://wa.me/5584981480327/" target="_blank"><img src="https://img.shields.io/badge/-WhatsApp-4EA94B?style=for-the-badge&logo=WhatsApp&logoColor=white" target="_blank"></a>
</div>