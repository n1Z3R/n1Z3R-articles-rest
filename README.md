# Articles API app
Application Programming Interface for business logic of articles.
Which implements the publication of articles, commenting, likes. 
It also has a user model system with custom permissions.

Routing:

![image](https://user-images.githubusercontent.com/19762455/166974024-419000a2-b581-4c43-8130-4f2e5a3bbabb.png)

Check it out at: https://articles-rest-n1z3r.herokuapp.com/api/v1/

## Content ##

- **Registration (with validation)**
  - Email
     - Email mask
     - Unique
  - Password
     - Minimum one letter and one digit
     - Length equals nine
- **Custom backend of auth**
  - Using email and password
- **Custom permission**
  - Read for all 
  - Create for authenticated
  - Update and delete for owners
- **Search by**
  - Name of article
  - Content of article
