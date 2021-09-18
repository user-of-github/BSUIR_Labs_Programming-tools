using System;
using System.Collections.Generic;

namespace LR8_2021._04._29
{
    internal sealed class Smartphone : MobileDevice
    {
        public delegate void NewOwner(string data);

        public event NewOwner OnNewOwner;

        public void AddNewOwner(string data)
        {
            try
            {
                OnNewOwner?.Invoke(data);
            }
            catch
            {
                Console.WriteLine("New Owner delegate does not work or data is not suitable");
            }
        }

        private bool HasInfraredPort { get; }

        public Smartphone(uint cost, string[] cpuInfo, IReadOnlyList<string> memoryInfo, string os, uint weight,
            bool hasPort) :
            base(cost,
                cpuInfo, memoryInfo, os, weight)
        {
            HasInfraredPort = hasPort;
            Owners = new List<string>();
        }

        public List<string> Owners { get; }

        public override void PrintInfo()
        {
            Console.WriteLine("_______________________");
            Console.WriteLine("Smartphone:");
            base.PrintInfo();
            Console.Write(HasInfraredPort ? "Has" : "Doesn't have");
            Console.WriteLine(" infrared port");
            Console.WriteLine("_______________________");
        }
    }
}