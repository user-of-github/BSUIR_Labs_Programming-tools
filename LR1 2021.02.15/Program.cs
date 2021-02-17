using System;
using System.Collections;
using System.Collections.Generic;
using System.Data.Common;
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
            test.PassLabirint();
            Console.Read();
        }
    }

    class Labirint
    {
        private struct Position
        {
            public sbyte Row, Col;
        }

        private static readonly char TEXTURE_STYLE = '▓';
        private static readonly string TEXTURE = "" + TEXTURE_STYLE + TEXTURE_STYLE;
        private readonly sbyte _width;
        private readonly sbyte _height;
        private readonly List<List<bool>> _field = new List<List<bool>>();
        private readonly Position _startCoordinate = new Position {Row = -1, Col = -1};
        private readonly Position _finishCoordinate = new Position {Row = -1, Col = -1};

        public Labirint(ref string fileName)
        {
            string[] lines = File.ReadAllLines(fileName);
            this._height = Convert.ToSByte(lines[0].Split(' ')[0]);
            this._width = Convert.ToSByte(lines[0].Split(' ')[1]);
            for (sbyte counter = 1; counter < this._height + 1; ++counter)
            {
                var tempRowList = new List<bool>();
                foreach (var state in lines[counter].Split(' ').ToArray())
                    tempRowList.Add(Convert.ToBoolean(Convert.ToSByte(state.Trim())));
                this._field.Add(tempRowList);
            }

            this._startCoordinate.Row += SByte.Parse(lines[lines.Length - 2].Split(' ')[0]);
            this._startCoordinate.Col += SByte.Parse(lines[lines.Length - 2].Split(' ')[1]);
            this._finishCoordinate.Row += SByte.Parse(lines[lines.Length - 1].Split(' ')[0]);
            this._finishCoordinate.Col += SByte.Parse(lines[lines.Length - 1].Split(' ')[1]);
        }

        public void PrintField()
        {
            Console.OutputEncoding = Encoding.UTF8;

            Console.Write('\n');
            foreach (var row in this._field)
            {
                foreach (var state in row)
                    Console.Write(state ? "  " : TEXTURE);
                Console.Write('\n');
            }

            Console.Write('\n');
        }

        public void PassLabirint()
        {
            sbyte[,] directions = new sbyte[4, 2] {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

            int[,] visitedPath = new int[this._height, this._width];
            for (sbyte row = 0; row < this._height; ++row)
            {
                for (sbyte col = 0; col < this._width; ++col)
                    visitedPath[row, col] = (_field[row][col] ? 0 : -1);
            }

            visitedPath[this._startCoordinate.Row, this._startCoordinate.Col] = 0;

            var bfs = new Queue<Position>();
            bfs.Enqueue(this._startCoordinate);
            var foundPath = false;

            while (bfs.Count > 0 && !foundPath)
            {
                var currentPosition = bfs.Dequeue();
                for (sbyte counter = 0; counter < 4; ++counter)
                {
                    var x = (SByte) (currentPosition.Col + directions[counter, 0]);
                    var y = (SByte) (currentPosition.Row + directions[counter, 1]);

                    if (x >= 0 && x < this._width && y >= 0 && y < this._height && visitedPath[y, x] == 0)
                    {
                        visitedPath[y, x] = visitedPath[currentPosition.Row, currentPosition.Col] + 1;
                        bfs.Enqueue(new Position {Row = y, Col = x});
                        Console.WriteLine("{" + y + "} ; {" + x + "}");
                    }

                    if (y != this._finishCoordinate.Row || x != this._finishCoordinate.Col) continue;

                    foundPath = true;
                    break;
                }
            }

            if (foundPath)
                Console.WriteLine(
                    $"Path was found. The length of path is {visitedPath[this._finishCoordinate.Row, this._finishCoordinate.Col]}");
            else
                Console.WriteLine("Path was not found");
        }
    }
}