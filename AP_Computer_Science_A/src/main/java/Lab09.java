import java.util.*;

enum Actions {
  DEPOSIT,
  PLAY,
  QUIT
}

enum GameCategories {
  DICE_ROLL("Dice Roll"),
  COIN_FLIP("Coin Flip"),
  COLOR_SPINNER("Color Spin");

  public final String label;

  GameCategories(String label) {
    this.label = label;
  }
}

enum Colors {
  NULL("Null"),
  RED("Red"),
  GREEN("Green"),
  BLUE("Blue"),
  YELLOW("Yellow");

  public final String label;

  Colors(String label) {
    this.label = label;
  }

  public boolean equals(Colors color) {
    return label.equals(color.label);
  }
}

enum CoinFlip {
  NULL("Null"),
  HEADS("Heads"),
  TAILS("Tails");

  public final String label;

  CoinFlip(String label) {
    this.label = label;
  }

  public boolean equals(CoinFlip coinFlip) {
    return label.equals(coinFlip.label);
  }
}

public class Main {

  // Constants
  private static final Scanner scanner = new Scanner(System.in);

  public static void main(String[] args) {
    // Hyper Parameters
    boolean play = true;

    // User Variables
    double bankBalance = 0d;
    Actions action;

    // Welcome Message
    System.out.println("Welcome To My Game.");

    while (play) {
      System.out.println();

      // Display User Information
      System.out.println("You Have $" + bankBalance + " In Your Bank Account.");

      // Display Actions: DEPOSIT, PLAY, QUIT
      System.out.println("[1] Deposit Money.");
      System.out.println("[2] Play Game.");
      System.out.println("[3] Quit Game.");

      // Prompt Used For Action
      System.out.print("What Action Would You Like To Take? >>> ");
      action = Actions.values()[scanner.nextInt() - 1];

      System.out.println();

      // Check Decision
      if (action == Actions.DEPOSIT)
        bankBalance = deposit(bankBalance);
      else if (action == Actions.PLAY)
        bankBalance = play(bankBalance);
      else if (action == Actions.QUIT) {
        quit(bankBalance);
        play = false;
      }
    }
  }

  private static double deposit(double currentBankBalance) {
    // User Variables
    double amountDeposit;
    double newBankBalance;

    // Take Input
    System.out.print("How Much Money Would You Like To Deposit? >>> ");
    amountDeposit = scanner.nextInt();

    // Return New Bank Balance
    newBankBalance = currentBankBalance + amountDeposit;
    return newBankBalance;
  }

  private static double play(double currentBankBalance) {
    // User Variables
    int betAmount;
    int diceRollChoice;
    CoinFlip coinFlipChoice;
    Colors colorChoice;

    // User Input
    System.out.print("How Much Money Would You Like To Bet? >>> ");
    betAmount = scanner.nextInt();

    while (betAmount > currentBankBalance) {
      System.out.print("Please Enter A Valid Amount That Is At Most $" + currentBankBalance + ". >>> ");
      betAmount = scanner.nextInt();
    }

    currentBankBalance -= betAmount;

    // Game Results
    int diceRollResult = (int)((Math.random() * 5) + 1);
    CoinFlip coinFlipResult = ((int)(Math.random() * 100) % 2 == 0) ? CoinFlip.HEADS : CoinFlip.TAILS;
    Colors colorResult = Colors.values()[(int)((Math.random() * 3) + 1)];

    // Game Choices
    System.out.print("What Is Your Choice On The Dice Roll? (Integer Between 1 and 6 Inclusive) >>> ");
    diceRollChoice = scanner.nextInt();

    System.out.print("What Is Your Choice On The Coin Flip? ('H' For Heads, 'T' For Tails)>>> ");

    coinFlipChoice = switch (scanner.next().toUpperCase().charAt(0)) {
      case 'H' -> CoinFlip.HEADS;
      case 'T' -> CoinFlip.TAILS;
      default -> CoinFlip.NULL;
    };

    System.out.print("What Is Your Choice On The Color Spinner? ('R' For Red, 'G' For Green, 'B' For Blue, 'Y' For Yellow) >>> ");

    colorChoice = switch (scanner.next().toUpperCase().charAt(0)) {
      case 'R' -> Colors.RED;
      case 'G' -> Colors.GREEN;
      case 'B' -> Colors.BLUE;
      case 'Y' -> Colors.YELLOW;
      default -> Colors.NULL;
    };

    // Display Game Results
    System.out.println("You Rolled A " + diceRollResult + ".");
    System.out.println("You Flipped A " + coinFlipResult.label + ".");
    System.out.println("You Spun A " + colorResult.label + ".");

    // Check Choice Accuracy
    ArrayList<GameCategories> correctGameCategories = new ArrayList<>();

    if (diceRollChoice == diceRollResult)
      correctGameCategories.add(GameCategories.DICE_ROLL);
    if (coinFlipChoice.equals(coinFlipResult))
      correctGameCategories.add(GameCategories.COIN_FLIP);
    if (colorChoice.equals(colorResult))
      correctGameCategories.add(GameCategories.COLOR_SPINNER);

    // Display Accuracy Message And Return New Bank Balance
    if (correctGameCategories.size() == 3) {
      System.out.println("Your Choices Corresponded With All Categories");
      return betAmount * 3 + currentBankBalance;
    } else if (correctGameCategories.size() == 2) {
      System.out.println("Your Choices Corresponded With The " + correctGameCategories.get(0).label + " And The " + correctGameCategories.get(1).label + ".");
      return betAmount * 2 + currentBankBalance;
    } else if (correctGameCategories.size() == 1) {
      System.out.println("Your Choices Corresponded Only With The " + correctGameCategories.get(0).label + ".");
      if (correctGameCategories.get(0) == GameCategories.DICE_ROLL)
        return betAmount + currentBankBalance;
      else if (correctGameCategories.get(0) == GameCategories.COIN_FLIP)
        return betAmount * 0.5 + currentBankBalance;
      else if (correctGameCategories.get(0) == GameCategories.COLOR_SPINNER)
        return betAmount * 0.25 + currentBankBalance;
    } else if (correctGameCategories.size() == 0) {
      System.out.println("Your choices corresponded with no categories.");
      return currentBankBalance;
    }

    return 0;
  }

  private static void quit(double currentBankBalance) {
    System.out.println("You left the game with $" + currentBankBalance + ".");
  }
}
