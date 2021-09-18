using System;

namespace LR8_2021._04._29
{
    internal static class Program
    {
        private static void Main()
        {
            Smartphone huaweiHonor10 = new Smartphone(600, new[] {"Hisilicon", "Kirin 970"}, new[] {"128", "6"},
                "Android 10", 150, true);

            huaweiHonor10.OnNewOwner += data => huaweiHonor10.Owners.Add(data);

            huaweiHonor10.AddNewOwner("Nikita Slutski");
            huaweiHonor10.AddNewOwner("Second owner");

            Console.WriteLine("Owners list:");
            huaweiHonor10.Owners.ForEach(owner => Console.WriteLine(owner));
            // 
            // Owners list:
            // Nikita Slutski
            // Second owner

            Laptop asusTufGaming = new Laptop(2700, new string[] {"AMD", "Ryzen 7 4800H"}, new string[] {"512", "8"},
                "Windows 10", 2000,
                144);

            asusTufGaming.OnGettingId += () => Console.WriteLine(asusTufGaming.Id);

            asusTufGaming.GetIdentificator();
            // G4btuJZ8hA
        }
    }
}