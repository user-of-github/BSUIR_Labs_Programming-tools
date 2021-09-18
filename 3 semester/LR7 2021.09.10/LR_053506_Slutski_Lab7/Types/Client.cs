using System.Collections.Generic;
using System.Linq;

namespace LR_053506_Slutski_Lab7.Types
{
    public class Client
    {
        public string Surname { get; }
        private readonly List<SingleCall> _calls;

        public Client(string surname) =>
            (Surname, _calls) = (surname.Trim(), new List<SingleCall>());

        public ushort GetAllCallsCost() => (ushort) _calls.Sum(call => call.Cost);

        public List<string> GetSumsForEveryUsedTariff() =>
            _calls.GroupBy(call => call.UsedTariff)
                .Select(groupedItem =>
                    $"{groupedItem.Key.Type.ToString()}: " +
                    $"{_calls.Sum(call => call.UsedTariff.Type == groupedItem.Key.Type ? call.Cost : 0)}")
                .ToList();

        public void RegisterCall(SingleCall call) => _calls.Add(call);
    }
}