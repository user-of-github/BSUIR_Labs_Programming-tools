using System;

namespace Library
{
	public static class Library
	{
		public static bool CheckIfPalindrom(string word)
		{
			for (var counter = 0; counter < word.Length / 2; ++counter)
				if (word[counter] != word[word.Length - counter - 1])
					return false;

			return true;
		}

		public static ulong ConvertToInteger(string word)
		{
			ulong response = 0;
			foreach (var symbol in word)
				response = response * 10 + (ulong)((int)symbol - 48);

			return response;
		}

		public static bool CheckIfNumber(string word)
		{
			const string Numbers = "0123456789";
			foreach (var symbol in word)
				if (Numbers.Contains(symbol) == false)
					return false;

			return true;
		}

	}
}
