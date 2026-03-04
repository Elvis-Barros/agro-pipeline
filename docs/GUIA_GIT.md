# 🔧 Guia: Subindo o projeto no GitHub (passo a passo)

Execute esses comandos **uma única vez** para iniciar o repositório local
e conectá-lo ao GitHub.

---

## 1. Navegue até a pasta do projeto
```bash
cd agro-pipeline
```

## 2. Inicie o repositório Git
```bash
git init
```
> Isso cria o repositório Git local. Aparece a mensagem: "Initialized empty Git repository"

## 3. Adicione todos os arquivos ao controle de versão
```bash
git add .
```
> O ponto (.) significa "todos os arquivos da pasta". O .gitignore já garante
> que arquivos desnecessários não entrem.

## 4. Faça o primeiro commit
```bash
git commit -m "feat: estrutura inicial do projeto agro-pipeline"
```
> Um commit é como um "save" com mensagem. A convenção "feat:" é padrão
> profissional (Conventional Commits) e impressiona em portfólios.

## 5. Crie o repositório no GitHub
- Acesse https://github.com/new
- Nome: `agro-pipeline`
- Descrição: `Pipeline de dados end-to-end aplicado ao agronegócio brasileiro`
- Deixe como **público** (para o portfólio aparecer)
- **NÃO** marque "Add README" (já temos o nosso)
- Clique em "Create repository"

## 6. Conecte o repositório local ao GitHub
```bash
git remote add origin https://github.com/SEU-USUARIO/agro-pipeline.git
git branch -M main
git push -u origin main
```
> Substitua SEU-USUARIO pelo seu nome de usuário do GitHub.

---

## ✅ Verificação
Acesse https://github.com/SEU-USUARIO/agro-pipeline  
Você deve ver a estrutura de pastas e o README renderizado com formatação.

---

## 📌 Após cada projeto, o comando para atualizar será sempre:
```bash
git add .
git commit -m "feat: projeto01 scraping preço da soja"
git push
```
