namespace LR_053506_Slutski_Lab7.Types
{
    public class SingleCall
    {
        public Tariff UsedTariff { get; }
        private ushort _duration;

        public SingleCall(Tariff tariff, ushort duration) =>
            (UsedTariff, _duration, Cost) = (tariff, duration, (ushort) (tariff.CostPerMinute * duration));

        public ushort Cost { get; }
    }
}