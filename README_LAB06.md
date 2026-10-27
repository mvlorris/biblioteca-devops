# Laboratorio Pratico 06 — Docker e GitHub Actions

Projeto: https://github.com/mvlorris/biblioteca-devops.

O Dockerfile empacota src/, tests/ e pytest==8.4.2 em uma imagem baseada em python:3.12-slim. O comando padrao executa os seis testes. O processo roda como appuser, UID 10001. E uma imagem de testes, nao uma imagem de runtime para producao.

## Execucao local

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python -m pytest -v
docker --version
docker info
docker build --progress=plain -t biblioteca-devops:1.0 .
docker image ls biblioteca-devops
docker image inspect biblioteca-devops:1.0
docker run --name biblioteca-devops-teste biblioteca-devops:1.0
docker ps -a
docker logs biblioteca-devops-teste
docker inspect biblioteca-devops-teste
docker rm biblioteca-devops-teste
docker run --rm biblioteca-devops:1.0
```

Se o usuario nao tiver acesso ao daemon, use sudo conforme a politica do ambiente. Nao e necessario associar o usuario ao grupo docker para o laboratorio; esse grupo concede privilegios elevados.

## Falha e correcao

Altere temporariamente a assercao do titulo em test_adicionar_livro de Clean Code para Livro Incorreto. Construa a imagem biblioteca-devops:teste-falha e execute docker run --rm. O pytest deve reprovar um teste e devolver codigo 1. Restaure Clean Code, reconstrua biblioteca-devops:1.0 e execute novamente. O resultado corrigido esperado e 6 passed e codigo 0. Os resultados reais sao documentados no relatorio de entrega.

## GitHub Actions

O workflow .github/workflows/docker-ci.yml roda em push/PR na main e permite acionamento manual. Ele verifica Docker, faz build, inspeciona a imagem, executa os testes no container e salva os logs e o codigo de saida. Uma falha de teste causa falha do job. A inspecao e o upload dos logs ainda rodam por if: always(). Quando os testes passam, uma segunda execucao valida --rm e confirma que a imagem continua disponivel.

Cada execucao publica somente arquivos de evidencia no artifact evidencias-docker, com retencao de 14 dias. Nao ha push da imagem para registry nem deploy. Os logs tambem foram exportados no pacote de entrega.

O .dockerignore exclui .git, .venv, caches, .env e arquivos de evidencia. A tag explicita da base facilita identificar a versao, mas nao a torna imutavel; para isso, pode-se fixar um digest apos validar as atualizacoes. A imagem de teste nao precisa de portas publicadas ou volumes permanentes.

GitHub e a plataforma do repositorio; GitHub Actions e o servico de CI usado nesta atividade. Jenkins e uma alternativa de CI, nao a mesma ferramenta. O Jenkinsfile do laboratorio anterior foi preservado. Este roteiro prepara o estudo de infraestrutura como codigo, mas nao pede provisionamento Terraform, publicacao ou implantacao em producao.
