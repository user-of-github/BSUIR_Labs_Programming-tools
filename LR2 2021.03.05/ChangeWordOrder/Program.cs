using System;
using System.Collections.Generic;
using System.Linq;

namespace ChangeWordOrder
{
    internal static class Program
    {
        private static void Main(string[] args)
        {
            /* •	В заданной строке поменять порядок слов на обратный (слова разделены пробела-ми). */

            var input = Console.ReadLine();

            var response = string.Join(' ',
                input.Split(new char[] {' '}, StringSplitOptions.RemoveEmptyEntries).ToArray().Reverse());

            Console.WriteLine(response);
        }
    }
}