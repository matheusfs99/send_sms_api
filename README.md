## Como rodar o projeto:
Para rodar o projeto local siga os seguintes passos:

1. clone o repositório do projeto num repositório local
   ```console 
    git clone git@github.com:matheusfs99/send_sms_api.git
   ```
2. crie uma conta na twilio, caso nao tenha, e passe os valores de TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN e TWILIO_PHONE_NUMBER no arquivo .env
3. rode os seguintes comandos:
    ```console
    cp .env-example .env
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver
   ```

## Regra de negócio:
 - Existem 2 modelos:
    - Contacts: onde são criados contatos informando nome e telefone do contato.
    - GroupContacts: onde são criados grupos que possuem contatos inseridos nesses grupos.

 - Para criar um contact, basta fazer um POST no endpoint `localhost:8000/api/contact/` passando o name e o phone (no formato +<código do país><ddd><número>) no body.
 - Para criar um group, basta fazer um POST no endpoint `localhost:8000/api/group/` passando o name e os contacts a serem incluídos neste grupo (no caso, é passado os ids dos grupos dentro de uma lista) no body
 - Para enviar um sms para os contatos do grupo, basta fazer um POST no endpoint `localhost:8000/api/send-sms/` passando o group e uma message no body da request.