# Amazot
Code for an automated servebot that chats with you regarding the specs of the ec2 instance that you want to deploy and deploys the instance automatically upon approval

User Input:

1. User opens the chat window and asks for instance creation
"Hello xxx, I'd like to create an instance"
2. Lex responds back with more questions about the instance type and other questions
"Hello User, what instance type are you looking for? We have these available ... list the types available"
3. FInally after all the prompts, Lex executes a lamda function to create a .txt file with all the user requirements and sends out the text file to the admin

Admin creation of instances:

4. Admin receives the .txt file with user information and user requirements for the instance and see if it's approved/ not approved
5. Admin opens the chat window and enters ask for instance creation
"Hello xxx, please create the following instances -instance type ......"
6. Lex then asks for more infor regarding the instances and also the user info such as email address
7. When received with all the required info, Lex then executes the lambda function specific to instances such as create/run
8. After creating the instance, it asks if it should send an email to the user, if yes, it executes send email lamda function
