# Projeto: HackNewsMonitor (ou CyberAlert)

## Objetivo

Criar um monitor de notícias do Hacker News que envia alertas por e-mail sempre que surgirem notícias novas.

## Funcionalidades

1. **Raspagem de notícias**
   - Acessa a página principal ou RSS do Hacker News.
   - Coleta títulos e links das notícias.

2. **Filtragem de novidades**
   - Compara com as notícias já enviadas para evitar duplicatas.
   - Mantém um histórico em arquivo ou banco de dados leve (ex: SQLite, JSON).

3. **Envio por e-mail**
   - Envia um e-mail com:
     - Título da notícia
     - Link para o artigo
   - Pode usar **SMTP** (ex: Gmail) ou uma **API de e-mail**.

4. **Automação na nuvem**
   - Roda periodicamente (ex: a cada hora) usando:
     - **AWS Lambda + CloudWatch**
     - **Google Cloud Functions**
     - Ou outro serviço que permita cron jobs.

## Tecnologias

- Python
- BeautifulSoup (para raspagem de HTML)
- Requests (para acessar páginas)
- SQLite ou JSON (para histórico)
- SMTP / API de e-mail (para envio de alertas)
- AWS / Google Cloud / Azure (para automação na nuvem)

## Descrição resumida

O HackNewsMonitor funciona como um “Google Alert” personalizado para Hacker News, te avisando automaticamente sobre novas notícias, sem precisar checar manualmente.
