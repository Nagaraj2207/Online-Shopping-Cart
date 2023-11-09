# Online Shopping Cart

## Description

This project is an online shopping cart system designed for a supermarket. It enables customers to browse a list of items, select items for purchase, and generate a receipt with the total amount due. The system also incorporates a discount calculation feature for specific items and offers a lucky draw for registered customers.

## Classes and Inheritance

The project utilizes two levels of inheritance:

1. The first level involves a child class inheriting from the base class, introducing additional functionality for calculating discounts and generating receipts.

2. The second level includes a grandchild class inheriting from the child class and adding functionality for participating in a lucky draw.

## Functionality

#### 1. Shopping (Base Class)

- Provides functionality for user registration, including customer name, phone number, and customer ID.
- Allows customers to add items to the cart and generate receipts.
- Handles customer location and delivery options.

#### 2. Discount (Child Class)

- Inherits from the Shopping class and adds functionality for applying discounts to specific products (Sugar, Rice, Atta).
- Calculates the total cart price with discounts.

#### 3. LuckyDraw (Grandchild Class)

- Inherits from the Discount class and introduces functionality for a lucky draw.
- Randomly selects a prize for the customer in the lucky draw.

### Sample Interaction

The project demonstrates a sample interaction, including customer registration, item selection, discounts, and lucky draw participation. Here's a summary of the interaction:

1. User chooses "Sign up" and provides their name and phone number.

2. After registration, the user can sign in.

3. The user selects items to add to the cart, and discounts are applied to eligible products.

4. The user can generate a receipt and select a delivery option.

5. If the cart is not empty, the user can participate in the lucky draw.

## Steps to run the Projects

1. **Prerequisites**:
   - Ensure you have Python installed on your system.

2. **Clone the Project**:
   - Clone the project's repository from a version control system like GitHub, or download the project's source code if available.

3. **Navigate to the Project Directory**:
   - Use the `cd` command to navigate to the project directory where your main Python script is located.

4. **Run the Project**:
   - Run the main Python script that serves as the entry point to your project.

   ```
   python main.py
   ```

   Replace `main.py` with the actual name of your main script.

5. **Interact with the Project**:
   - After running the script, you can interact with the project based on the available functions and features provided by the OOP code.

6. **Customization (Optional)**:
   - If needed, you can customize the project by modifying the code within your Python script. Make changes to the OOP classes and methods to add or modify features.

7. **Testing**:
   - Thoroughly test the project to ensure that it functions as expected and handles various scenarios.

Since this approach is based on OOP principles and does not involve a database or web framework .
