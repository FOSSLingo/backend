# Backend for FOSSLingo

### Deploying (Vercel preferred)

The best (free!) way to host would probably be on Vercel. Click this button to deploy instantly!

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FFOSSLingo%2Fbackend&project-name=fosslingo-backend&repository-name=fosslingo-backend)

Or, follow these instructions manually;

1. Create a Vercel account and link your Github account to it (Create a Github account if you don't have one)

2. Fork `FOSSLingo/backend`

3. In Vercel, select "Import Project" and select 
"backend". This is the repo we forked.

4. Click "Deploy", and note down the URL it gives you! This URL will be used in your selfhosted frontend.

### Self hosting deploy

If you would like to self host the backend on your own machine, follow these instructions. 

> [!TIP]
> We don't cover port forwarding / exposing to the web,
> but for that, we recommend `cloudflared`!

1. Clone this repo somewhere easy to access: 

```bash
git clone https://github.com/FOSSLingo/web
```

2. cd into the directory:

```bash
cd web
```

3. Create a Python venv: 

```bash
uv venv venv
```

4. Activate the venv: 

```bash
venv\Scripts\activate
```

5. Install dependencies: 

```bash
uv pip install -r requirements.txt
```

6. Start server: 

```bash
fastapi run main.py --host 0.0.0.0 --port 8000
```

or run

```bat
start.bat
```