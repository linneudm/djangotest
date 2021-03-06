# Django Test App
[![Requirements Status](https://requires.io/github/linneudm/djangotest/requirements.svg?branch=master)](https://requires.io/github/linneudm/djangotest/requirements/?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/63a0119f3e514bdda67a41d0e53687c6)](https://app.codacy.com/app/linneudm/djangotest?utm_source=github.com&utm_medium=referral&utm_content=linneudm/djangotest&utm_campaign=Badge_Grade_Dashboard)
[![codebeat badge](https://codebeat.co/badges/7e77d1c8-e6c2-4fb1-ac2e-c1f78fbad917)](https://codebeat.co/projects/github-com-linneudm-djangotest-master)
[![CodeFactor](https://www.codefactor.io/repository/github/linneudm/djangotest/badge)](https://www.codefactor.io/repository/github/linneudm/djangotest)

Esta é uma aplicação feita para testar os conhecimentos em Django, Django Rest Framework e Docker.

Toda a documentação está disponível no diretório "``docs``" e online no link [djangotest-piaui.readthedocs.io](https://djangotest-piaui.readthedocs.io/en/latest/). Se você quer construir essa aplicação na sua máquina, recomendo que a leia.

### Tecnologias Utilizadas

Para consutrução desta aplicação, foram utilizadas as seguintes ferramentas:

* [Django](https://www.djangoproject.com/) - Framework para Desenvolvimento Web escrito em Python!
* [DRF](https://www.django-rest-framework.org/) - Django Rest Framework, uma aplicação para desenvolvimento de API Restful
* [Bootstrap 4](https://getbootstrap.com/) - Framework de front-end para aplicações web.

### Instalação
Para instalar a aplicação, basta executar o seguinte comando no terminal:

```sh
$ docker-compose up --build
```
Prontinho, sua aplicação está rodando e poderá acessá-la localmente:
http://localhost:8000

### Acesso a Aplicação

Para acessar a aplicação e utilizar da rotina da API, será necessário fazer Login. Do contrário, você não conseguirá efetuar cadastro ou remoção de dados.

### Heroku

A aplicação também está disponível no Heroku através do link:
https://djangopiaui.herokuapp.com

Para efetuar login, utilize as seguintes informações:
```sh
 Usuário: admin
 Senha: 12345infog2
```

**Desenvolvido por [Linneu Lopes](https://github.com/LinneuDM)**
