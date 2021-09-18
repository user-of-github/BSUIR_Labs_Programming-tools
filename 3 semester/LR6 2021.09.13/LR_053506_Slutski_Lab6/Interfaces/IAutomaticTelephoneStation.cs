using LR_053506_Slutski_Lab6.Entities;


namespace LR_053506_Slutski_Lab6.Interfaces
{
    public interface IAutomaticTelephoneStation
    {
        void RegisterClient(Client client);

        Client GetClientBySurname(string surname);

        void AddTariff(Tariff tarrif);

        ushort CountAllUsersCost();

        string GetTariffsInformation();
    }
}