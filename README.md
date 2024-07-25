# README
**Author:** Lucas de Paula Souza  
**Date:** 2024-07-17  
**Version:** 3.5

## Description 
This program is a simple password manager with basic encryption capabilities. It allows users 
to securely store login credentials for various accounts.

## Features

### Inserting New Logins
The application provides functionality to insert new logins securely into the database. Each 
login entry includes details such as the site/app name, username, and encrypted password.

### Viewing and Searching Logins
Users can view a list of stored logins in a tabular format. The application supports searching 
for specific logins based on the site/app name.

### Decrypting Passwords
For authorized users, the program allows decrypting stored passwords. Upon providing the correct
master password, users can view the decrypted password for each stored login.

### Deleting Logins
Users have the option to delete stored logins from the database. The delete window now displays 
all records from the database, making it easier to manage and remove outdated or unwanted credentials.

### Selecting Encryption Method
Users can now choose the encryption method directly within the application. The available options 
are Caesar Cipher and Vigenère Cipher. This selection is made through the application's user interface 
and will be applied to both encryption and decryption processes.

## Future Enhancements

### Offline, Static Database
Implementing an offline, static database feature will allow users to store their passwords 
locally without relying on an internet connection. This enhances security by reducing the 
exposure to online threats.

### Enhanced Encryption
To improve security, future versions will implement stronger encryption techniques. This 
ensures that even if the database is compromised, passwords remain secure and not easily 
recognizable.

### Implementation Details

#### Encryption Methods
In the `insert_frame.py` file, you can choose between Caesar cipher and Vigenère cipher for encrypting passwords 
through the application's user interface. No need to modify the code to switch between encryption methods.

#### Decryption Methods
Similarly, in the `find_password_frame.py` file, passwords can be decrypted using either Caesar cipher 
or Vigenère cipher based on the user's selection within the application.

#### Encryption Algorithm Details
The Vigenère cipher in the `login_bank.py` file uses a 94 x 94 matrix and a vector containing 
characters ranging from letters (lowercase and uppercase) to digits and special characters. 
This matrix and vector combination enables robust encryption capabilities.

### Future Developments
Work is ongoing to enhance the functionality of the application, including creating a more 
user-friendly executable and developing an installer for easier app deployment.

---

# README -> pt - Br
**Autor:** Lucas de Paula Souza  
**Data:** 17-07-2024  
**Versão:** 3.5

## Descrição 
Este programa é um banco de senhas simples com um nível básico de criptografia. Ele permite 
armazenar logins de várias contas de forma segura.

## Funcionalidades

### Inserção de Novos Logins
A aplicação oferece funcionalidade para inserir novos logins de forma segura no banco de 
dados. Cada entrada de login inclui detalhes como nome do site/app, nome de usuário e 
senha criptografada.

### Visualização e Busca de Logins
Os usuários podem visualizar uma lista de logins armazenados em formato tabular. A aplicação 
suporta a busca por logins específicos com base no nome do site/app.

### Descriptografia de Senhas
Para usuários autorizados, o programa permite descriptografar senhas armazenadas. Ao fornecer 
a senha mestra correta, os usuários podem visualizar a senha descriptografada de cada login 
armazenado.

### Exclusão de Logins
Os usuários têm a opção de excluir logins armazenados no banco de dados. A janela de exclusão agora 
exibe todos os registros do banco de dados, facilitando a gestão e remoção de credenciais desatualizadas 
ou indesejadas.

### Seleção do Método de Criptografia
Agora, os usuários podem escolher o método de criptografia diretamente dentro do aplicativo. As 
opções disponíveis são Cifra de César e Cifra de Vigenère. A seleção é feita através da interface do 
aplicativo e será aplicada tanto para criptografia quanto para descriptografia de senhas.

## Melhorias Futuras

### Banco de Dados Offline e Estático
Implementar um recurso de banco de dados offline e estático permitirá que os usuários armazenem 
suas senhas localmente sem depender de uma conexão com a internet. Isso melhora a segurança ao 
reduzir a exposição a ameaças online.

### Criptografia Reforçada
Para aumentar a segurança, futuras versões implementarão técnicas de criptografia mais 
robustas. Isso garante que mesmo se o banco de dados for comprometido, as senhas permaneçam 
seguras e não sejam facilmente reconhecíveis.

### Detalhes de Implementação

#### Métodos de Criptografia
No arquivo `insert_frame.py`, você pode escolher entre a cifra de César e a cifra de Vigenère para 
criptografar senhas através da interface do aplicativo. Não é necessário modificar o código para 
alternar entre os métodos de criptografia.

#### Métodos de Descriptografia
Da mesma forma, no arquivo `find_password_frame.py`, as senhas podem ser descriptografadas usando 
cifra de César ou cifra de Vigenère com base na seleção do usuário dentro do aplicativo.

#### Detalhes do Algoritmo de Criptografia
A cifra de Vigenère no arquivo `login_bank.py` utiliza uma matriz 94 x 94 e um vetor contendo 
caracteres que variam de letras (minúsculas e maiúsculas) a dígitos e caracteres especiais. 
Essa combinação de matriz e vetor permite capacidades robustas de criptografia.

### Desenvolvimentos Futuros
Estamos trabalhando para aprimorar a funcionalidade do aplicativo, incluindo a criação de um 
executável mais amigável ao usuário e o desenvolvimento de um instalador para facilitar a 
implantação do aplicativo.
