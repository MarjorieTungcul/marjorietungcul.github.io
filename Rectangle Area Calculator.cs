using System;

public class MultiplicationTableProgram
{
    public static void Main(string[] args)
    {
        Console.Write("Multiples of:");
        int number = Convert.ToInt32(Console.ReadLine());

        for (int iteration = 1; iteration < 11; iteration++)
        {
            Console.WriteLine("{0} x {1} = {2}\n", number, iteration, number * iteration);
        }
    }
}
