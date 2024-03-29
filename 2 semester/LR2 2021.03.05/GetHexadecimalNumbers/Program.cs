﻿using System;
using System.Linq;

namespace GetHexadecimalNumbers
{
    static class Program
    {
        static void Main(string[] args)
        {
            /* •	Дана строка, слова которой разделены пробелами. Распознать в ней слова,
             являющиеся числами в шестнадцатеричной системе счисления, и вывести их десятичный эквивалент.*/

            var input = Console.ReadLine().Split(new char[] {' '}, StringSplitOptions.RemoveEmptyEntries);
            var hexadecimalsStrings = input.Where(Hexadecimal.DetectHexadecimal).ToList();
            var response = hexadecimalsStrings.Select(Hexadecimal.ConvertToDecimalNumber).ToList();
            response.ForEach(number => Console.Write(number + " "));
        }
    }

    static class Hexadecimal
    {
        private const byte Base = 16;

        private const string Digits = "0123456789",
            Letters = "ABCDEF";

        private static int GetCoefficient(char symbol) => (Digits.Contains(symbol)
            ? symbol - 48
            : Letters.IndexOf(symbol.ToString(), StringComparison.Ordinal) + 10+);
        
        public static bool DetectHexadecimal(string word) =>
            word.ToUpper().All(symbol => Digits.Contains(symbol) || Letters.Contains(symbol));

        public static ulong ConvertToDecimalNumber(string hexadecimalsString)
        {
            ulong response = 0, pow = 1;
            var str = hexadecimalsString.ToUpper().ToCharArray().Reverse();

            foreach (var symbol in str)
            {
                response += (ulong) GetCoefficient(symbol) * pow;
                pow *= Base;
            }

            return response;
        }
    }
}