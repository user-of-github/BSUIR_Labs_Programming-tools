using System;

namespace LR8_2021._04._29
{
    internal abstract class Gadget : IComparable
    {
        protected uint Cost { get; init; }

        public int CompareTo(object other)
        {
            if (other is not Gadget obj)
                throw new Exception("Exception: Not the Computer Type.");
            if (Cost > obj.Cost)
                return 1;
            if (Cost < obj.Cost)
                return -1;

            return 0;
        }

        public abstract void UpgradeRam(byte gigabytes);
        public abstract void PrintInfo();
    }
}