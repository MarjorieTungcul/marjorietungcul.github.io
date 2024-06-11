using System

class Calculator
{
    public double Add(double num1, double num2)
    {
        return num1 + num2;
    }

    public double Subtract(double num1, double num2)
    {
        return num1 - num2;
    }

    public double Multiply(double num1, double num2)
    {
        return num1 * num2;
    }

    public double Divide(double num1, double num2)
    {
        if (num2 == 0)
        {
            Console.WriteLine("It cannot be divided by zero!");
            return 0;
        }
        else
        {
            return num1 / num2;
        }
    }
    
    public string Odd_num(double num)
    {
        if (num % 2 != 0)
        {
            return $"{num} is an odd number.";
        }
        else
        {
            return $"{num} is not an odd number.";
        }
    }
    
    public string Even_num(double num)
    {
        if (num % 2 == 0)
        {
            return $"{num} is an even number.";
        }
        else
        {
            return $"{num} is not an even number.";
        }
    }
}

class Program
{
    static void Main()
    {
        Calculator mycalculator = new Calculator();
        
        while (true)
        {
            Console.WriteLine("\nHere are the 7 features of this calculator:");
            Console.WriteLine("1. Add Two Numbers\n2. Subtract Two Numbers\n3. Multiply Two Numbers\n4. Divide Two Numbers");
            Console.WriteLine("5. Check if a Number is Odd\n6. Check if a Number is Even\n7. Exit the Application");
            Console.WriteLine();
            Console.Write("Please choose a command you want to execute (1-7): ");
            
            int command;
            if (int.TryParse(Console.ReadLine(), out command))
            {
                switch (command)
                {
                    case 1:
                        Console.Write("Enter the first number: ");
                        double add_num1 = Convert.ToDouble(Console.ReadLine());
                        Console.Write("Enter the second number: ");
                        double add_num2 = Convert.ToDouble(Console.ReadLine());
                        double sum = mycalculator.Add(add_num1, add_num2);
                        Console.WriteLine($"The sum of the two numbers is {sum}.");
                        break;
                    case 2:
                        Console.Write("Enter the minuend number: ");
                        double subtract_num1 = Convert.ToDouble(Console.ReadLine());
                        Console.Write("Enter the subtrahend number: ");
                        double subtract_num2 = Convert.ToDouble(Console.ReadLine());
                        double difference = mycalculator.Subtract(subtract_num1, subtract_num2);
                        Console.WriteLine($"The difference of the two numbers is {difference}.");
                        break;
                    case 3:
                        Console.Write("Enter the multiplicand number: ");
                        double multiply_num1 = Convert.ToDouble(Console.ReadLine());
                        Console.Write("Enter the multiplier number: ");
                        double multiply_num2 = Convert.ToDouble(Console.ReadLine());
                        double product = mycalculator.Multiply(multiply_num1, multiply_num2);
                        Console.WriteLine($"The product of the two numbers is {product}.");
                        break;
                    case 4:
                        Console.Write("Enter dividend: ");
                        double divide_num1 = Convert.ToDouble(Console.ReadLine());
                        Console.Write("Enter divisor: ");
                        double divide_num2 = Convert.ToDouble(Console.ReadLine());
                        double quotient = mycalculator.Divide(divide_num1, divide_num2);
                        Console.WriteLine($"The quotient of the two numbers is {quotient}.");
                        break;
                    case 5:
                        Console.Write("Enter a number you want to check: ");
                        double odd_num = Convert.ToDouble(Console.ReadLine());
                        string odd_result = mycalculator.Odd_num(odd_num);
                        Console.WriteLine(odd_result);
                        break;
                    case 6:
                        Console.Write("Enter a number you want to check: ");
                        double even_num = Convert.ToDouble(Console.ReadLine());
                        string even_result = mycalculator.Even_num(even_num);
                        Console.WriteLine(even_result);
                        break;
                    case 7:
                        Console.WriteLine("Thank you for using our Calculator!");
                        return;
                    default:
                        Console.WriteLine("Invalid choice. Please select a valid command.");
                        break;
                }
            }
            else
            {
                Console.WriteLine("Invalid input. Please enter a number that corresponds to the command.");
            }
        }
    }
}
