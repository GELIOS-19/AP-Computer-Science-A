package labs.control_structures.iteration;

import java.util.Scanner;

public class Lab08 {

  public static void main(String[] args) {
    // Constants
    final Scanner scanner = new Scanner(System.in);
    final char[] colorChoices = {'R', 'G', 'B', 'Y'};

    // Program Results
    int diceResult = (int)((Math.random() * 5) + 1);
    char coinResult = (int)(Math.random() * 100) % 2 == 0 ? 'H' : 'T';  // Checking for even numbers produces a more variable output
    char colorResult = colorChoices[(int)((Math.random() * 3) + 1)];

    // Introduction
    System.out.print("Welcome to the Game of Chance.\nLet's see if you won.\n");

    // User Input
    System.out.print("What is your guess on the dice roll? (Integer between 1 and 6) ");
    int diceChoice = scanner.nextInt();
    System.out.print("What is your guess on the coin flip? ('H' for Heads, 'T' for Tails) ");
    char coinChoice = scanner.next().replace("\u0020", "").charAt(0);
    System.out.print("What is your guess on the spinner? ('R' for Red, 'G' for Green, 'B' for Blue, 'Y' for Yellow) ");
    char colorChoice = scanner.next().replace("\u0020", "").charAt(0);

    // Print results
    System.out.println("\nYou rolled a " + diceResult);
    System.out.println("You flipped a " + coinResult);
    System.out.println("You spun a " + colorResult);

    // Print output
    final String defaultOutput = "\nYou guessed ";
    String output = defaultOutput;

    if (diceChoice == diceResult) {
      output += "the dice roll";
    }

    if (coinChoice ==  coinResult) {
      if (!output.equals(defaultOutput)) output += ", and ";
      output += "the coin flip";
    }

    if (colorChoice == colorResult) {
      if (!output.equals(defaultOutput)) output += ", and ";
      output += "the color spin";
    }

    if (output.equals(defaultOutput)) output += "nothing correctly.";
    else output += " correctly";

    System.out.println(output);
  }
}
