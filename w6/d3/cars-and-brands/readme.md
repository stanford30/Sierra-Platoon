# Cars and Brands

We are going to create a nested CRUD app that focuses on creating cars and their corresponding brands. Make it look nice and make sure your code is clean! Best of luck!

Here are our recommended steps for creating CRUD apps:
1. Schema
2. Migrations
3. Models
4. Associations
5. Validations
6. Create some text data in the database
7. Manually test your associations in the `django shell`
8. Create your routes
9. Visit each page and create the views/forms for each

In the end, you should be able to visit the following routes:

```
/brands # a list of all the car brands
/brands/new # form for a new car brand
/brands/<:id> # see a specific car brand
/brands/<:id>/edit # edit page for a specific car brand

/brands/<:brand_id>/cars # a list of cars for a specific car brand
/brands/<:brand_id>/cars/new # form for a new car under a specific car brand
/brands/<:brand_id>/cars/<:car_id> # see a specific car for a specific car brand
/brands/<:brand_id>/cars/<:car_id>/edit # edit page for a specific car under a specific car brand
```

Remember to start by creating a new virtual environment.

`python -m venv venv source venv/bin/activate`
`source venv/bin/activate`

Once you have your virtual environment up and running you can tell pip to download all the requirements for this app by running `pip install -r requirements.txt`. Make sure you are in the main directory of the repo (the one with the readme in it).

Next set up the database `car_app` by running `createdb car_app`.
