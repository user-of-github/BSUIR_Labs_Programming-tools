using System;
using System.Collections.Generic;

namespace LR8_2021._04._29
{
    internal abstract class MobileDevice : Computer
    {
        private uint Weight { get; set; }

        public MobileDevice(uint cost, string[] cpuInfo, IReadOnlyList<string> memoryInfo, string os, uint weight) :
            base(cost,
                cpuInfo, memoryInfo, os) => Weight = weight;

        public override void PrintInfo()
        {
            base.PrintInfo();
            Console.WriteLine($"Weight is : {Weight} G");
        }
    }
}