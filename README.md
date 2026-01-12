# soundmirror-phoneme-backend (single-language demo)

This is a minimal example repo to deploy a single English service to Railway via GitHub Actions.

Files:
- `app.py` - tiny Flask app that exposes `/` and `/health`.
- `Dockerfile` - builds and runs the app with Gunicorn.
- `.github/workflows/deploy.yml` - GitHub Action to deploy the service to Railway.

How to set up
1. Create a new GitHub repository and add these files (you can copy/paste them using the web UI).
2. In Railway, create a project (or use an existing one). Note its Project ID on the project settings page.
3. In the Railway project settings → Tokens, create a new *project token* (not an account token). Copy the token value.
4. In GitHub repo → Settings → Secrets & variables → Actions:
   - Add a secret named `RAILWAY_TOKEN` — paste the project token.
   - Optionally add `RAILWAY_PROJECT_ID` — paste the Railway project ID (recommended).
5. In GitHub Actions, open the "Deploy English to Railway" workflow and click "Run workflow" to trigger a deployment.
6. Watch the Actions logs — the workflow runs `railway up` non-interactively. On success, check Railway dashboard for the new service (`soundmirror-en`).

Notes
- Do NOT call `railway login` or `railway link` in CI. Provide the token via the `RAILWAY_TOKEN` secret only.
- If you want the workflow to run automatically on pushes, change `on:` in `.github/workflows/deploy.yml` (but be careful: deploying on every push may start many deployments).
- The example sets `MODEL_ID` as an environment variable in Railway after deployment. You can adjust that to change the model used by your service.
