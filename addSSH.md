# Como Criar uma Chave SSH no Windows (com Git Bash)

## 1. Verificar se o Git Bash está Instalado
Baixe e instale o [Git para Windows](https://git-scm.com/downloads) se ainda não tiver.

## 2. Abrir o Git Bash
No menu Iniciar, procure por **Git Bash** e abra-o.

## 3. Gerar uma Nova Chave SSH
Execute o seguinte comando:
```bash
ssh-keygen -t rsa -b 4096 -C "seu-email@example.com"
```
- `-t rsa`: Define o tipo de chave como RSA.
- `-b 4096`: Especifica o tamanho da chave.
- `-C "seu-email@example.com"`: Adiciona um comentário para identificação.

Pressione **Enter** para aceitar o caminho padrão (`~/.ssh/id_rsa`) ou especifique um diferente.

## 4. Definir uma Senha Opcional
Você pode definir uma senha para maior segurança ou apenas pressionar **Enter** para continuar sem senha.

## 5. Adicionar a Chave ao ssh-agent
Inicie o ssh-agent e adicione a chave:
```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
```

## 6. Copiar a Chave Pública para o Servidor
Para adicionar a chave pública a um servidor remoto, exiba seu conteúdo:
```bash
cat ~/.ssh/id_rsa.pub
```
Depois, copie e cole o conteúdo no arquivo `~/.ssh/authorized_keys` do servidor remoto.

## 7. Testar a Conexão SSH
Verifique se a autenticação funciona sem senha:
```bash
ssh usuario@servidor
```
Se tudo estiver correto, você estará conectado sem precisar digitar a senha!

## 8. Configuração Opcional: Arquivo `config`
Para facilitar a conexão, crie ou edite o arquivo `~/.ssh/config` e adicione:
```plaintext
Host meu-servidor
    HostName servidor
    User usuario
    IdentityFile ~/.ssh/id_rsa
```
Agora, basta rodar:
```bash
ssh meu-servidor
```
