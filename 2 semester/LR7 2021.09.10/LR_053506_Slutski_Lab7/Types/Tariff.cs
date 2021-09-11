namespace LR_053506_Slutski_Lab7.Types
{
    public class Tariff
    {
        public TariffType Type { get; }
        public ushort CostPerMinute { get; private set; }

        public Tariff(TariffType type, ushort cost) => (Type, CostPerMinute) = (type, cost);

        public void UpdateCost(ushort newCost) => CostPerMinute = newCost > 0 ? newCost : CostPerMinute;
    }
}