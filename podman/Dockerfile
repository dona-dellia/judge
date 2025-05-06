# Usa imagem oficial do Python
FROM python:3.11-slim

# Instala o Git
RUN apt-get update && apt-get install -y git

# Define diretório de trabalho no container
WORKDIR /app

# Lista de repositórios para clonar
ENV REPOS="https://github.com/usuario/projeto_a.git https://github.com/usuario/projeto_b.git https://github.com/usuario/projeto_c.git"

# Clone ou atualize os repositórios
RUN for repo in $REPOS; do \
      dir=$(basename $repo .git); \
      if [ -d "$dir" ]; then \
        echo "📁 '$dir' já existe. Realizando git pull..."; \
        cd $dir && git pull && cd ..; \
      else \
        echo "📥 Clonando '$repo'..."; \
        git clone $repo; \
      fi \
    done

# Instala dependências de cada projeto
RUN pip install --no-cache-dir \
    -r projeto_a/requirements.txt \
    -r projeto_b/requirements.txt \
    -r projeto_c/requirements.txt

# Comando padrão para executar o script
CMD ["python", "run.py"]
