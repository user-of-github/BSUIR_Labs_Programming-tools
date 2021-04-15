using System;

namespace LR7_2021._04._15
{
    internal static class Program
    {
        private static void Main()
        {
            RationalNumber example = new RationalNumber(123, 12300);
            Console.Write(example); // output: 123 / 12300
            Console.Write(example.GetShortenFraction()); // output: 1 / 100

            RationalNumber example2 = new RationalNumber(" 3 / 200");
            Console.Write((example + example2).GetShortenFraction()); // output: 1 / 40

            Console.WriteLine(example * example2); // output: 3 / 20000

            RationalNumber division = example / example2;
            Console.WriteLine(division); // output: 2 / 3

            Console.WriteLine(division * 4); // output: 8 / 3
            Console.WriteLine(division / 10); // output: 1 / 15

            Console.WriteLine(division > example); // output: True
        }
    }
}