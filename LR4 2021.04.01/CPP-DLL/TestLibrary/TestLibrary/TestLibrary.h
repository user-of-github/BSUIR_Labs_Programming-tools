#pragma once
#include <vector>

#ifdef TESTLIBRARY_EXPORTS
#define DLLIMPORT_EXPORT __declspec(dllexport)
#else
#define DLLIMPORT_EXPORT __declspec(dllimport)
#endif

using namespace std;

extern "C" {
	DLLIMPORT_EXPORT bool _stdcall CheckIfPolindrom(int number);
	DLLIMPORT_EXPORT int _stdcall ReflectNumber(int number);
}