# README
**Author:** Lucas de Paula Souza  
**Date:** 2024-07-17  
**Version:** 3.0

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
        Users have the option to delete stored logins from the database. This feature helps in managing 
        and removing outdated or unwanted login credentials.

## Future Enhancements

### Offline, Static Database
        Implementing an offline, static database feature will allow users to store their passwords 
        locally without relying on an internet connection. This enhances security by reducing the 
        exposure to online threats.

### Enhanced Encryption
        To improve security, future versions will implement stronger encryption techniques. This 
        ensures hat even if the database is compromised, passwords remain secure and not easily 
        recognizable.

### Implementation Details

#### Encryption Methods
        In the `insert_frame.py` file, users can choose between two encryption methods: Caesar cipher 
        and Vigenère cipher, for encrypting passwords. If he chooses one, the other method must be 
        commented as in the following examples.
        
        - Caesar Cipher:
~~~python
        encrypted_password = lb.encrepter_cezar(password, login, site)
        #encrypted_password = lb.encrypted_vinegere(password, login, site))
~~~
        
        - Vigenère Cipher:
~~~python
        #encrypted_password = lb.encrepter_cezar(password, login, site)
        encrypted_password = lb.encrypted_vinegere(password, login, site))
~~~

#### Decryption Methods
        Similarly, in the `find_password_frame.py` file, users have the option to decrypt passwords 
        using either Caesar cipher or Vigenère cipher. Just like at the cryptography, here if he 
        chooses one, the other method must be commented as in the following examples.
        
        - Caesar Cipher:
~~~python
        decrypted_password = lb.decripter_cezar(encrypted_password)
        #decrypted_password = lb.decrypted_vinegere(encrypted_password, login_user)
~~~
        
        - Vigenère Cipher:
~~~python
        #decrypted_password = lb.decripter_cezar(encrypted_password)
        decrypted_password = lb.decrypted_vinegere(encrypted_password, login_user)
~~~

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
**Versão:** 3.0

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
        Os usuários têm a opção de excluir logins armazenados no banco de dados. Esta funcionalidade 
        ajuda na gestão e remoção de credenciais de login desatualizadas ou indesejadas.

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
        No arquivo `insert_frame.py`, os usuários podem escolher entre dois métodos de criptografia: 
        cifra de César e cifra de Vigenère, para criptografar senhas. Caso ele escolha um, o outro 
        método deve estar comentado como nos exemplos a seguir.
        
        - Cifra de César:
~~~python
        encrypted_password = lb.encrepter_cezar(password, login, site)
        #encrypted_password = lb.encrypted_vinegere(password, login, site))
~~~
        
        - Cifra de Vigenère:
~~~python
        #encrypted_password = lb.encrepter_cezar(password, login, site)
        encrypted_password = lb.encrypted_vinegere(password, login, site))
~~~

#### Métodos de Descriptografia
        Da mesma forma, no arquivo `find_password_frame.py`, os usuários têm a opção de descriptografar 
        senhas usando a cifra de César ou a cifra de Vigenère. Assim como na criptografia, aqui caso ele
        escolha um, o outro método deve estar comentado como nos exemplos a seguir.
        
        - Cifra de César:
~~~python
        decrypted_password = lb.decripter_cezar(encrypted_password)
        #decrypted_password = lb.decrypted_vinegere(encrypted_password, login_user)
~~~
        
        - Cifra de Vigenère:
~~~python
        #decrypted_password = lb.decripter_cezar(encrypted_password)
        decrypted_password = lb.decrypted_vinegere(encrypted_password, login_user)
~~~

#### Detalhes do Algoritmo de Criptografia
        A cifra de Vigenère no arquivo `login_bank.py` utiliza uma matriz 94 x 94 e um vetor contendo 
        caracteres que variam de letras (minúsculas e maiúsculas) a dígitos e caracteres especiais. 
        Essa combinação de matriz e vetor permite capacidades robustas de criptografia.

### Desenvolvimentos Futuros
        Estamos trabalhando para aprimorar a funcionalidade do aplicativo, incluindo a criação de um 
        executável mais amigável ao usuário e o desenvolvimento de um instalador para facilitar a 
        implantação do aplicativo.
