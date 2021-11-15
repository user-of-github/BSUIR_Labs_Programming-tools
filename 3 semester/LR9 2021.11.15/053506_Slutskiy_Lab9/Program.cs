using System;
using _053506_Slutskiy_Lab9.Domain;
using System.Collections.Generic;
using System.Linq;

namespace _053506_Slutskiy_Lab9
{
    internal class Program
    {
        static void Main() => Run();

        private static void Run()
        {
            var data = GetDefaultList();

            Serializer.Serializer serialize = new();

            serialize.SerializeXML(data, "test.xml");
            serialize.SerializeJSON(data, "test2.json");
            serialize.SerializeByLINQ(data, "test3.xml");

            Console.WriteLine("\nFrom JSON: ");
            serialize.DeSerializeJSON("test2.json")
                .ToList()
                .ForEach(item => Console.Write($"{item.PowerConsumption} "));

            Console.WriteLine("\nFrom XML: ");
            serialize.DeSerializeXML("test.xml")
                .ToList()
                .ForEach(item => Console.Write($"{item.PowerConsumption} "));

            Console.WriteLine("\nFrom XML (LINQ): ");
            serialize.DeSerializeByLINQ("test3.xml")
                .ToList()
                .ForEach(item => Console.Write($"{item.PowerConsumption} "));
        }

        private static List<HeatedBuilding> GetDefaultList()
        {
            List<HeatedBuilding> response = new();
            for (ushort count = 0; count < 5; ++count)
                response.Add(new HeatedBuilding(count));
            return response;
        }
    }
}
