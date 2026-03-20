FROM python:3.12

ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /workspaces/my-workflow-plus

RUN apt-get update && apt-get install -y \
    curl ca-certificates gnupg wget grep git tree sqlite3 \
    build-essential clang cmake gdb lldb valgrind && \
    curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - && \
    apt-get update && apt-get install -y nodejs && \
    rm -rf /var/lib/apt/lists/*
    # python -m pip install --upgrade pip

RUN echo 'export PS1="bernardo\w> "' >> /root/.bashrc && \
    echo '.mode qbox' > /root/.sqliterc

CMD ["bash"]
