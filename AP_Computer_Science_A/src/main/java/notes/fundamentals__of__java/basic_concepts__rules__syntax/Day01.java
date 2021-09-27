package notes.fundamentals__of__java.basic_concepts__rules__syntax;

public class Day01 {

  public static void main(String[] args) {
    ////////////////////////////////////////////////////
    // COMMENTS
    ////////////////////////////////////////////////////

    // This is a single-line comment
    // This is another single-line comment

    /* This
     * is
     * a
     * multi-line
     * comment
     * */

    ////////////////////////////////////////////////////
    // IDENTIFIER NAMING CONVENTIONS
    ////////////////////////////////////////////////////

    // Camel Case: Capitalize the first letter of each new word
    // Camel Case Example: CamelCase or camelCase

    // Class Names: Begin with a capital letter then follow camel case
    // Methods & Variables: Begin with a lowercase letter then follow camel case
    // Constants: All capital letters; separate words using the underscore

    ////////////////////////////////////////////////////
    // PRINT vs PRINTLN
    ////////////////////////////////////////////////////

    // println moves the cursor to the next line after it prints
    System.out.println("Print #1");

    // print does not move the cursor to the next line after it prints
    System.out.print("Print #2");
    System.out.print("Print #3");
    // notice that "Print #3" is on the same line as "Print #2"
  }
}
