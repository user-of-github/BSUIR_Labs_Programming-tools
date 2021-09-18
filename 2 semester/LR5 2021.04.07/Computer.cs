using System;
using System.Collections.Generic;
using System.IO;

namespace LR5_2021._04._07
{
    internal abstract class Computer
    {
        private const string Currency = "BYN";
        public uint Cost { get; set; }
        public uint Ram { get; set; }
        public uint Rom { get; set; }
        public string OperatingSystem { get; set; }

        private struct Cpu
        {
            private const string Uncertainty = "unknown";

            internal enum Vendors
            {
                AMD,
                QUALCOMM,
                INTEL,
                MEDIATEK,
                SAMSUNG,
                HISILICON,
                APPLE,
                OTHER
            }

            public Vendors _vendor { get; set; }
            public string _model { get; set; }


            public static Vendors DetermineVendor(string sample) => sample.ToUpper() switch
            {
                "AMD" => Vendors.AMD,
                "SAMSUNG" => Vendors.SAMSUNG,
                "HISILICON" => Vendors.HISILICON,
                "MEDIATEK" => Vendors.MEDIATEK,
                "APPLE" => Vendors.APPLE,
                "INTEL" => Vendors.INTEL,
                "QUALCOMM" => Vendors.QUALCOMM,
                _ => Vendors.OTHER
            };

            public Cpu(IReadOnlyList<string> cpuInfo)
            {
                _vendor = cpuInfo.Count > 0 ? Cpu.DetermineVendor(cpuInfo[0]) : Vendors.OTHER;
                _model = cpuInfo.Count > 1 ? cpuInfo[1] : Uncertainty;
            }
        }

        private Cpu _cpuInfo;

        public Computer()
        {
            Cost = 0;
            _cpuInfo = new Cpu(Array.Empty<string>());
        }

        public Computer(uint cost, string[] cpuInfo, string[] memoryInfo, string os)
        {
            Cost = cost;
            _cpuInfo = new Cpu(cpuInfo);
            Ram = Convert.ToUInt32(memoryInfo[0]);
            Rom = Convert.ToUInt32(memoryInfo[1]);
            OperatingSystem = os;
        }

        public virtual void PrintInfo()
        {
            Console.WriteLine($"OS: {this.OperatingSystem}");
            Console.WriteLine($"Cost: {this.Cost} {Currency}");
            Console.WriteLine($"Vendor of CPU: {this._cpuInfo._vendor}");
        }
    }
}