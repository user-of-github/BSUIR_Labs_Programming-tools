using System;

namespace TestDLL
{
	class Program
	{
		static void Main()
		{
			Console.WriteLine(Library.Library.CheckIfNumber("2021hello")); // False
			Console.WriteLine(Library.Library.CheckIfNumber("123456")); // True
			Console.WriteLine(Library.Library.CheckIfNumber("abcd")); // False

			Console.WriteLine(Library.Library.ConvertToInteger("123456789")); // 123456789
			Console.WriteLine(Library.Library.ConvertToInteger("98765")); // 98765

			Console.WriteLine(Library.Library.CheckIfPalindrom("1234554321")); // True
			Console.WriteLine(Library.Library.CheckIfPalindrom("123455432")); // False
		}
	}
}
