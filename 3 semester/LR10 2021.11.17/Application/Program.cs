using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;

namespace Application
{
    internal class Program
    {
        static void Main() => RunDemo(GetDefaultEmployeesPack(), "test.json");

        static void RunDemo(List<Employee> defaultEmployees, string FileName)
        {
            Console.WriteLine("Default pack: ".ToUpper());
            defaultEmployees.ForEach((Employee item) => Console.WriteLine($"\t{item}"));

            var asm = Assembly.LoadFrom("../../../fileService.dll");

            var FileServiceEmployee = asm.GetType("FileService.FileService`1")
                                        .MakeGenericType(typeof(Employee));//[0]; // raw type
            //var FileServiceEmployee = RawType.MakeGenericType(typeof(Employee)); // made generic and assigned for Employee
            var fileServicer = Activator.CreateInstance(FileServiceEmployee);


            MethodInfo FileServiceEmployeeReadFileMethod = FileServiceEmployee.GetMethod("ReadFile");
            MethodInfo FileServiceEmployeeSaveFileMethod = FileServiceEmployee.GetMethod("SaveData");

            FileServiceEmployeeSaveFileMethod.Invoke(fileServicer, new object[] { defaultEmployees, FileName });

            var dataReadFromFile = (List<Employee>)FileServiceEmployeeReadFileMethod.Invoke(fileServicer, new object[] { FileName });

            Console.WriteLine("\n\nWritten pack: ".ToUpper());
            dataReadFromFile.ForEach((Employee item) => Console.WriteLine($"\t{item}"));
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

        public override string ToString() =>
            $"{Name} | {Age} years | {(OnVacationNow == true ? VacationText : WorkText)}";
    }
}