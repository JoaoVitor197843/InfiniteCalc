
# 🧮 INFINITE CALC

![Static Badge](https://img.shields.io/badge/status-in_development-yellow)
![License](https://img.shields.io/github/license/JoaoVitor197843/InfiniteCalc)
![Last Commit](https://img.shields.io/github/last-commit/JoaoVitor197843/InfiniteCalc)
![Python](https://img.shields.io/badge/python-3.x-blue)

> A comprehensive math library made exclusively in Python - covering everything from the basic to advanced!

# 📑INDEX

- [Description](#️-description)
- [Features](#️-features)
- [Installation](#️-installation)
- [Usage examples](#-usage-example)
- [Contributions](#-contributions)
- [License](#license)

## 🗣️ DESCRIPTION

Infinite Calc is a math library entirely based on python that covers operations and expressions from the simplest to the most complex. In addition, this library includes calculations from other areas such as physics, chemistry, geography and literature.

## ⚒️ FEATURES

- `Basic Operations`:
  - Addition, Subtract, Multiply, Division.

- `Advanced Operations`:
  - Power: Calculates the    power of a number raised to N.
  - Nth rooting: Calculates nth roots.
  - Factorial: Calculates the factorial of a number.
  - Logarithms: Calculates logarithms of any base as well as natural logarithms.

- `Equation Solver`:
  - First-degree equation (linear): Calculates the root of an linear equation.
  - Second-degree equation (Bhaskara's formula): Calculate the two roots of a quadratic equation, supporting c = 0.
  - Discriminant(delta): Calculates the discriminant of the quadratic equation.

- `Mathematics constants with precision`:
  - π: Pi value accurate to 40 decimal places.
  - e: Euler's constant with 40 decimal places of precision.

## ⚙️ INSTALLATION

**Clone the repository**:  

```git clone <https://github.com/GhostPro1736/InfiniteCalc.git>```

**Import the library**:

import InfiniteCalc `module`

## 📖 USAGE EXAMPLE

### CALCULATING LOGARITHMS OF ANY BASE AND NATURAL LOGARITHMS

from InfiniteCalc import Operations  

**Logarithm of any base**  
print(Operations.log(1000,10)) ≈ 3.0  

**Natural logarithm**  
print(Operations.natural_log(2)) ≈ 0.6931

### BHASKARA'S FORMULA AND DISCRIMINANT DELTA

from InfiniteCalc import EqSolver  

**Quadratic equation**  
print(EqSolver.bhaskara(1,-3,2)) = (2.0, 1.0)  

**Discriminant delta**  
print(EqSolver.delta(1,-3,2)) = 1

## CONSTANTS

from InfiniteCalc import Constants

**Pi value**  
print(Constants.pi)

**Euler's constant**
print(Constants.e)

## 🏆 CONTRIBUTIONS

Contributions are always welcome! If you would like to contribute to this project, follow these steps:

1. Fork the repository.
2. Create a branch for your feature or fix (`git checkout -b my-feature`).
3. Commit your changes (`git commit -m 'I added my feature'`).
4. Push to the branch (`git push origin my-feature`).
5. Open a Pull Request.
6. Fill out the required information for the pull request, such as a detailed description of the changes you made. Make sure to provide clear and concise information so that the owner of the original repository can understand your contributions.
7. Click "Create pull request" to submit the pull request to the original repository. I will check the changes as soon as possible to bring new features or the necessary changes.

## 🤳 CONTACTS

If you want to talk with me, feel free to use any of this forms of contact:

- GitHub: [JoaoVitor197843](https://github.com/JoaoVitor197843)

- Discord: [.ghost_pro](https://discord.com/)

- Email: [João_Vitor](<mailto:jv2093809@gmail.com?subject=InfiniteCalc&bodyHi! I want to propose an idea to InfiniteCalc.>)

## 👨‍💻 AUTORS

[<img loading="lazy" src="https://avatars.githubusercontent.com/u/118195418?v=4" width=115><br><sub>João Vitor</sub>](https://github.com/JoaoVitor197843)

## LICENSE

This Open Source Project is using a MIT license [License MIT](LICENSE.md) acess the file for more details.
