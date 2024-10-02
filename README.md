# TecTecSpy - Keylogger em Python

<<<<<<< HEAD
**TecTecSpy** é um keylogger simples e escalável escrito em Python, projetado para capturar as teclas pressionadas pelo usuário e armazená-las em um arquivo de log. O projeto foi projetado para ser modular, facilitando a adição de novas funcionalidades no futuro, como o envio automático de logs via e-mail.
=======
**TecTecSpy** é um keylogger simples e escalável escrito em Python, projetado para capturar as teclas pressionadas pelo usuário e armazená-las em um arquivo de log. O projeto também permite capturar screenshots periódicas ou baseadas em eventos de teclado.
>>>>>>> be48feb7d730e01ca4a23d77d2c77d17b80da1bd

## Funcionalidades

- Captura de teclas pressionadas e gravação em logs.
- Extensível para adicionar novos módulos (como envio de logs via e-mail).
- Arquitetura modular e organizada para fácil manutenção e escalabilidade.

## Estrutura do Projeto

```plaintext
TecTecSpy/
│
├── logs/                        # Diretório de logs de teclas
<<<<<<< HEAD
=======
├── screenshots/                 # Diretório de screenshots capturadas
>>>>>>> be48feb7d730e01ca4a23d77d2c77d17b80da1bd
├── tecspy/                      # Diretório principal dos módulos do keylogger
│   ├── keylogger.py             # Módulo de captura de teclas
│   ├── logger.py                # Módulo de gravação de logs
│   ├── sender.py                # (Opcional) Módulo de envio de logs
│   ├── config.py                # Arquivo de configuração
│   └── utils.py                 # Funções utilitárias
├── tests/                       # Testes automatizados
│   ├── test_keylogger.py        # Testes do keylogger
│   ├── test_logger.py           # Testes do logger
├── main.py                      # Arquivo principal para rodar o keylogger
├── requirements.txt             # Arquivo com as dependências do projeto
├── .gitignore                   # Arquivo gitignore para evitar rastrear venv, logs, etc.
└── README.md                    # Documentação do projeto
