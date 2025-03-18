# Como Criar uma Chave SSH no Windows

## 1. Verificar se o OpenSSH está Instalado
No Windows 10 e 11, o OpenSSH já vem instalado. Para verificar:
```powershell
Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'
```
Se não estiver instalado, adicione via:
```powershell
Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0
```

## 2. Gerar uma Nova Chave SSH
Abra o **PowerShell** ou o **Prompt de Comando** e execute:
```powershell
ssh-keygen -t rsa -b 4096 -C "seu-email@example.com"
```
- `-t rsa`: Define o tipo de chave como RSA.
- `-b 4096`: Especifica o tamanho da chave.
- `-C "seu-email@example.com"`: Adiciona um comentário para identificação.

Pressione **Enter** para aceitar o caminho padrão (`C:\Users\SeuUsuario\.ssh\id_rsa`) ou especifique um diferente.

## 3. Definir uma Senha Opcional
Você pode definir uma senha para maior segurança ou apenas pressionar **Enter** para continuar sem senha.

## 4. Adicionar a Chave ao ssh-agent
Inicie o serviço SSH-Agent e adicione a chave:
```powershell
Start-Service ssh-agent
ssh-add $env:USERPROFILE\.ssh\id_rsa
```

## 5. Copiar a Chave Pública para o Servidor
Para adicionar a chave pública a um servidor remoto manualmente, exiba seu conteúdo:
```powershell
Get-Content $env:USERPROFILE\.ssh\id_rsa.pub
```
Depois, copie e cole o conteúdo no arquivo `~/.ssh/authorized_keys` do servidor remoto.

## 6. Testar a Conexão SSH
Verifique se a autenticação funciona sem senha:
```powershell
ssh usuario@servidor
```
Se tudo estiver correto, você estará conectado sem precisar digitar a senha!

## 7. Configuração Opcional: Arquivo `config`
Para facilitar a conexão, crie ou edite o arquivo `config` em `C:\Users\SeuUsuario\.ssh\config` e adicione:
```plaintext
Host meu-servidor
    HostName servidor
    User usuario
    IdentityFile C:\Users\SeuUsuario\.ssh\id_rsa
```
Agora, basta rodar:
```powershell
ssh meu-servidor
```
