 class Polynomial {
  private
   int degree;
  private
   int numberOfTerms;
 
  public
   Polynomial(int degree, int numberOfTerms) {
     this.degree = degree >= 0 ? degree : 0;
     this.numberOfTerms = numberOfTerms;
   }
 
  public
   int getDegree() { return degree; }
 
  public
   int getNumberOfTerms() { return numberOfTerms; }
 
  public
   String toString() {
     return String.format("There are %d terms and a degree of %d", numberOfTerms,
                          degree);
   }
 
  public
   boolean equals(Polynomial other) {
     return degree == other.degree && numberOfTerms == other.numberOfTerms;
   }
 }
 
 class Trinomial extends Polynomial {
  private
   int leadCoefficient;
  private
   int middleCoefficient;
  private
   int lastCoefficient;
 
  public
   Trinomial(int degree, int leadCoefficient, int middleCoefficient,
             int lastCoefficient) {
     super(degree, 3);
     this.leadCoefficient = leadCoefficient;
     this.middleCoefficient = middleCoefficient;
     this.lastCoefficient = lastCoefficient;
   }
 
  public
   int getLeadCoefficient() { return leadCoefficient; }
 
  public
   int getMiddleCoefficient() { return middleCoefficient; }
 
  public
   int getLastCoefficient() { return lastCoefficient; }
 
  public
   String toString() {
     return String.format("%s\nThis trinomial has coefficients of %d %d %d",
                          super.toString(), leadCoefficient, middleCoefficient,
                          lastCoefficient);
   }
 
  public
   boolean equals(Trinomial other) {
     return super.equals(other) && leadCoefficient == other.leadCoefficient &&
            middleCoefficient == other.middleCoefficient &&
            lastCoefficient == other.lastCoefficient;
   }
 }
 
 class Quadratic extends Trinomial {
  private
   double discriminant;
 
  public
   Quadratic(int a, int b, int c) {
     super(2, a, b, c);
     discriminant = Math.pow(b, 2) - 4 * a * c;
     System.out.println("The discriminant is " + discriminant);
   }
 
  public
   double getDiscriminant() { return discriminant; }
 
  public
   String toString() {
     return String.format("%s\n%dx^2 + %dx + %d\n", super.toString(),
                          getLeadCoefficient(), getMiddleCoefficient(),
                          getLastCoefficient());
   }
 
  public
   boolean equals(Quadratic other) { return super.equals(other); }
 
  public
   boolean hasRealSolutions() { return discriminant >= 0; }
 
  public
   double firstZero() {
     return (double)(-getMiddleCoefficient() + Math.sqrt(discriminant)) /
            (double)(2 * getLeadCoefficient());
   }
 
  public
   double secondZero() {
     return (double)(-getMiddleCoefficient() - Math.sqrt(discriminant)) /
            (double)(2 * getLeadCoefficient());
   }
 
  public
   boolean isPerfectSquare() { return discriminant == 0; }
 }
 
 public class tempCodeRunnerFile {
  public
   static void main(String[] args) {
     // DO NOT MODIFY ANYTHING IN THE MAIN CLASS / METHOD
     Polynomial polly = new Polynomial(5, 7);
     System.out.println(polly);
 
     Trinomial trinity = new Trinomial(4, 3, -5, 1);
     System.out.println(trinity);
 
     Quadratic quinn = new Quadratic(2, 5, -3);
     System.out.println(quinn);
 
     Polynomial pollySister = new Polynomial(5, 7);
     System.out.println(polly.equals(pollySister));
 
     Trinomial trinityBrother = new Trinomial(4, 3, -5, 1);
     System.out.println(trinity.equals(trinityBrother));
 
     Quadratic quinnSister = new Quadratic(2, 5, -3);
     System.out.println(quinn.equals(quinnSister));
     System.out.println(quinn == quinnSister);
 
     System.out.println(quinn.hasRealSolutions());
     System.out.println(quinn.firstZero());
     System.out.println(quinn.secondZero());
     System.out.println(quinn.isPerfectSquare());
 
     Quadratic quinton = new Quadratic(9, 12, 4);
     System.out.println(quinton.isPerfectSquare());
   }
 }
