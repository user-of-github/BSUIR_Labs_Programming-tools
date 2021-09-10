using System;
using System.Collections.Generic;
using System.Linq;
using LR_053506_Slutski_Lab5.Collections;
using LR_053506_Slutski_Lab5.Entities;


namespace LR_053506_Slutski_Lab5
{
    internal static class Program
    {
        private static void Main()
        {
            /* MAIN STATION INSTANCE */
            var station = new AutomaticTelephoneStation();


            /* IEnumerable INTERFACE (IMPLEMENTED) & SETTING TARIFFS TO STATION */
            var testCollectionTariffs = new CustomCollection<Tariff>();
            GetDefaultTariffsPack().ToList().ForEach(testCollectionTariffs.Add);
            foreach (var tariff in testCollectionTariffs)
                station.AddTariff(tariff);


            /* GETTING INFO ABOUT CURRENT SET OF TARIFFS IN THE STATION */
            Console.WriteLine(station.GetTariffsInformation());
            // output: LOCAL | 5BYN/min, INTERCITY | 10BYN/min, INTERNATIONAL | 15BYN/min


            /* REGISTERING TRIAL CLIENTS TO THE STATION */
            GetDefaultClientsPack().ToList().ForEach(station.RegisterClient);
            Console.WriteLine(station.GetClientsInformation());
            // output: Slutski, calls: 0, total spent: 0, Levankou, calls: 0, total spent: 0


            /* REGISTERING TRIAL CALL FOR FOUND CLIENT (BY SURNAME) */
            station.GetClientBySurname("Levankov")?.RegisterCall(new SingleCall(testCollectionTariffs[0], 5));
            Console.WriteLine(station.GetClientsInformation());
            // output: Slutski, calls: 0, total spent: 0, Levankou, calls: 1, total spent: 25


            /* DEMONSTRATING OF INDEXER */
            Console.WriteLine(testCollectionTariffs[(ushort) (testCollectionTariffs.Count - 1)].GetInformation());
            // output: INTERNATIONAL | 15BYN/min


            /* TOTAL CALLS COST */
            station.GetClientBySurname("Slutski")?.RegisterCall(new SingleCall(testCollectionTariffs[1], 50));
            Console.WriteLine(station.CountAllUsersCost());
            // output: 525
        }


        private static IEnumerable<Tariff> GetDefaultTariffsPack() => new[]
        {
            new Tariff(TariffType.LOCAL, 5),
            new Tariff(TariffType.INTERCITY, 10),
            new Tariff(TariffType.INTERNATIONAL, 15)
        };

        private static IEnumerable<Client> GetDefaultClientsPack() => new[]
        {
            new Client("Slutski"),
            new Client("Levankov")
        };
    }
}