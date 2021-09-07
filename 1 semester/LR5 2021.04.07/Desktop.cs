using System;

namespace LR5_2021._04._07
{
    internal sealed class Desktop : DesktopDevice
    {
        private byte PowerSupplyUnitPower { get; set; }

        public Desktop(uint cost, string[] cpuInfo, string[] memoryInfo, string os, byte numberOfComponents,
            byte powerSupplyUnitPower) :
            base(cost, cpuInfo, memoryInfo, os, numberOfComponents) => this.PowerSupplyUnitPower = powerSupplyUnitPower;

        public override void PrintInfo()
        {
            Console.WriteLine("_______________________");
            Console.WriteLine("Desktop:");
            base.PrintInfo();
            Console.WriteLine($"Power of power supply unit: {this.PowerSupplyUnitPower}");
            Console.WriteLine("_______________________");
        }
    }
}