using System;
using System.Collections.Generic;
using System.Linq;

namespace LR8_2021._04._29
{
    internal abstract class Computer : Gadget, IInformation, IGadget
    {
        private const byte IdLength = 10;

        private static readonly HashSet<string> AllIds = new HashSet<string>();

        public string Id;

        private static string GenerateId()
        {
            const string chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz";
            var random = new Random();
            return new string(Enumerable.Repeat(chars, IdLength).Select(s => s[random.Next(s.Length)]).ToArray());
        }

        private const string Currency = "BYN";
        private uint Ram { get; set; }
        private string OperatingSystem { get; }

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

            public Vendors Vendor { get; }

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
                Vendor = cpuInfo.Count > 0 ? DetermineVendor(cpuInfo[0]) : Vendors.Other;
            }
        }

        private readonly Cpu _cpuInfo;

        protected Computer()
        {
            Cost = 0;
            _cpuInfo = new Cpu(Array.Empty<string>());

            AddIdentificator();
        }

        protected Computer(uint cost, IReadOnlyList<string> cpuInfo, IReadOnlyList<string> memoryInfo, string os)
        {
            Cost = cost;
            _cpuInfo = new Cpu(cpuInfo);
            Ram = Convert.ToUInt32(memoryInfo[0]);
            Convert.ToUInt32(memoryInfo[1]);
            OperatingSystem = os;

            AddIdentificator();
        }

        public override void PrintInfo() =>
            Console.WriteLine($"OS: {OperatingSystem}\nCost: {Cost} {Currency}\nVendor of CPU: {_cpuInfo.Vendor}");

        public override void UpgradeRam(byte gigabytes) => Ram += gigabytes;

        private void AddIdentificator()
        {
            var newId = GenerateId();
            while (AllIds.Contains(newId))
                newId = GenerateId();

            Id = newId;
            AllIds.Add(newId);
        }

        public delegate void PrintUniqueCharacteristic();

        public event PrintUniqueCharacteristic OnGettingId;

        public void GetIdentificator()
        {
            try
            {
                OnGettingId.Invoke();
            }
            catch
            {
                Console.WriteLine("Print ID method doesn't work correctly");
            }
        }
    }
}