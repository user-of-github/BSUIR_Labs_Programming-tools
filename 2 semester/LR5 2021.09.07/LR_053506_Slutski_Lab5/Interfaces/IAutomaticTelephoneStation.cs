using LR_053506_Slutski_Lab5.Entities;


namespace LR_053506_Slutski_Lab5.Interfaces
{
    public interface IAutomaticTelephoneStation
    {
        void RegisterClient(Client client);

        Client GetClientBySurname(string surname);

        void AddTarrif(Tariff tarrif);
    }
}