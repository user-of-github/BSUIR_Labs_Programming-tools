using System;

namespace LR8_2021._04._29
{
    internal sealed class Desktop : DesktopDevice
    {
        private byte PowerSupplyUnitPower { get; }

        public Desktop(uint cost, string[] cpuInfo, string[] memoryInfo, string os, byte numberOfComponents,
            byte powerSupplyUnitPower) :
            base(cost, cpuInfo, memoryInfo, os, numberOfComponents) => PowerSupplyUnitPower = powerSupplyUnitPower;

        public override void PrintInfo()
        {
            Console.WriteLine("_______________________");
            Console.WriteLine("Desktop:");
            base.PrintInfo();
            Console.WriteLine($"Power of power supply unit: {PowerSupplyUnitPower}");
            Console.WriteLine("_______________________");
        }
    }
}