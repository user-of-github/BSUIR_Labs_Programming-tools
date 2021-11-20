using System;
using System.Threading;
using System.Text;
using System.Threading.Tasks;
using System.IO;


namespace Application
{
    public static class Program
    {
        // delegate for counting sinus
        private static void Count() => 
            SinusIntegral.SinusIntegral.CountSinus((double result, double milliseconds) => 
            Console.WriteLine($"{Thread.CurrentThread.Name}\n\tRESPONSE:{result}\n\tTIME: {milliseconds}\n"));

        public static async Task Main()
        {
            Console.OutputEncoding = Encoding.UTF8;

            const string FilePath = "data.json";
            // separate threads for sinus
            Thread firstThread = new(Count);
            Thread secondThread = new(Count);

            firstThread.Priority = ThreadPriority.Lowest;
            secondThread.Priority = ThreadPriority.Highest;

            firstThread.Name = "First Thread (ThreadPriority.Lowest)";
            secondThread.Name = "Second Thread (ThreadPriority.Highest)";

            firstThread.Start();
            secondThread.Start();

            ///////////////////////////////////////////////////////////////////////
            
            MemoryStream memoryStream = new (); // realization of Stream Class
            Task writing = StreamService.StreamService.WriteToStream(memoryStream);

            
            Task copy = StreamService.StreamService.CopyFromStream(memoryStream, FilePath);
            await Task.WhenAll(writing, copy); // waiting 1st and 2nd methods to complete (because Main is async)


            int filtCount = await StreamService.StreamService.GetStatisticsAsync(FilePath, Filter);
            Console.WriteLine($"\nFiltered houses, where <= 1000 renters = {filtCount}\n");
        }

        public static bool Filter(StreamService.House house) => house.RentersNumber <= 1000;
    }
}
