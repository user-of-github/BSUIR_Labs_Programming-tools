using System;
using System.Collections.Generic;
using System.Linq;
using fileService;

namespace ConsoleApp1
{
    internal class Program
    {
        static void Main()
        {
            List<Employee> defaultEmployees = GetDefaultEmployeesPack();

            Console.WriteLine("Default pack: ".ToUpper());
            defaultEmployees.ForEach((Employee item) => Console.WriteLine($"\t{item}"));

            FileService<Employee> test = new();

            test.SaveData(defaultEmployees, "test.json");

            List<Employee> writtenEmployees = test.ReadFile("test.json").ToList();

            Console.WriteLine("\n\nWritten pack: ".ToUpper());
            writtenEmployees.ForEach((Employee item) => Console.WriteLine($"\t{item}"));
        }

        private static List<Employee> GetDefaultEmployeesPack() => (new[]
        {
            new Employee("Slutski", 18, true),
            new Employee("Levankov", 18, false),
            new Employee("Bondarkov", 18, false)
        }).ToList();
    }

    public class Employee
    {
        public const string VacationText = "On vacation";
        public const string WorkText = "Working";
        public string Name { get; set; }

        public byte Age { get; set; }

        public bool OnVacationNow { get; set; }

        public Employee() { }

        public Employee(string name, byte age) => 
            (Name, Age, OnVacationNow) = (name, age, false);

        public Employee(string name, byte age, bool onVacationNow) => 
            (Name, Age, OnVacationNow) = (name, age, onVacationNow);

        public override string ToString() => $"{Name} | {Age} years | {(OnVacationNow == true ? VacationText : WorkText)}";
    }

  
}
