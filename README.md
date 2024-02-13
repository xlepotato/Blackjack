<a name="readme-top"></a>



[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
<h2 align="center">Blackjack Game ♠</h2>

  <p align="center">
    A command-line interface (CLI) implementation of the classic casino card game, Blackjack. <br />
    Try your luck by fighting against a computer dealer today and strive to get a hand closest to 21!
    <br />
    <br />
    <a href="#about-the-project"><strong>Explore the docs »</strong></a>
    <br />
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#use-case-diagram">Use Case Diagram</a></li>
        <li><a href="#class-diagram">Class Diagram</a></li>
        <li><a href="#activity-diagram">Activity Diagram</a></li>
        <li><a href="#project-structure">Project Structure</a></li>
      </ul>
    </li>
    <li><a href="#design-choices">Design Choices</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<p align="center">
<img src="https://github.com/xlepotato/Blackjack/assets/22700895/f8e46497-3d58-487c-8a01-002345424431" width="550" height="350">
</p>

### Use Case Diagram

<p align="center">
<img src="https://github.com/xlepotato/Blackjack/assets/22700895/46058c1b-d479-41d3-b3e6-5468ad846a8b" width="350" height="350">
</p>

### Class Diagram

<p align="center">
<img src="https://github.com/xlepotato/Blackjack/assets/22700895/0054410d-2ee5-4bc8-8dc8-b60c856f6c86" width="350" height="350">
</p>

### Activity Diagram

<p align="center">
<img src="https://github.com/xlepotato/Blackjack/assets/22700895/f36159b7-2fb5-48ff-8fab-b9f95fbef27d" width="350" height="350">
</p>


### Project Structure

### `main.py`
This file contains the main entry point of the game. It initializes the game components, such as the player, dealer, and game engine, and starts the game loop.

### `blackjack/`
This directory contains the Python package for the Blackjack game.

#### `baseplayer.py`
Defines the `BasePlayer` class, which serves as the base class for both the player and dealer classes. It contains common functionalities and attributes shared between players and the dealer.

#### `player.py`
Contains the `Player` class, which represents the human player in the game. It handles player actions such as placing bets, hitting, standing, and managing the player's balance.

#### `dealer.py`
Defines the `Dealer` class, representing the game's computer dealer. It manages the dealer's actions during the game, such as hitting until reaching a certain threshold and revealing the hidden card.

#### `card.py`
Contains the `Card` class, which represents a playing card in the game. It defines the properties of a card, such as its suit, rank, and value.

#### `deck.py`
Defines the `Deck` class, representing a deck of playing cards used in the game. It manages the creation, shuffling, and dealing of cards.

#### `hand.py`
Contains the `Hand` class, which represents a player's hand of cards. It manages the cards in the hand, computes the hand's total value, and handles adding new cards to the hand.

#### `game.py`
Defines the `Game` class, which manages the core logic of the Blackjack game. It orchestrates the interactions between the player, dealer, and deck, and determines the outcome of each round.

#### `banner.py`
Contains the `display_banner` function, which displays the ASCII art banner and game rules at the start of the game.

### `tests/`
This directory contains the essential test cases for the Blackjack game.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Design Choices
- **Modular Structure**: The project is structured as a Python package (`blackjack/`) with each component (player, dealer, game logic, etc.) in separate modules. This promotes code organization and reusability.
- **Object-Oriented Design**: The game components (player, dealer, cards) are implemented as classes with well-defined responsibilities and interfaces. This allows for easy extensibility and maintenance.
- **CLI Interface**: The game is implemented as a command-line interface, making it accessible and easy to play without the need for graphical user interfaces.

<p align="center">
<img src="https://github.com/xlepotato/Blackjack/assets/22700895/94c83b96-48a7-42b3-822a-4d50389c1054" width="350" height="350">
</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running, follow these simple example steps.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/xlepotato/Blackjack.git
   ```
2. Install all the required dependencies
   ```sh
   pip install -r requirements.txt
   ```
3. Run the application by executing the following command in the directory where main.py resides in
   ```sh
   python main.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

The video below is a walkthrough of the Blackjack CLI Game. 

https://github.com/xlepotato/Blackjack/assets/22700895/0c8c3f3f-1ced-4f05-a980-2c6e22c07a40


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See [LICENSE](https://github.com/xlepotato/Blackjack/blob/main/LICENSE) for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Harvard University, CS50P 2024](https://cs50.harvard.edu/python/2022/)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/xlepotato/Blackjack.svg?style=for-the-badge
[contributors-url]: https://github.com/xlepotato/Blackjack/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/xlepotato/Blackjack.svg?style=for-the-badge
[forks-url]: https://github.com/xlepotato/Blackjack/network/members
[stars-shield]: https://img.shields.io/github/stars/xlepotato/Blackjack.svg?style=for-the-badge
[stars-url]: https://github.com/xlepotato/Blackjack/stargazers
[issues-shield]: https://img.shields.io/github/issues/xlepotato/Blackjack.svg?style=for-the-badge
[issues-url]: https://github.com/xlepotato/Blackjack/issues
[license-shield]: https://img.shields.io/github/license/xlepotato/Blackjack.svg?style=for-the-badge
[license-url]: https://github.com/xlepotato/Blackjack/blob/main/LICENSE

