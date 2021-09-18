using System;
using LR_053506_Slutski_Lab6.Interfaces;


namespace LR_053506_Slutski_Lab6.Entities
{
    public class SingleCall: ISingleCall
    {
        private const string DurationMeasurementUnits = "min";
        private const string CurrencyMeasurementUnits = "BYN";
        private readonly Tariff _usedTarrif;
        private readonly byte _duration;
        private ushort _totalCost;

        public SingleCall(Tariff tariff, byte duration) =>
            (_usedTarrif, _duration, _totalCost) = (tariff, duration, (ushort) (tariff.Price * duration));

        public override string ToString() =>
            $"{Enum.GetName(typeof(TariffType), _usedTarrif.Type)}; " +
            $"{_duration} {DurationMeasurementUnits}; " +
            $"{_totalCost} {CurrencyMeasurementUnits}";

        public void RecountTotalCosts() => _totalCost = (ushort)(_duration * _usedTarrif.Price);

        public ushort TotalCost => _totalCost;
    }
}