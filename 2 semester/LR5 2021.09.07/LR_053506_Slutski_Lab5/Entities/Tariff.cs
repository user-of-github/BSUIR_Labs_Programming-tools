using LR_053506_Slutski_Lab5.Interfaces;

namespace LR_053506_Slutski_Lab5.Entities
{
    public enum TariffType
    {
        LOCAL = 0,
        INTERCITY = 1,
        INTERNATIONAL = 2
    }

    public class Tariff : ITariff
    {
        private const string Currency = "BYN";
        public TariffType Type { get; private set; }
        public ushort Price { get; set; }

        public Tariff(TariffType type, ushort price) => (Type, Price) = (type, price);

        public string GetInformation() => $"{Type.ToString()} | {Price}{Currency}/min";
    }
}