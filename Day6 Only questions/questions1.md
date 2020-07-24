
## Exercises
### Triangles

1. **Easiest**

    Print one asterisk to the console.

    Example:
    ```
    *
    ```

2. **Draw a horizontal line**

    Given a number n, print n asterisks on one line.
    
    Example when n=8:
    ```
    ********
    ```

3. **Draw a vertical line**

    Given a number n, print n lines, each with one asterisks.
    
    Example when n=3:
    ```
    *
    *
    *
    ```

4. **Draw a right triangle**

    Given a number n, print n lines, each with one more asterisk than the last (i.e. one on the first line, two on the second,etc.) 
    
    Example when n=3:
    ```
    *
    **
    ***
    ```

### Diamonds

5. **Isosceles triangle**

    Given a number n, print a centered triangle. 
    
    Example for n=3:
    ```
      *
     ***
    *****
    ```

6. **Diamond**

    Given a number n, print a centered diamond. 
    
    Example for n=3:
    
    ```
      *
     ***
    *****
     ***
      *
    ```


7.
### FizzBuzz
FizzBuzz is a simple number game where you count, but say "Fizz" and/or "Buzz" instead of numbers adhering to certain rules.

Create a FizzBuzz() method that prints out the numbers 1 through 100.
Instead of numbers divisible by three print "Fizz".
Instead of numbers divisible by five print "Buzz".
Instead of numbers divisible by three and five print "FizzBuzz".

Sample Output:
```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
```

8. ### Prime Factors
Write a method generate(int n) that given an integer N will return a list of integers such that the numbers are the factors of N and are arranged in increasing numerical order.

For example, generate(1) should return an empty list and generate(30) should return the numbers: 2,3,5.
