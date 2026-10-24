# Laboratório Prático 05 — Jenkins

Projeto: biblioteca-devops. Repositório: https://github.com/mvlorris/biblioteca-devops.

## Aplicação e testes

A função `buscar_livro(titulo, livros)` em `src/biblioteca.py` percorre a lista e retorna o primeiro dicionário cujo título é exatamente igual ao pesquisado. A comparação diferencia maiúsculas e minúsculas. Retorna `None` quando não encontra o livro ou quando recebe título vazio. Não altera a lista original.

Os arquivos de aplicação e os seis testes já existiam na branch main e foram preservados. Os três testes de busca cobrem livro encontrado, não encontrado e título vazio. Os demais cobrem cadastro e validação.

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
python3 -m compileall -q src tests
.venv/bin/python -m pytest -v
```

## Pipeline Jenkins

Crie o job `biblioteca-devops-ci` do tipo Pipeline. Em Definition, selecione Pipeline script from SCM; SCM: Git; URL: `https://github.com/mvlorris/biblioteca-devops.git`; branch: `*/main`; Script Path: `Jenkinsfile`. O repositório é público e o checkout não exige token.

O Jenkinsfile contém Checkout → Verificar ambiente → Build → Instalar dependências → Testes. O build usa compileall para validar a sintaxe; o pytest valida o comportamento. O relatório XML é publicado pelo plugin JUnit, inclusive se um teste falhar. O código de saída não zero do pytest provoca FAILURE.

Pré-requisitos no agente Linux: Git, Python 3 e python3-venv. No controller: Java compatível com a versão instalada e plugins Pipeline, Git, Timestamper e JUnit. Consulte https://www.jenkins.io/doc/book/installing/linux/ antes de instalar Jenkins LTS. Para Ubuntu, o roteiro utiliza Java 21.

```bash
sudo apt update
sudo apt install -y git python3 python3-venv python3-pip fontconfig openjdk-21-jre
```

`agent any` exige que todos os agentes elegíveis tenham os requisitos. O uso do executor do controller é apenas para laboratório isolado; prefira agentes separados em produção.

## Acionamento

`pollSCM('H/5 * * * *')` configura verificações aproximadamente a cada cinco minutos com distribuição por hash; só inicia um build se houver mudança detectada. Não é um webhook. Build Now permite disparo manual. O sandbox desta atividade não é hospedagem Jenkins permanente: o polling só funciona enquanto a instância estiver ativa. Uma instância própria pode importar o Jenkinsfile para manter a automação.

## Falha e correção

Após obter SUCCESS, mude temporariamente a asserção em `test_adicionar_livro` de `Clean Code` para `Livro Incorreto`, registre a alteração em commit e execute o Jenkins. O build deve falhar no estágio Testes, com 1 failed e 5 passed. Leia os logs e restaure `Clean Code`, registre a correção em novo commit e execute novamente: 6 passed e SUCCESS. Os commits e logs reais da atividade serão incluídos na entrega.

Jenkins coordena tarefas repetíveis e oferece feedback rápido sobre cada revisão do código. Esta atividade cobre integração contínua; nenhum deploy de produção é realizado.
