using System;
using System.Linq;

namespace LR3_2021._03._18
{
    internal static class Program
    {
        private static void Main()
        {
            const string filePath = "data.txt";
            var data = Computer.LoadFromDataBaseFile(filePath).ToList();

            data.ForEach(sample =>
                Console.WriteLine(
                    $"{sample.Type}: {sample.Ram}GB RAM, {sample.Rom}GB ROM, OS:{sample.OperatingSystem} Cost: {sample.Cost}$"));
        }
    }
}