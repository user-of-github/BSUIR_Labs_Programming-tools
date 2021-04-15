using System;

namespace LR6_2021._04._08
{
    internal sealed class Laptop : MobileDevice
    {
        private byte ScreenFrequency { get; set; }

        public Laptop(uint cost, string[] cpuInfo, string[] memoryInfo, string os, uint weight,
            byte screenFrequency) : base(cost,
            cpuInfo, memoryInfo, os, weight) => this.ScreenFrequency = screenFrequency;
        
        public override void PrintInfo()
        {
            Console.WriteLine("_______________________");
            Console.WriteLine("Laptop:");
            base.PrintInfo();
            Console.WriteLine($"Frequency of Updating the screen is : {this.ScreenFrequency} Hz");
            Console.WriteLine("_______________________");
        }
    }
}