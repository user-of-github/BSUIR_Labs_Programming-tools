using System;

namespace LR6_2021._04._08
{
    internal abstract class DesktopDevice : Computer
    {
        private byte NumberOfComponents { get; set; }

        public DesktopDevice(uint cost, string[] cpuInfo, string[] memoryInfo, string os, byte numberOfComponents) :
            base(cost, cpuInfo, memoryInfo, os) => this.NumberOfComponents = numberOfComponents;

        public override void PrintInfo()
        {
            base.PrintInfo();
            Console.WriteLine($"Number of components in this DesktopDevice: {this.NumberOfComponents}");
        }
    }
}