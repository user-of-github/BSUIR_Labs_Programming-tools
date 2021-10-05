using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using LR_053506_Slutski_Lab8.Entities;

namespace LR_053506_Slutski_Lab8
{
    internal static class Program
    {
        private static void Main()
        {
            var session = new FileService();

            var employedByDailyBugle = GetDefaultEmployeesPack();
            var (firstFileName, secondFileName) =
                (GetRandomStringFileName(), GetRandomStringFileName());

            Console.WriteLine(firstFileName);
            Console.WriteLine(secondFileName);

            session.SaveData(employedByDailyBugle, firstFileName);

            File.Move(firstFileName, secondFileName);

            var testReading = session.ReadFile(secondFileName).ToList();
            testReading.Sort(new EmployeeComparer());
            testReading.ForEach(Console.WriteLine);
        }


        #region GetDefaultEmployeesPack()

        private static IEnumerable<Employee> GetDefaultEmployeesPack() => new[]
        {
            new Employee("Peter Parker", 300, true),
            new Employee("Eddie Brock", 300, true),
            new Employee("John Jonah Jameson Jr.", 1000, false),
            new Employee("Robbie Robertson", 500, false),
            new Employee("Betty Brant", 650, false)
        };

        #endregion

        #region GetRandomStringFileName

        private static string GetRandomStringFileName() =>
            new string(Enumerable
                .Repeat("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", new Random().Next(7, 10))
                .Select(s => s[new Random().Next(s.Length)]).ToArray()) + ".txt";

        #endregion
    }
}