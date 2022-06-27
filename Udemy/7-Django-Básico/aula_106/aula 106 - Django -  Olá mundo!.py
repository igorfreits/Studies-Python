"""Django: Olá mundo!

-https://docs.djangoproject.com/pt-br/4.0/
-Framework
-Crianção de website (back-end)

X - nome do projeto/app
-Inicia projeto com todos os arquivos necessários
    django-admin startproject "X" .(TERMINAL)
    (inserir ponto para nao criar mais de uma pasta)

-Criar um servidor local
    python manage.py runserver(TERMINAL)
        CTRL+C para cancelar o servidor local

-Posta site na web
    wsgi.py

-Apps - sessões (EX: pagina inicial, produtos, sobre, blog)
    python manage.py startapp "Nome do app"(TERMINAL)
    Registrar em INSTALLED_APPS(settings.py-principal)
        "X"."X"Config - blog.BlogConfig
    Criar url referente ao app que foi criado(urls.py) - importar o include
        path('X'/,include('X.urls)) - path('blog/', include('blog.urls'))
        Criar urls.py dentro da pasta do app criado
    Deve setar as sessões em urls(EX: ling que redimensiona pro blog)

-Migrations - Base de dados
"""
