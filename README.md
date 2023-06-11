# E-Commerce_Store
The E-Commerce Store is a platform for selling used clothes. It uses Python/Django for backend and React for 
frontend, managing user profiles, product listings, and orders. It also features reviews, product recommendations, and advanced search.

# Models Description
Our e-commerce application uses several data models to represent the main entities in the system:

User Model:
The User model is provided by Django's built-in authentication framework. It represents the users of our e-commerce store. Each user has a username, password, and other fields such as email address, first name, and last name. The User model is used to handle user registration, login, and associated functionalities.

Product Model:
The Product model represents the items that are for sale in our e-commerce store. Each product has a name, description, price, and an associated image. This model is used to store and retrieve information about the products that our store offers.

Order Model:
The Order model represents the purchases made by users. Each order is associated with a user and contains one or more products. It also stores information such as the date of the order, whether the order is complete, and a transaction ID. This model is crucial for handling the buying process and keeping track of what users have purchased.

These models interact with each other to handle the main functionalities of our e-commerce store. The User model is connected to the Order model, as each order must be associated with a user. The Order model is also linked to the Product model, as each order contains one or more products. These connections between models are made using Django's foreign key functionality, allowing us to create complex relationships between data.