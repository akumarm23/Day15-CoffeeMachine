# Coffee Machine Simulator v0.1

![MIT License](https://img.shields.io/badge/License-MIT-darkblue.svg)
![Python Version](https://img.shields.io/badge/Python-3.8-green.svg)
![Version](https://img.shields.io/badge/Version-0.1-lightblue.svg)

## Overview

This Coffee Machine Simulator is a simple Python program that simulates the functionality of a coffee vending machine. Users can choose from a menu of drinks, insert coins to make a purchase, and the machine will dispense the selected drink if the required resources are available. The program incorporates a visual interface with ASCII art and supports features such as reporting on available resources and turning off the machine.

## Features

- **User-Friendly Interface:** Utilizes the `art` library to display an attractive ASCII art logo for an engaging user experience.

- **Menu Options:** Offers a menu of drinks including Espresso, Latte, and Cappuccino, each with its own set of ingredients and cost.

- **Resource Management:** Tracks available resources such as water, milk, and coffee grounds. Users are notified if there are insufficient resources to fulfill their order.

- **Coin Processing:** Allows users to insert coins (quarters, dimes, nickels, and pennies) to make a purchase. The program calculates the total amount inserted.

- **Transaction Handling:** Verifies if the inserted coins are sufficient to cover the cost of the selected drink. If successful, the program provides change and updates the profit.

- **Machine Control:** Users can turn off the machine to exit the program. A report option provides details on available resources.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/akumarm23/Day15-CoffeeMachine.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Day15-CoffeeMachine
   ```

3. Run the coffee machine program:

   ```bash
   python main.py
   ```

## Usage

1. When prompted, enter the name of the desired drink (Espresso, Latte, or Cappuccino).

2. Follow the instructions to insert the required coins.

3. The machine will process the transaction, dispense the drink, and provide change if applicable.

4. To check available resources, type "report" during the drink selection prompt.

5. To turn off the machine, type "off" during the drink selection prompt.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- ASCII art generated using the `art` library.

## Version History

- **v0.1:** Initial release
