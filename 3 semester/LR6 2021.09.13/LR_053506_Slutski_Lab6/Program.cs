using System;
using System.Collections.Generic;
using System.Linq;
using LR_053506_Slutski_Lab6.Collections;
using LR_053506_Slutski_Lab6.Entities;

namespace LR_053506_Slutski_Lab6
{
    internal static class Program
    {
        private static void Main() => RunAppDemonstration();


        private static void RunAppDemonstration()
        {
            var station = new AutomaticTelephoneStation();
            var journalLogger = new Journal();

            // REGISTRING ANONIMOUS FUNCTIONS FOR EVENTS
            station.AddClientNotification +=
                (description, client) =>
                    journalLogger.AddEvent(client.Surname, description);

            station.AddTariffNotification +=
                (description, tariff) =>
                    journalLogger.AddEvent(tariff.Type.ToString(), description);


            // IEnumerable INTERFACE (IMPLEMENTED) & SETTING TARIFFS TO STATION 
            var testCollectionTariffs = new CustomCollection<Tariff>();
            GetDefaultTariffsPack().ToList().ForEach(testCollectionTariffs.Add);
            foreach (var tariff in testCollectionTariffs)
                station.AddTariff(tariff);

            // CHECK FOR CORRECTNESS 
            journalLogger.PrintRegisteredEvents();
            /* output:
                Currently logged events:
                    New tariff: LOCAL
                    New tariff: INTERCITY
                    New tariff: INTERNATIONAL*/

            // REGISTERING TRIAL CLIENTS TO THE STATION 
            GetDefaultClientsPack().ToList().ForEach(station.RegisterClient);

            // CHECK FOR CORRECTNESS
            journalLogger.PrintRegisteredEvents();
            /* output:
                Currently logged events:
                    New tariff: LOCAL
                    New tariff: INTERCITY
                    New tariff: INTERNATIONAL
                    New client: Slutski
                    New client: Levankov */

            station.RegisterCallNotification += ClientCalledToSomeone;

            station.RegisterCallForClient(
                station.GetClientBySurname("Slutski"),
                new SingleCall(new Tariff(TariffType.LOCAL, 25), 2)
            ); /* output: Slutski talked & spent 50 */

            // CHECKING FOR EXCEPTIONS:
            testCollectionTariffs.Remove(GetDefaultTariffsPack().ToList()[0]);
            /* output:
             Unhandled exception. LR......Exception: Unable to remove the element. Not existing item */
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

        private static void ClientCalledToSomeone(string a, string b) =>
            Console.WriteLine($"{a} talked & spent {b}");
    }
}