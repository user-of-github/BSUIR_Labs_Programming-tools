using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StreamService
{
    public class House
    {
        private static readonly HashSet<string> ids = new();
        public string Id { get; private set; }
        public string Name { get; private set; }
        public ushort RentersNumber { get; private set; }

        public House(string name, ushort rentersNumber) => 
            (Id, Name, RentersNumber) = (GenerateId(), name, rentersNumber);

        private static string GenerateId()
        {
            const string str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$%^&*()";
            var num = new Random();

            var rand = new string(str.ToCharArray().OrderBy(s => (num.Next(2) % 2) == 0).ToArray());

            while (ids.Contains(rand))
                rand = new string(str.ToCharArray().OrderBy(s => (num.Next(2) % 2) == 0).ToArray());

            return rand;
        }
    }
}
