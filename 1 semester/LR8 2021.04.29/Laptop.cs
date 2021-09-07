using System;

namespace LR8_2021._04._29
{
    internal sealed class Laptop : MobileDevice
    {
        private byte ScreenFrequency { get; set; }

        public Laptop(uint cost, string[] cpuInfo, string[] memoryInfo, string os, uint weight,
            byte screenFrequency) : base(cost,
            cpuInfo, memoryInfo, os, weight) => ScreenFrequency = screenFrequency;

        public override void PrintInfo()
        {
            Console.WriteLine("_______________________");
            Console.WriteLine("Laptop:");
            base.PrintInfo();
            Console.WriteLine($"Frequency of Updating the screen is : {ScreenFrequency} Hz");
            Console.WriteLine("_______________________");
        }
    }
}