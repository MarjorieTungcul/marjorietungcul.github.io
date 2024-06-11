using System;

public class Converter
{
    private double _kilometers, _miles, _celsius, _fahrenheit, _usd, _php;

    public double Kilometers
    {
        get { return _kilometers; }
        set { _kilometers = value; }
    }

    public double Miles
    {
        get { return _miles; }
        set { _miles = value; }
    }

    public double Celsius
    {
        get { return _celsius; }
        set { _celsius = value; }
    }

    public double Fahrenheit
    {
        get { return _fahrenheit; }
        set { _fahrenheit = value; }
    }

    public double USD
    {
        get { return _usd; }
        set { _usd = value; }
    }

    public double PHP
    {
        get { return _php; }
        set { _php = value; }
    }

    public double MilesToKilometers(double miles)
    {
        return miles * 1.60934;
    }

    public double KilometersToMiles(double kilometers)
    {
        return kilometers / 1.60934;
    }

    public double CelsiusToFahrenheit(double celsius)
    {
        return celsius * 9 / 5 + 32;
    }

    public double FahrenheitToCelsius(double fahrenheit)
    {
        return (fahrenheit - 32) * 5 / 9;
    }

    public double USDToPhilippinePesos(double usd)
    {
        return usd * 56.21;
    }

    public double PhilippinePesosToUSD(double php)
    {
        return php / 56.21;
    }
}

class Program
{
    static void Main(string[] args)
    {
        Converter converter = new Converter();
        double input;

        while (true)
        {
            Console.WriteLine("\n1. Kilometers to Miles Conversion");
            Console.WriteLine("2. Miles to Kilometers Conversion");
            Console.WriteLine("3. Celsius to Fahrenheit Conversion");
            Console.WriteLine("4. Fahrenheit to Celsius Conversion");
            Console.WriteLine("5. USD to Philippine Pesos Conversion");
            Console.WriteLine("6. Philippine Pesos to USD Conversion");
            Console.WriteLine("7. Exit");
            Console.Write("Choose a type of Conversion (1-7): ");
            int choice = int.Parse(Console.ReadLine());

            switch (choice)
            {
                case 1:
                    Console.Write("Enter the number of kilometers: ");
                    input = Convert.ToDouble(Console.ReadLine());
                    Console.WriteLine($"Miles: {converter.KilometersToMiles(input)}");
                    break;

                case 2:
                    Console.Write("Enter the number of miles: ");
                    input = Convert.ToDouble(Console.ReadLine());
                    Console.WriteLine($"Kilometers: {converter.MilesToKilometers(input)}");
                    break;

                case 3:
                    Console.Write("Enter the temperature in Celsius: ");
                    input = Convert.ToDouble(Console.ReadLine());
                    Console.WriteLine($"Fahrenheit: {converter.CelsiusToFahrenheit(input)}");
                    break;

                case 4:
                    Console.Write("Enter the temperature in Fahrenheit: ");
                    input = Convert.ToDouble(Console.ReadLine());
                    Console.WriteLine($"Celsius: {converter.FahrenheitToCelsius(input)}");
                    break;

                case 5:
                    Console.Write("Enter the amount in USD: ");
                    input = Convert.ToDouble(Console.ReadLine());
                    Console.WriteLine($"Philippine Pesos: {converter.USDToPhilippinePesos(input)}");
                    break;

                case 6:
                    Console.Write("Enter the amount in Philippine Pesos: ");
                    input = Convert.ToDouble(Console.ReadLine());
                    Console.WriteLine($"USD: {converter.PhilippinePesosToUSD(input)}");
                    break;

                case 7:
                    Environment.Exit(0);
                    break;

                default:
                    Console.WriteLine("Invalid choice. Please try again.");
                    break;
            }
        }
    }
}
