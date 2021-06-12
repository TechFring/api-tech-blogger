<h1 align="center">
<br />
API TECH BLOGGER
</h1>

<br />

## 🚀 Tecnologias

- ✔️ Python

- ✔️ Django

- ✔️ Django REST Framework

<br />
<br />

## 💻 Demo

<a href="https://api-tech-blogger.herokuapp.com/api/v1/">https://api-tech-blogger.herokuapp.com/api/v1/</a>

<br/>
<br/>

## ⚙️ Executando ambiente de desenvolvimento

<strong>Clone o projeto e acesso o diretório via terminal para prosseguir (os comandos a seguir foram testados somente no Linux)</strong>

<br/>

<span>Criando o ambiente virtual e instalando as dependências do projeto</span>

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.tx
```

<br/>

<span>Migrando o banco de dados</span>

```
python3 manage.py migrate
```

<br/>

<span>Criando super usuário</span>

```
python3 manage.py createsuperuser
```

<br/>

<span>Rodando projeto</span>

```
python3 manage.py runserver
```