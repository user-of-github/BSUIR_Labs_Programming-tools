using LR_053506_Slutski_Lab5.Collections;
using LR_053506_Slutski_Lab5.Interfaces;

namespace LR_053506_Slutski_Lab5.Entities
{
    public class AutomaticTelephoneStation : IAutomaticTelephoneStation
    {
        private readonly CustomCollection<Tariff> _tarrifs;
        private CustomCollection<Client> _clients;

        public void AddTarrif(Tariff tariff) => _tarrifs.Add(tariff);

        public void RegisterClient(Client client) => _clients.Add(client);

        public Client GetClientBySurname(string surname)
        {
            while (_clients.Current() != null && _clients.Current().Surname != surname)
                _clients.Next();
            return _clients.Current();
        }
    }
}