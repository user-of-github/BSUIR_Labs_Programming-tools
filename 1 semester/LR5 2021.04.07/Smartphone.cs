using System;

namespace LR5_2021._04._07
{
    internal sealed class Smartphone : MobileDevice
    {
        private bool HasInfraredPort { get; set; }
        
        public Smartphone(uint cost, string[] cpuInfo, string[] memoryInfo, string os, uint weight, bool hasPort) : base(cost,
            cpuInfo, memoryInfo, os, weight) => this.HasInfraredPort = hasPort;

        public override void PrintInfo()
        {
            Console.WriteLine("_______________________");
            Console.WriteLine("Smartphone:");
            base.PrintInfo();
            Console.Write(this.HasInfraredPort ? "Has" : "Doesn't have");
            Console.WriteLine(" infrared port");
            Console.WriteLine("_______________________");
        }
    }
}