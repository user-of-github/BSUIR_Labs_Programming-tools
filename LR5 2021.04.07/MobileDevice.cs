using System;

namespace LR5_2021._04._07
{
    internal abstract class MobileDevice : Computer
    {
        private uint Weight { get; set; }

        public MobileDevice(uint cost, string[] cpuInfo, string[] memoryInfo, string os, uint weight) : base(cost,
            cpuInfo, memoryInfo, os) => this.Weight = weight;

        public override void PrintInfo()
        {
            base.PrintInfo();
            Console.WriteLine($"Weight is : {this.Weight} KG");
        }
    }
}