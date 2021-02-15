using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace LR_1_Slutski_variant3
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            string fileName = "labirint.txt";
            Labirint test = new Labirint(ref fileName);
            test.PrintField();
            Console.Read();
        }
    }

    class Labirint
    {
        private static char TEXTURE_TYPE = '▓';
        private static string TEXTURE = "" + TEXTURE_TYPE + TEXTURE_TYPE;
        private byte _width;
        private byte _height;
        private List<List<bool>> _field = new List<List<bool>>();
        public Labirint(ref string fileName)
        {
            string[] lines = File.ReadAllLines(fileName);
            this._width = Convert.ToByte(lines[0]);
            this._height = Convert.ToByte(lines[1]);
            for (byte counter = 2; counter < (2 + this._height); ++counter)
            {
                var tempRowList = new List<bool>();
                foreach (var state in lines[counter].Split(' ').ToArray())
                {
                    tempRowList.Add(Convert.ToBoolean(Convert.ToByte(state.Trim())));
                }
                this._field.Add(tempRowList);
            }
        }

        public void PrintField()
        {
            Console.OutputEncoding = Encoding.UTF8;
            for (byte row = 0; row < this._height; ++row)
            {
                Console.Write(TEXTURE);
                for (byte col = 0; col < this._width; ++col)
                {
                    Console.Write((this._field[row][col] == false ? TEXTURE : "  "));
                }

                Console.Write(TEXTURE + '\n');
            }
        }
    }
}