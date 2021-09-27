package notes.fundamentals__of__java.variables__assignment;

public class Day03 {

  public static void main(String[] args) {
    //////////////////////////////////////////////////
    // VARIABLES
    //////////////////////////////////////////////////

    // Variables allow us to store data in memory
    // Primitive Data Types: boolean, char, double, int
    // boolean    -   1-Bit     -   Stores true or false
    // char       -   16-Bits   -   Stores a single character
    // int        -   32-Bits   -   Stores an integer
    // double     -   64-Bits   -   Stores a number with a decimal

    //////////////////////////////////////////////////
    // VARIABLE DECLARATIONS - Create / Allocate space in memory
    //////////////////////////////////////////////////

    // Convention for naming variables: Begin with a lowercase letter then use camelCase
    boolean myBoolean;  // 1-Bit of memory has been allocated for `myBoolean`.
    char myChar;        // 16-Bits of memory has been allocated for `myChar`.
    int myInt;          // 32-Bits of memory has been allocated for `myInt`.
    double myDouble;    // 64-Bits of memory has been allocated for `myDouble`.

    //////////////////////////////////////////////////
    // ASSIGNMENT STATEMENTS - The equal sign ( = ) is the assignment operator.
    //////////////////////////////////////////////////

    myBoolean = true;
    myChar = '%';       // Characters are enclosed in single quotations.
    myChar = '\'';      // Still need to apply escape sequences.
    myInt = 57;
    myDouble = 1.23;

    System.out.println("The value of `myDouble` is " + myDouble + ".");
    myDouble = 19;  // This will be stored in memory as 19.0.
    System.out.println("The value of `myDouble` is " + myDouble + ".");

    //////////////////////////////////////////////////
    // VARIABLE DECLARATIONS WITH INITIALIZATION - Declare and Assign on one line
    //////////////////////////////////////////////////

    // All variables should be initialized
    int cookie = 26;
    double jellyDonut = 5.67;

    //////////////////////////////////////////////////
    // MULTIPLE DECLARATIONS / INITIALIZATIONS - Declare and Assign multiple variables on one line
    //////////////////////////////////////////////////

    int i1, i2, i3, i4, i5;         // Declares 5 int variables
    double d1 = 1.2, d2, d3 = 3.4;  // Declares 3 double variables, initializes 2 of them
  }
}
