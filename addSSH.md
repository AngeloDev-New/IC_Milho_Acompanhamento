# Como Criar uma Chave SSH

## 1. Verificar Chaves Existentes
Antes de criar uma nova chave SSH, verifique se já possui uma:
```sh
ls -al ~/.ssh
```
Se houver arquivos como `id_rsa` e `id_rsa.pub`, você já tem uma chave.

## 2. Gerar uma Nova Chave SSH
Para criar uma nova chave, execute:
```sh
ssh-keygen -t rsa -b 4096 -C "seu-email@example.com"
```
- `-t rsa`: Define o tipo de chave como RSA.
- `-b 4096`: Especifica o tamanho da chave.
- `-C "seu-email@example.com"`: Adiciona um comentário para identificação.

Aperte **Enter** para aceitar o caminho padrão (`~/.ssh/id_rsa`) ou especifique um diferente.

## 3. Definir uma Senha Opcional
Você pode definir uma senha para maior segurança ou apenas pressionar **Enter** para continuar sem senha.

## 4. Adicionar a Chave ao ssh-agent
Para facilitar a autenticação, adicione a chave ao ssh-agent:
```sh
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
```

## 5. Copiar a Chave Pública para o Servidor
Para adicionar a chave pública a um servidor remoto:
```sh
ssh-copy-id usuario@servidor
```
Caso o comando acima não esteja disponível, copie manualmente:
```sh
cat ~/.ssh/id_rsa.pub
```
E cole o conteúdo no arquivo `~/.ssh/authorized_keys` do servidor remoto.

## 6. Testar a Conexão SSH
Verifique se a autenticação funciona sem senha:
```sh
ssh usuario@servidor
```
Se tudo estiver correto, você estará conectado sem precisar digitar a senha!

## 7. Configuração Opcional: Arquivo `~/.ssh/config`
Para facilitar a conexão, adicione um alias ao arquivo `~/.ssh/config`:
```sh
echo "
Host meu-servidor
    HostName servidor
    User usuario
    IdentityFile ~/.ssh/id_rsa
" >> ~/.ssh/config
```
Agora, basta rodar:
```sh
ssh meu-servidor
