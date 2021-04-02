
using System;
using System.Runtime.InteropServices;

namespace DinamicLibraryUsage
{
	class Program
	{

        [DllImport("TestLibrary.dll", CallingConvention = CallingConvention.StdCall)]
        private static extern bool CheckIfPalindrom(int number);

        [DllImport("TestLibrary.dll", CallingConvention = CallingConvention.StdCall)]
        private static extern int ReflectNumber(int number);

        [DllImport("TestLibrary.dll", CallingConvention = CallingConvention.StdCall)]
        private static extern long ConvertToInteger(String number);

        static void Main(string[] args)
		{
            int test = 123321;

            Console.WriteLine(CheckIfPalindrom(test));
		}
	}
}
