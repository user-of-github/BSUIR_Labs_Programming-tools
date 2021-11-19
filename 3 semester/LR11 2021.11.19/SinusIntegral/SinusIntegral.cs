using System;
using System.Diagnostics;

namespace SinusIntegral
{
    public static class SinusIntegral
    {
        private const double Step = 0.00000001;
        private const double LeftBorder = 0;
        private const double RightBorder = 1;
        public delegate void OnFinish(double result, double time);

        public static void CountSinus(OnFinish onfinish)
        {
            var timer = new Stopwatch();
            timer.Start();

            var response = 0.0;
            for (var x = LeftBorder; x <= RightBorder; x += Step)
                response += Step * Math.Sin(x + Step / 2);

            timer.Stop();

            onfinish(response, timer.ElapsedMilliseconds);
        }
    }
}
