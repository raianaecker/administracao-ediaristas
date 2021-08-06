# Projeto E-diaristas

### Instalando o projeto

#### Clonar o projeto
`git clone https://github.com/raianaecker/administracao-ediaristas`

#### Instalar dependências
`pip install -r requirements.txt`

#### Alterar as configurações do BD no arquivo `settings.py`
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_bd',
        'HOST': 'host_bd',
        'PORT': 'porta_bd,
        'USER': 'usuario_bd',
        'PASSWORD': 'senha_bd'
    }
}
```

#### Migrar banco de dados
`python manage.py migrate`

#### Iniciar o servidor
`python manage.py runserver`