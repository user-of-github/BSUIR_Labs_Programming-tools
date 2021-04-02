#include "pch.h"
#include "TestLibrary.h"

bool CheckIfPolindrom(int number)
{
	vector<int> digits;
	while (number > 0)
	{
		digits.push_back(number % 10);
		number /= 10;
	}
	for (int counter = 0; counter < digits.size() / 2; ++counter)
		if (digits[counter] != digits[digits.size() - counter - 1])
			return false;

	return true;
}

int ReflectNumber(int number)
{
	return number * (-1);
}
