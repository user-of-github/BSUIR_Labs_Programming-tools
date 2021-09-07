using System;
using System.Collections.Generic;

namespace LR6_2021._04._08
{
    internal class Computer : Gadget, IInformation, IGadget
    {
        private const string Currency = "BYN";
        private uint Ram { get; set; }
        private string OperatingSystem { get; set; }

        private struct Cpu
        {
            internal enum Vendors
            {
                Amd,
                Qualcomm,
                Intel,
                Mediatek,
                Samsung,
                Hisilicon,
                Apple,
                Other
            }

            public Vendors Vendor { get; private set; }


            private static Vendors DetermineVendor(string sample) => sample.ToUpper() switch
            {
                "AMD" => Vendors.Amd,
                "SAMSUNG" => Vendors.Samsung,
                "HISILICON" => Vendors.Hisilicon,
                "MEDIATEK" => Vendors.Mediatek,
                "APPLE" => Vendors.Apple,
                "INTEL" => Vendors.Intel,
                "QUALCOMM" => Vendors.Qualcomm,
                _ => Vendors.Other
            };

            public Cpu(IReadOnlyList<string> cpuInfo)
            {
                Vendor = cpuInfo.Count > 0 ? Cpu.DetermineVendor(cpuInfo[0]) : Vendors.Other;
            }
        }

        private Cpu _cpuInfo;

        public Computer()
        {
            Cost = 0;
            _cpuInfo = new Cpu(Array.Empty<string>());
        }

        protected Computer(uint cost, IReadOnlyList<string> cpuInfo, IReadOnlyList<string> memoryInfo, string os)
        {
            Cost = cost;
            _cpuInfo = new Cpu(cpuInfo);
            Ram = Convert.ToUInt32(memoryInfo[0]);
            Convert.ToUInt32(memoryInfo[1]);
            OperatingSystem = os;
        }

        public override void PrintInfo()
        {
            Console.WriteLine($"OS: {this.OperatingSystem}");
            Console.WriteLine($"Cost: {this.Cost} {Currency}");
            Console.WriteLine($"Vendor of CPU: {this._cpuInfo.Vendor}");
        }


        public override void UpgradeRam(byte gigabytes) => this.Ram += gigabytes;
    }
}