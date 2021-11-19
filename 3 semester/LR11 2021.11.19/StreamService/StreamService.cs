using System;
using System.IO;
using System.Threading.Tasks;

namespace StreamService
{
    public static class StreamService
    {
        public static Task WriteToStream(Stream stream)
        {
            return null;
        }

        public static Task CopyFromStream(Stream stream, string fileName)
        {
            return null;
        }

        public async Task<int> GetStatisticsAsync(string fileName, Func<House, bool> filter)
        {
            return 32;
        }
    }
}
