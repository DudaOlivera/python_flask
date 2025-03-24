## 🛠️ CRUD de Produtos com Flask

Bem-vindo ao projeto CRUD de Produtos! Este é um aplicativo web simples, desenvolvido em Python usando o framework Flask e MySQL, que permite criar, ler, atualizar e excluir (CRUD) produtos. 

## 💻 Estrutura do Projeto

PROJECT/  
│  
├── __pycache__/  
│  
├── static/  
│   └── style.css  
│  
├── templates/  
│   ├── create.html  
│   ├── index.html  
│   └── update.html  
│  
├── app.py  
└── config.py  

- **static/**: Contém arquivos estáticos como CSS.
- **templates/**: Armazena os arquivos HTML para a interface do usuário.
- **app.py**: O código principal do aplicativo.
- **config.py**: Configurações do banco de dados.

## 📦 Pré-requisitos

Antes de começar, você precisa ter os seguintes itens instalados:

- [Python 3](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/)
- [PyMySQL](https://pymysql.readthedocs.io/)
- [MySQL](https://www.mysql.com/)

Você pode instalar as dependências necessárias com o seguinte comando:

```bash
pip install Flask PyMySQL  
```

## ⚙️ Configuração do Ambiente

1. Certifique-se de que o MySQL está instalado e em execução.
2. Crie um banco de dados chamado `produto`.
3. Altere as configurações em `config.py` conforme necessário:

```python
class Config:
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = 3307  # ou a porta que você usa
    MYSQL_USER = 'root'  # seu usuário do MySQL
    MYSQL_PASSWORD = 'alunos'  # sua senha do MySQL
    MYSQL_DB = 'produto'
```

## 🚀 Como Executar

Para rodar o aplicativo, execute o seguinte comando no terminal:

```bash
python app.py
```

Acesse `http://127.0.0.1:5000` em seu navegador.

## 📝 Funcionalidades

- **Criar**: Adicione novos produtos ao banco de dados.
- **Ler**: Visualize todos os produtos armazenados.
- **Atualizar**: Edite os detalhes de produtos existentes.
- **Excluir**: Remova produtos do banco de dados.

## 🎨 Personalização

As estilizações podem ser encontradas em `static/style.css`, onde você pode modificar cores, fontes e layout de acordo com suas preferências.

## 🤝 Contribuições

Sinta-se à vontade para abrir issues ou pull requests se tiver sugestões ou melhorias!

## 📄 Licença

Este projeto é especializado para fins educacionais, então sinta-se à vontade para explorar e modificar como quiser. 

---

Espero que este projeto te ajude a entender melhor como funciona o Flask e a interação com bancos de dados! 🚀
