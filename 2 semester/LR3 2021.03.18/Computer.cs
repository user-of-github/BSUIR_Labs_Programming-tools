using System;
using System.Collections.Generic;
using System.IO;

namespace LR3_2021._03._18
{
    internal class Computer
    {
        public static IEnumerable<Computer> LoadFromDataBaseFile(string filePath)
        {
            var data = new List<Computer>();
            var readData = new StreamReader(filePath, System.Text.Encoding.Default);

            var amountOfModels = Convert.ToByte(readData.ReadLine().Trim());
            for (var counter = 0; counter < amountOfModels; ++counter)
            {
                var type = Computer.DetermineComputerType(readData.ReadLine().Trim());
                var cost = Convert.ToUInt32(readData.ReadLine().Trim());
                var cpu = readData.ReadLine().Trim().Split(new char[] {' '}, StringSplitOptions.RemoveEmptyEntries);
                var memory = readData.ReadLine().Trim().Split(new char[] {' '}, StringSplitOptions.RemoveEmptyEntries);
                var os = readData.ReadLine().Trim();
                data.Add(new Computer(type, cost, cpu, memory, os));
            }

            return data;
        }

        public enum ComputerType
        {
            Laptop,
            Desktop,
            Tablet,
            Other
        }

        public ComputerType Type { get; set; }
        public uint Cost { get; set; }
        public uint Ram { get; set; }
        public uint Rom { get; set; }
        public string OperatingSystem { get; set; }

        private struct Cpu
        {
            private const string Uncertainty = "unknown";

            private enum Vendors
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

            private Vendors _vendor { get; set; }
            private string _model { get; set; }
            private uint _clockSpeed { get; set; }
            private uint _processTechnology { get; set; }

            private static Vendors DetermineVendor(string sample) => sample.ToUpper() switch
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
                _clockSpeed = cpuInfo.Count > 2 ? Convert.ToUInt32(cpuInfo[2]) : 0;
                _processTechnology = cpuInfo.Count > 3 ? Convert.ToUInt32(cpuInfo[3]) : 0;
            }
        }

        private Cpu _cpuInfo;

        public Computer()
        {
            Type = DetermineComputerType("");
            Cost = 0;
            _cpuInfo = new Cpu(Array.Empty<string>());
        }

        public Computer(ComputerType type, uint cost, string[] cpuInfo, string[] memoryInfo, string os)
        {
            Type = type;
            Cost = cost;
            _cpuInfo = new Cpu(cpuInfo);
            Ram = Convert.ToUInt32(memoryInfo[0]);
            Rom = Convert.ToUInt32(memoryInfo[1]);
            OperatingSystem = os;
        }


        public static ComputerType DetermineComputerType(string sample) => sample.ToLower() switch
        {
            "tablet" => ComputerType.Tablet,
            "laptop" => ComputerType.Laptop,
            "notebook" => ComputerType.Laptop,
            "pc" => ComputerType.Desktop,
            "desktop" => ComputerType.Desktop,
            "pad" => ComputerType.Tablet,
            _ => ComputerType.Other
        };
    }
}