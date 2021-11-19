package labs.control_structures.iteration;

import java.util.*;

enum Actions {
  DEPOSIT,
  PLAY,
  QUIT
}

enum GameCategories {
  DICE_ROLL,
  COIN_FLIP,
  COLOR_SPINNER,
}

enum Colors {
  RED,
  GREEN,
  BLUE,
  YELLOW
}

enum CoinFlip {
  HEADS,
  TAILS
}

public class Lab09 {

  // Constants
  private static final Scanner scanner = new Scanner(System.in);

  public static void main(String[] args) {
    // Hyper Parameters
    boolean play = true;

    // User Variables
    int bankBalance = 0;
    Actions action;

    while (play) {
      // Welcome Message
      System.out.println("Welcome To My Game.\n");

      // Display User Information
      System.out.println("You Have $" + bankBalance + " In Your Bank Account.");

      // Display Actions: DEPOSIT, PLAY, QUIT
      System.out.println("[1] Deposit Money.");
      System.out.println("[2] Play Game.");
      System.out.println("[3] Quit Game.");

      System.out.print("What Action Would You Like To Commit? >>> ");
      action = Actions.values()[scanner.nextInt() - 1];

      // Check Decision
      if (action == Actions.DEPOSIT) {
        bankBalance = deposit(bankBalance);
      } else if (action == Actions.PLAY) {
        bankBalance = play(bankBalance);
      } else if (action == Actions.QUIT) {

      }
    }
  }

  private static int deposit(int currentBankBalance) {
    // User Variables
    int amountDeposit;
    int newBankBalance;

    // Take Input
    System.out.print("How Much Money Would You Like To Deposit? >>> ");
    amountDeposit = scanner.nextInt();

    // Return New Bank Balance
    newBankBalance = currentBankBalance + amountDeposit;
    return newBankBalance;
  }

  private static int play(int currentBankBalance) {
    // User Variables
    int diceRollChoice;
    CoinFlip coinFlipChoice;
    Colors colorChoice;
    
    // Game Results
    int diceRollResult = (int)((Math.random() * 5) + 1);

    CoinFlip coinFlipResult;
    if ((int)(Math.random() * 100) % 2 == 0) {
      coinFlipResult = CoinFlip.HEADS;
    } else {
      coinFlipResult = CoinFlip.TAILS;
    }

    Colors colorResult = Colors.values()[(int)((Math.random() * 3) + 1)];

    // Game Choices
    System.out.println("What Is Your Choice On The Dice Roll? >>> ");
    diceRollChoice = scanner.nextInt();

    System.out.println("What Is Your Choice On The Coin Flip? >>> ");
    switch (scanner.next().toUpperCase(Locale.ROOT).charAt(0)) {
      case 'H':
        coinFlipChoice = CoinFlip.HEADS;
      case 'T':
        coinFlipChoice = CoinFlip.TAILS;
    }

    System.out.println("What Is Your Choice On The Color Spinner? >>> ");
    switch (scanner.next().toUpperCase(Locale.ROOT).charAt(0)) {
      case 'R':
        colorChoice = Colors.RED;
      case 'G':
        colorChoice = Colors.GREEN;
      case 'B':
        colorChoice = Colors.BLUE;
      case 'Y':
        colorChoice = Colors.YELLOW;
    }

    return 0;
  }
}
