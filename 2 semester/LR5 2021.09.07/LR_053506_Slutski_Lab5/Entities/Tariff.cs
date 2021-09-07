namespace LR_053506_Slutski_Lab5.Entities
{
    public enum TariffType
    {
        Local = 0,
        Intercity = 1,
        International = 2
    }

    public class Tariff
    {
        public TariffType Type { get; private set; }
        public ushort Price { get; set; }
        public Tariff(TariffType type, ushort price) => (Type, Price) = (type, price);
    }
}