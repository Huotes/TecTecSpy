# TecTecSpy - Keylogger em Python

**TecTecSpy** é um keylogger simples e escalável escrito em Python, projetado para capturar as teclas pressionadas pelo usuário e armazená-las em um arquivo de log. O projeto também permite capturar screenshots periódicas ou baseadas em eventos de teclado.

## Funcionalidades

- Captura de teclas pressionadas e gravação em logs.
- Captura de screenshots periódicas ou com base em eventos.
- Extensível para adicionar novos módulos (como envio de logs via e-mail).
- Arquitetura modular e organizada para fácil manutenção e escalabilidade.

## Estrutura do Projeto

```plaintext
TecTecSpy/
│
├── logs/                        # Diretório de logs de teclas
├── screenshots/                 # Diretório de screenshots capturadas
├── tecspy/                      # Diretório principal dos módulos do keylogger
│   ├── keylogger.py             # Módulo de captura de teclas
│   ├── logger.py                # Módulo de gravação de logs
│   ├── screenshot.py            # Módulo de captura de tela
│   ├── sender.py                # (Opcional) Módulo de envio de logs
│   ├── config.py                # Arquivo de configuração
│   └── utils.py                 # Funções utilitárias
├── tests/                       # Testes automatizados
├── main.py                      # Arquivo principal para rodar o keylogger
├── requirements.txt             # Arquivo com as dependências do projeto
├── .gitignore                   # Arquivo gitignore para evitar rastrear venv, logs, etc.
└── README.md                    # Documentação do projeto
