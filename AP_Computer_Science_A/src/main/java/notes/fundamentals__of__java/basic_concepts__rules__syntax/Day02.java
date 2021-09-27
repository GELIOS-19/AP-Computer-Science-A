package notes.fundamentals__of__java.basic_concepts__rules__syntax;

public class Day02 {

  public static void main(String[] args) {
    //////////////////////////////////////////////////
    // ESCAPE SEQUENCES
    //////////////////////////////////////////////////

    // Double Quotations    -    \"
    // Single Quotations    -    \'
    // Tab                  -    \t
    // New Line             -    \n
    // Backslash            -    \\

    System.out.println("\"Hello\t\tWorld\"\nHello Again\\");
    System.out.println("\\/\'");

    //////////////////////////////////////////////////
    // PRINTING INTEGERS AND DECIMALS (double)
    //////////////////////////////////////////////////

    // quotations are not necessary to print numeric values
    System.out.println("42"); // 42 is treated as a String
    System.out.println(42);   // 42 is treated as an Integer
    System.out.println(4.2);  // 4.2 is treated as a Double

    //////////////////////////////////////////////////
    // CONCATENATION - Combine (Concatenation Operator is +)
    //////////////////////////////////////////////////

    System.out.println("My name is " + "Arjun");
    System.out.println("My favorite number is " + 9);
  }
}
