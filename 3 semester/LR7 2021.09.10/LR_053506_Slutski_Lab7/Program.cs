using System;
using System.Collections.Generic;
using LR_053506_Slutski_Lab7.Types;

namespace LR_053506_Slutski_Lab7
{
    internal static class Program
    {
        private static void Main() => RunApplicationDemonstration();


        private static void RunApplicationDemonstration()
        {
            var station = new AutomaticTelephoneStation();

            var tariffs = GetDefaultTariffsPack();
            var clients = GetDefaultClientsPack();

            tariffs.ForEach(station.RegisterNewTariff);
            clients.ForEach(station.RegisterClient);

            /* GETTING A LIST OF NAMES OF ALL TARIFFS, SORTED BY COST */
            Console.WriteLine(string.Join(", ", station.GetTariffsNames()));
            // output: Local, Intercity, International, Luxe


            station.GetClientBySurname(clients[0].Surname)?.RegisterCall(new SingleCall(tariffs[2], 5));
            station.GetClientBySurname(clients[0].Surname)?.RegisterCall(new SingleCall(tariffs[3], 50));
            station.GetClientBySurname(clients[3].Surname)?.RegisterCall(new SingleCall(tariffs[0], 1));


            /* GETTING THE TOTAL COST OF ALL CALLS */
            Console.WriteLine(station.GetAllCallsCost());
            // output: 710


            /* GETTING TOTAL COST OF ALL CALLS MADE BY CLIENT IN ACCORDANCE WITH THE CURRENT TARIFFS */
            Console.WriteLine(station.GetClientBySurname(clients[0].Surname)?.GetAllCallsCost());
            // output: 650
            tariffs[2].UpdateCost(8); // changing actual tariff cost
            station.GetClientBySurname(clients[0].Surname)?.RegisterCall(new SingleCall(tariffs[2], 5));
            Console.WriteLine(station.GetClientBySurname(clients[0].Surname)?.GetAllCallsCost());
            // output: 690 (8 * 5, but not a 10 * 5)


            /* GETTING NAME OF CLIENT WHO PAID MAXIMUM AMOUNT */
            station.GetClientBySurname(clients[4].Surname)?.RegisterCall(new SingleCall(tariffs[0], 20));
            Console.WriteLine(station.GetClientSurnameWithMaximumCallCost());
            // output: Sukhovei


            /* GETTING NUMBER OF CUSTOMERS WHO PAID MORE THAN A CERTAIN AMOUNT */
            station.GetClientBySurname("Khrapko")?.RegisterCall(new SingleCall(tariffs[1], 30));
            Console.WriteLine(station.GetNumberOfClientsWhoPaidMoreThan(900));
            // output: 2


            /* RECEIPT BY CLIENT OF A LIST OF AMOUNTS PAID FOR EACH TARIFF */
            Console.WriteLine(string.Join(", ", station.GetClientBySurname("Slutski")?.GetSumsForEveryUsedTariff()));
            // output: LOCAL: 90, INTERCITY: 600
        }

        private static List<Client> GetDefaultClientsPack() => new()
        {
            new Client("Slutski"),
            new Client("Levankov"),
            new Client("Bondarkov"),
            new Client("Lazarev"),
            new Client("Sukhovei"),
            new Client("Pankratov"),
            new Client("Khrapko")
        };

        private static List<Tariff> GetDefaultTariffsPack() => new()
        {
            new Tariff(TariffType.Luxe, 60),
            new Tariff(TariffType.International, 30),
            new Tariff(TariffType.Local, 10),
            new Tariff(TariffType.Intercity, 12)
        };
    }
}