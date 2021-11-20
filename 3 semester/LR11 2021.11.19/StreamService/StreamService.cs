using System;
using System.Collections.Generic;
using System.IO;
using System.Threading;
using System.Threading.Tasks;
using System.Linq;
using System.Text.Json;
using System.Text;

namespace StreamService
{
    public static class StreamService
    {
        private static readonly object GenralThreadLockerReference = new(); // where to read: https://metanit.com/sharp/tutorial/11.4.php

        public static Task WriteToStream(Stream stream)
        {
            const ushort TestDataCount = 1000;
            using (Utf8JsonWriter writer = new(stream))
            {
                List<House> testData = new();
                Random randomizer = new();

                for (ushort counter = 1; counter < TestDataCount; ++counter)
                    testData.Add(new House($"House №{counter}",(ushort)(counter + randomizer.Next(0, 10000))));

                byte[] byteArray = Encoding.UTF8.GetBytes(JsonSerializer.Serialize(testData));

                return Task.Run(() =>
                {
                    lock (GenralThreadLockerReference)
                    {
                        Console.WriteLine($"WriteToStream: STARTED WRITTING TO THREAD: {Thread.CurrentThread.ManagedThreadId}");
                        stream.Write(byteArray, 0, byteArray.Length);
                        Console.WriteLine($"WriteToStream: FINISHED WRITTING TO THREAD: {Thread.CurrentThread.ManagedThreadId}\n");
                    }
                });
            }
        }

        public static Task CopyFromStream(Stream stream, string fileName) =>
            Task.Run(() =>
            {
                StreamReader reader = new(stream);
                lock (GenralThreadLockerReference)
                {
                    Console.WriteLine($"CopyFromStream: STARTED READING FROM THREAD: {Thread.CurrentThread.ManagedThreadId}");
                    using (FileStream newStream = new(fileName, FileMode.Create))
                    {
                        stream.Position = 0;
                        stream.CopyTo(newStream);
                    }

                    Console.WriteLine($"CopyFromStream: FINISHED READING FROM THREAD: {Thread.CurrentThread.ManagedThreadId}\n");
                }
            });

        public static async Task<int> GetStatisticsAsync(string fileName, Func<House, bool> filter)
        {
            List<House> list;
            using (var reader = File.OpenRead(fileName))
            {
                Console.WriteLine($"GetStatisticsAsync: STARTED READING FROM THREAD: {Thread.CurrentThread.ManagedThreadId}");
                list = await JsonSerializer.DeserializeAsync<List<House>>(reader);
                Console.WriteLine($"GetStatisticsAsync: FINISHED READING FROM THREAD: {Thread.CurrentThread.ManagedThreadId}");
            }

            return list.Count((House house) => filter(house));
        }
    }
}
