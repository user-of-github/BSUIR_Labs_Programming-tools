using System;

namespace LR6_2021._04._08
{
    internal static class Program
    {
        private static void Main(string[] args)
        {
            Laptop someonesLaptop = new Laptop(2700, new string[] {"AMD", "Ryzen 7 4800H"}, new string[] {"512", "8"},
                "Windows 10", 2000,
                144);

            someonesLaptop.PrintInfo();
            /* Laptop:
            OS: Windows 10
            Cost: 2700 BYN
            Vendor of CPU: Amd
            Weight is : 2000 G
            Frequency of Updating the screen is : 144 Hz */

            Smartphone neighboursSmartphone = new Smartphone(600, new string[] {"Qualcomm", "Snapdragon 768"},
                new string[] {"128", "6"},
                "Android 11", 150,
                true);

            neighboursSmartphone.PrintInfo();
            /* Smartphone:
                OS: Android 11
                Cost: 600 BYN
                Vendor of CPU: Qualcomm
                Weight is : 150 G
                Has infrared port*/

            Console.WriteLine(neighboursSmartphone.CompareTo(someonesLaptop) == 1
                ? "Smartphone is more expensive"
                : (neighboursSmartphone.CompareTo(someonesLaptop) == 0 ? "The same price" : "Laptop is more expensive"));
            // Laptop is more expensive

            neighboursSmartphone.Cost = 3000;
            
            Console.WriteLine(neighboursSmartphone.CompareTo(someonesLaptop) == 1
                ? "Smartphone is more expensive"
                : (neighboursSmartphone.CompareTo(someonesLaptop) == 0 ? "The same price" : "Laptop is more expensive"));
            // Smartphone is more expensive

        }
    }
}