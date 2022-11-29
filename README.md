
<h1 align="center">
	<p align="center">Alura Receita - Django</p>
	<a href="https://alura-receita-django.herokuapp.com/"><img src="src\static\img\core-img\favicon.ico" alt="Alura Challenges"></a>
</h1>

<div align="center" id="badges">
    <img src="https://img.shields.io/badge/STATUS-COMPLETED-green"/>
</div>

---

# Alura Receita Django
## Descrição do Projeto
Projeto Django para cadastro de receitas desenvolvido durante o curso [Formação Django da Alura](https://www.alura.com.br/formacao-django). O projeto foi desenvolvido utilizando Python, Django com deploy na plataforma [Heroku](https://www.heroku.com), as imagens estão sendo hospedadas em um [Bucket S3 AWS](https://aws.amazon.com/pt/s3/).

O projeto está disponível no link: [alura-receita-django.herokuapp.com](https://alura-receita-django.herokuapp.com)
> ***Obs.: Devido as recentes alterações dos planos do Heroku, o site foi temporariamente desativado até eu encontrar outra opção viável.***

<div align="center">
    <img src="docs\alura_receita_tour.gif" width="400" height="200" />
</div>

---

## Requirements
- Python 3.10
- Django 4.1
- Heroku
---

## Endpoints
### Autenticação
Sinta-se a vontade para realizar um cadastro e testar a plataforma no link abaixo:

[Cadastro Alura Receita](https://alura-receita-django.herokuapp.com/usuario/cadastro)

Realize o login e cadastre suas receitas:

[Criar uma Receita](https://alura-receita-django.herokuapp.com/receita/criar)

---

## Executando o Projeto
Para executar o projeto forneça uma `SECRET_KEY` no arquivo `.env` e execute os comando abaixo:

`python -m pip freeze -r requirements.txt`

`python src/manage.py migrate`

`python src/manage.py createsuperuser`

`python src/manage.py runserver`

---

## Testes
Os testes podem ser executados através do comando:

`python src/manage.py test --debug-mode`
