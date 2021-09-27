package scratch;

import java.util.*;

public class Scratch {

  public static void main(String[] args) {
    ArrayList<Double> sequence = fibonacciSequence(10);
    sequence.forEach(System.out::println);
    System.out.println(sequence.size());
  }

  /**
   * Generates an ArrayList containing numbers of the fibonacci sequence of size `size`.
   *
   * @param size The size of the generated ArrayList
   * @return ArrayList of size `size` containing numbers of the fibonacci sequence
   */
  private static ArrayList<Double> fibonacciSequence(int size) {
    double numberA = 1d;
    double numberB = 2d;
    ArrayList<Double> sequence = new ArrayList<>(List.of(numberA, numberB));

    for (int count = 0; count < size - 2; count++) {
      double numberC = numberA + numberB;
      sequence.add(numberC);
      numberA = numberB;
      numberB = numberC;
    }

    return sequence;
  }
}
