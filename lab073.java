package scratch;

import java.util.AbstractMap;
import java.util.Scanner;

public class Scratch {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);

    final int SALESPEOPLE = 5; // number of salespeople
    int[] sales = new int[SALESPEOPLE]; // stores the sale of each salesperson.
    int sum = 0; // stores the total of all the sales

    // input the sale of each salesperson into `sales`
    var maxSale = new AbstractMap.SimpleEntry<>(0, 0); // 2. store the max sale
    var minSale = new AbstractMap.SimpleEntry<>(0, 0); // 3. store the min sale
    for (int i = 0; i < sales.length; i++) {
      System.out.print("Enter sales for salesperson " + i + ": ");
      sales[i] = scan.nextInt();

      // 2. Find the max sale
      if (sales[i] > maxSale.getValue()) {
        maxSale = new AbstractMap.SimpleEntry<>(i, sales[i]);
      } else if (sales[i] < minSale.getValue()) {
        minSale = new AbstractMap.SimpleEntry<>(i, sales[i]);
      }
    }

    // print out the sales and increment `sum`
    System.out.println("\nSalesperson Sales");
    for (int i = 0; i < sales.length; i++) {
      System.out.println("" + i + " => " + sales[i]);
      sum += sales[i];
    }

    // 2. print max sale
    System.out.println("Salesperson " + maxSale.getKey() + " had the highest sale of $" + maxSale.getValue());
    // 3. print min sale
    System.out.println("Salesperson " + maxSale.getKey() + " had the lowest sale of $" + minSale.getValue());

    // print total sales
    System.out.println("\nTotal Sales " + sum);

    // 1. calculate average sale
    double averageSale = (double)sum / SALESPEOPLE;
  }
}

