from app import app, cli

@app.shell_context_processor
def make_shell_context():
    return {}