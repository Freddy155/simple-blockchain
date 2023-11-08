Simple Blockchain Documentation
===============================

Introduction
------------

Welcome to the documentation for the "Freddy155/simple-blockchain" project. This is a basic example of a blockchain implemented in Python. It allows for the creation of coins, transferring them between users, and mining new blocks.

### Table of Contents

1.  [Getting Started](#getting-started)
    -   [Prerequisites](#prerequisites)
    -   [Installation](#installation)
2.  [Usage](#usage)
    -   [Creating Coins](#creating-coins)
    -   [Transferring Coins](#transferring-coins)
    -   [Mining New Blocks](#mining-new-blocks)
    -   [Checking Balances](#checking-balances)
3.  [Code Structure](#code-structure)
4.  [Contributing](#contributing)
5.  [License](#license)

Getting Started
---------------

### Prerequisites

-   Python 3.x
-   Git (for cloning the repository)

### Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/Freddy155/simple-blockchain.git
    ```

2.  Change to the project directory:

    ```bash
    cd simple-blockchain
    ```

3.  Run the blockchain app:

    ```bash
    python app.py
    ```

Usage
-----

The "Freddy155/simple-blockchain" project allows you to perform basic blockchain operations.

### Creating Coins

To create coins for a user, use the `create_coin` method. For example, to create 100 coins for the user "Alice," execute the following code on one of the running instances of the app:

```python
my_blockchain.create_coin("Alice", 100)
```


This will create 100 coins for Alice.

### Transferring Coins

To transfer coins from one user to another, use the `transfer_coin` method. For example, to transfer 30 coins from Alice to Bob, execute the following code on the same instance:

```python
my_blockchain.transfer_coin("Alice", "Bob", 30)
```

This will transfer 30 coins from Alice to Bob.

### Mining New Blocks

You can mine new blocks using the `mine` method. Mining adds new blocks to the blockchain. To mine a new block with a specified difficulty level (e.g., difficulty level 4), run:

```python
my_blockchain.mine(4)
```

The mining process may take some time and computational effort as it requires finding a hash with the desired number of leading zeros (defined by the difficulty level).

### Checking Balances

To check the balances of users, use the `get_balance` method. For example, to check Alice's balance, execute:

```python

balance = my_blockchain.get_balance("Alice")
print(f"Alice's balance: {balance}")
```

This will print Alice's current balance.

Code Structure
--------------

The code for the "Freddy155/simple-blockchain" project is structured as follows:

-   `app.py`: The main application script that combines the Block and Blockchain classes to create and manage the blockchain.

-   `Block`: A class that represents individual blocks in the blockchain.

-   `Blockchain`: A class that manages the blockchain, including adding blocks, validation, and mining.

Contributing
------------

Contributions to this project are welcome. If you'd like to contribute, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix: 
```bash
git checkout -b feature-name
```
3.  Make your changes and test them.
4.  Commit your changes: 
```bash
git commit -m "Your commit message"
```
5.  Push your branch: 
```bash
git push origin feature-name
```
6.  Create a pull request.

License
-------

This project is licensed under the MIT License - see the [LICENSE](/LICENSE) file for details.