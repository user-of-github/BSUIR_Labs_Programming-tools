using System;

namespace LR6_2021._04._08
{
    internal abstract class Gadget : IComparable
    {
        public uint Cost { get; set; }

        public int CompareTo(object other)
        {
            if (other is Gadget obj)
                if (this.Cost > obj.Cost) return 1;
                else if (this.Cost < obj.Cost) return -1;
                else return 0;
            else
                throw new Exception("Exception: Not the Computer Type.");
        }
        
        public abstract void UpgradeRam(byte gigabytes);
        public abstract void PrintInfo();
    }
}