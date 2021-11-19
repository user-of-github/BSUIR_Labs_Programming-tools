using System;
using SinusIntegral;
using System.Threading;
using System.Text;

namespace Application
{
    internal static class Program
    {
        private static void Main() => Run();

        private static void Run()
        {
            Console.OutputEncoding = Encoding.UTF8;

            var firstThread = new Thread(new ParameterizedThreadStart(Count));
            var secondThread = new Thread(new ParameterizedThreadStart(Count));

            firstThread.Priority = ThreadPriority.Lowest;
            secondThread.Priority = ThreadPriority.Highest;

            firstThread.Name = "First Thread (ThreadPriority.Lowest)";
            secondThread.Name = "Second Thread (ThreadPriority.Highest)";
           

            firstThread.Start(firstThread.Name);
            secondThread.Start(secondThread.Name);
        }

        private static void Count(object threadName) => 
            SinusIntegral.SinusIntegral.CountSinus((double result, double milliseconds) => 
            Console.WriteLine($"{threadName}\n\tRESPONSE:{result}\n\tTIME: {milliseconds}\n"));
        
    }
}
