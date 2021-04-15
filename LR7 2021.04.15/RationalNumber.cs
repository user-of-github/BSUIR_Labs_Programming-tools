using System;

namespace LR7_2021._04._15
{
    internal class RationalNumber : IComparable, IEquatable<RationalNumber>
    {
        private long _numerator, _abbreviatedNumerator;

        private ulong _denominator, _abbreviatedDenominator;

        public RationalNumber(long numerator, ulong denominator)
        {
            _numerator = numerator;
            _denominator = denominator;
            var gcd = GreatestCommonDivider((ulong) Math.Abs(_numerator), _denominator);

            _abbreviatedNumerator = _numerator / (long) gcd;
            _abbreviatedDenominator = _denominator / gcd;
        }

        public RationalNumber(long integer)
        {
            _numerator = integer;
            _denominator = 1;
            _abbreviatedDenominator = 1;
            _abbreviatedNumerator = integer;
        }

        public RationalNumber(string expression)
        {
            var dividers = new char[] {'/', ':', '\\', '|'};
            var nums = expression.Split(dividers);
            if (nums.Length != 2)
                throw new Exception("Unacceptable expression");

            _numerator = Convert.ToInt64(nums[0].Trim());
            _denominator = Convert.ToUInt64(nums[1].Trim());
            var gcd = GreatestCommonDivider((ulong) Math.Abs(_numerator), _denominator);

            _abbreviatedNumerator = _numerator / (long) gcd;
            _abbreviatedDenominator = _denominator / gcd;
        }

        private static ulong GreatestCommonDivider(ulong first, ulong second)
        {
            while (first != 0 && second != 0)
                if (first > second)
                    first %= second;
                else
                    second %= first;

            return first | second;
        }

        private static ulong LeastCommonMultiple(ulong first, ulong second) =>
            (first * second) / GreatestCommonDivider(first, second);

        public override string ToString() => $"{_numerator} / {_denominator}\n";

        public RationalNumber GetShortenFraction() => new(_abbreviatedNumerator, _abbreviatedDenominator);

        private static RationalNumber SumOrDifference(RationalNumber first, RationalNumber second, char operation)
        {
            var commonDenominator = LeastCommonMultiple(first._abbreviatedDenominator, second._abbreviatedDenominator);
            var firstMultiplicationFactor = commonDenominator / first._abbreviatedDenominator;
            var secondMultiplicationFactor = commonDenominator / second._abbreviatedDenominator;

            var newNumerator = operation switch
            {
                '+' => first._abbreviatedNumerator * (long) firstMultiplicationFactor +
                       second._abbreviatedNumerator * (long) secondMultiplicationFactor,
                '-' => first._abbreviatedNumerator * (long) firstMultiplicationFactor -
                       second._abbreviatedNumerator * (long) secondMultiplicationFactor,
                _ => throw new Exception("Unknown operation")
            };

            return new RationalNumber(newNumerator, commonDenominator);
        }

        public static RationalNumber operator +(RationalNumber first, RationalNumber second) =>
            SumOrDifference(first, second, '+');

        public static RationalNumber operator -(RationalNumber first, RationalNumber second) =>
            SumOrDifference(first, second, '-');

        public static RationalNumber operator +(RationalNumber first, long second) =>
            SumOrDifference(first, new RationalNumber(second), '+');

        public static RationalNumber operator +(long first, RationalNumber second) =>
            SumOrDifference(new RationalNumber(first), second, '+');

        public static RationalNumber operator -(RationalNumber first, long second) =>
            SumOrDifference(first, new RationalNumber(second), '-');

        public static RationalNumber operator -(long first, RationalNumber second) =>
            SumOrDifference(new RationalNumber(first), second, '-');

        private static RationalNumber Multiplication(RationalNumber first, RationalNumber second) =>
            new RationalNumber(first._abbreviatedNumerator * second._abbreviatedNumerator,
                first._abbreviatedDenominator * second._abbreviatedDenominator).GetShortenFraction();

        public static RationalNumber operator *(RationalNumber first, RationalNumber second) =>
            Multiplication(first, second);

        public static RationalNumber operator *(RationalNumber first, long second) =>
            Multiplication(first, new RationalNumber(second));

        public static RationalNumber operator *(long first, RationalNumber second) =>
            Multiplication(new RationalNumber(first), second);

        public static RationalNumber operator /(RationalNumber first, RationalNumber second) =>
            Multiplication(first, new RationalNumber(
                (long) second._denominator * (second._numerator > 0 ? 1 : -1),
                (ulong) Math.Abs(second._numerator))
            );

        public static RationalNumber operator /(RationalNumber first, long second) =>
            first / new RationalNumber(second);

        public static RationalNumber operator /(long first, RationalNumber second) =>
            new RationalNumber(first) / second;

        public static bool operator ==(RationalNumber first, RationalNumber second) => first is not null &&
            second is not null &&
            (first._abbreviatedNumerator == second._abbreviatedNumerator &&
             first._abbreviatedDenominator == second._abbreviatedDenominator);

        public static bool operator !=(RationalNumber first, RationalNumber second) => first is not null &&
            second is not null &&
            (first._abbreviatedNumerator != second._abbreviatedNumerator ||
             first._abbreviatedDenominator != second._abbreviatedDenominator);

        public static bool operator <(RationalNumber first, RationalNumber second) =>
            (((decimal) (decimal) first._abbreviatedNumerator / (decimal) first._abbreviatedDenominator) <
             (decimal) ((decimal) second._abbreviatedNumerator / (decimal) second._abbreviatedDenominator));

        public static bool operator >(RationalNumber first, RationalNumber second) =>
            (((decimal) (decimal) first._abbreviatedNumerator / (decimal) first._abbreviatedDenominator) >
             ((decimal) ((decimal) second._abbreviatedNumerator / (decimal) second._abbreviatedDenominator)));

        public static bool operator >(RationalNumber first, long second) => first > new RationalNumber(second);

        public static bool operator <(RationalNumber first, long second) => first < new RationalNumber(second);

        public static bool operator >(long first, RationalNumber second) => new RationalNumber(first) > second;

        public static bool operator <(long first, RationalNumber second) => new RationalNumber(first) < second;

        public int CompareTo(object other)
        {
            if (other is not RationalNumber obj)
                throw new Exception("Exception: Not the Computer Type.");

            if (this == obj) return 1;
            if (this < obj) return -1;
            return 0;
        }

        public bool Equals(RationalNumber other) => other is not null &&
                                                    (_abbreviatedNumerator == other._abbreviatedNumerator &&
                                                     _abbreviatedDenominator == other._abbreviatedDenominator);
    }
}