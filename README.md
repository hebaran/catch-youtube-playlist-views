# 📺 Coletor de Estatísticas de Playlist do YouTube com API

![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-brightgreen)
![Python](https://img.shields.io/badge/python-3.12%2B-blue)

Este projeto permite obter um relatório completo com **visualizações de todos os vídeos** de uma playlist do YouTube, utilizando a **API oficial do YouTube Data v3**. Ele lida automaticamente com **paginação** e busca todos os vídeos mesmo em playlists grandes.

---

### ✨ Funcionalidades

* **Autenticação via OAuth 2.0**
* **Coleta de informações de vídeos (título + views)**
* **Tratamento de playlists com mais de 50 vídeos (paginação via `nextPageToken`)**
* **Exibição ordenada de um relatório completo no terminal**

---

### 🛠️ Tecnologias Utilizadas

* **Python 3**
* **APIs utilizadas:**
  * [`google-auth-oauthlib`](https://pypi.org/project/google-auth-oauthlib/)
  * [`google-api-python-client`](https://pypi.org/project/google-api-python-client/)
* **Bibliotecas auxiliares:**
  * `os`
  * `utils.py` (funções utilitárias do próprio projeto)

---

### 🚀 Como Rodar o Projeto

> ⚠️ **Você precisará de uma credencial da API do YouTube (client_secrets.json)**. Veja abaixo como obter a sua.

1. **Clone este repositório:**

   ```bash
   git clone https://github.com/hebaran/catch-youtube-playlist-views.git
   cd catch-youtube-playlist-views
   ```

2. **Crie um ambiente virtual e ative:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Crie e configure o `secrets.json`:**

   Acesse [Google Cloud Console](https://console.cloud.google.com/):
   * Crie um projeto
   * Habilite a **YouTube Data API v3**
   * Vá em **Credenciais > Criar credenciais > ID do cliente OAuth**
   * Tipo de aplicativo: **App para computador**
   * Crie e baixe o `.json`, depois renomeie para **`secrets.json`** e coloque dentro do repositório
   * Em **Público-alvo**, adicione o e-mail que vai usar para logar no youtube em **Usuários de teste > Add users**

5. **Rode o projeto:**

   ```bash
   python main.py
   ```

6. **Cole o link da playlist** quando solicitado, e aguarde o relatório ser exibido no terminal.

---

### 🧾 Exemplo de Saída

```text
========================= Relatório Completo da Playlist =========================
1 - Como usar a API do YouTube: 24328 visualizações.
2 - Aula de Python para Web: 143329 visualizações.
3 - Criando um CRUD com FastAPI: 9831 visualizações.
...
```

---

### 🔐 Aviso de Segurança

> **NUNCA envie seu `secrets.json` para o GitHub** ou repositórios públicos. Ele contém dados sensíveis da sua conta do Google Cloud. Certifique-se de incluí-lo no `.gitignore`.

---

### 📂 Estrutura do Projeto

* `main.py` – Arquivo principal, contém a lógica de conexão com a API e exibição do relatório.
* `utils.py` – Funções auxiliares, como limpeza do terminal.
* `secrets.json` – Suas credenciais pessoais **(NÃO DEVE SER COMMITADO)**.
* `requirements.txt` – Dependências do projeto.

---

### 👨‍💻 Autor

* **Heitor Rangel**
* [LinkedIn](https://www.linkedin.com/in/heitor-rangel/)
* [GitHub](https://github.com/hebaran/)
