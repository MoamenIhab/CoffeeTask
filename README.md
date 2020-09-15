# CoffeeTask

i have build my code using flask , PyMongo 

## steps: 
 - First i have created the database using mongo db
 - created a flask application and connected it to the mongo db
 - builded up a rest api to get the data from the db
 
## How to use:
  - run the code on your local machine
  - visit the port its listening to in your browser or postman
  - input at the end '/machines' to access all machine
  - input at the end '/pods' to access all pods
  - input at the end '/machines/productType:<x>,waterLine:<y>' and replace x and y to your desired filters based on the original schema to access filtered machines
  - input at the end '/pods/productType:<x>,flavor:<y>,size:<z>' and replace x, y and z to your desired filters based on the original schema to access filtered pods

## PS: I CAN CREATE Other Basic Filters to only apply 1 filtered but this solution is generalized for the purpose of the task
  
## First task answers
### All espresso machines
- EM001
- EM002
- EM003

### All small pods
- CP001
- CP003
- CP011 
- CP013 
- CP021
- CP023
- CP031
- CP033
- CP041
- CP043

### All pods sold in 7 dozen packs
- EP007
- EP017
