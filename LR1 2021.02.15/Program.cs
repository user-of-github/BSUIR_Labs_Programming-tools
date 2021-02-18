using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading;

namespace LR1_2021._02._15
{
    class Program
    {
        static void Main()
        {
            var filePath = "labirint.txt";
            var test = new Labirint(ref filePath);

            test.PassByComputer();
            Console.Read();
        }
    }

    class Labirint
    {
        private struct Position
        {
            public sbyte Row, Col;
        }

        private static readonly sbyte[,] Directions = new sbyte[,] {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        private const byte MarginLeftSize = 4, MarginTopSize = 5;

        private static readonly string MarginLeft = new string(' ', MarginLeftSize),
            MarginTop = new string('\n', MarginTopSize);

        private static readonly char TextureStyle = '█';
        private static readonly string Texture = "" + TextureStyle + TextureStyle;

        private readonly sbyte _width, _height;
        private readonly List<List<bool>> _field = new List<List<bool>>();

        private readonly Position _startCoordinate = new Position {Row = -1, Col = -1},
            _finishCoordinate = new Position {Row = -1, Col = -1};

        private void SearchInLabirint(ref bool foundPath, ref Queue<Position> bfs, ref int[,] visitedPositions)
        {
            bfs.Enqueue(this._startCoordinate);

            while (bfs.Count > 0 && !foundPath)
            {
                var currentPosition = bfs.Dequeue();
                for (sbyte counter = 0; counter < 4; ++counter)
                {
                    var x = (SByte) (currentPosition.Col + Directions[counter, 0]);
                    var y = (SByte) (currentPosition.Row + Directions[counter, 1]);

                    if (x >= 0 && x < this._width && y >= 0 && y < this._height && visitedPositions[y, x] == 0 &&
                        !(x == this._startCoordinate.Col && y == this._startCoordinate.Row))
                    {
                        visitedPositions[y, x] = visitedPositions[currentPosition.Row, currentPosition.Col] + 1;
                        bfs.Enqueue(new Position {Row = y, Col = x});
                    }

                    if (y == this._finishCoordinate.Row && x == this._finishCoordinate.Col)
                    {
                        foundPath = true;
                        break;
                    }
                }
            }
        }

        private List<Position> GetPath(ref int[,] visitedPositions)
        {
            var path = new List<Position> {this._finishCoordinate};

            while (!(path[^1].Row == this._startCoordinate.Row && path[^1].Col == this._startCoordinate.Col))
            {
                for (sbyte counter = 0; counter < 4; ++counter)
                {
                    var x = (SByte) (path[^1].Col + Directions[counter, 0]);
                    var y = (SByte) (path[^1].Row + Directions[counter, 1]);

                    if (x >= 0 && x < this._width && y >= 0 && y < this._height && visitedPositions[y, x] != -1 &&
                        visitedPositions[y, x] == visitedPositions[path[^1].Row, path[^1].Col] - 1)
                    {
                        path.Add(new Position {Row = y, Col = x});
                        break;
                    }
                }
            }

            return path;
        }

        private void PrintField()
        {
            Console.OutputEncoding = Encoding.UTF8;

            Console.Write(MarginTop);
            foreach (var row in this._field)
            {
                Console.Write(MarginLeft);
                foreach (var state in row) Console.Write(state ? "  " : Texture);
                Console.Write('\n');
            }

            Console.Write('\n');
        }

        private void ShowPassage(ref List<Position> path)
        {
            ConsoleColor copyOfStandardColor = Console.ForegroundColor;
            this.PrintField();
            Console.CursorVisible = false;
            Console.ForegroundColor = ConsoleColor.Green;
            var previousCoordinate = this._startCoordinate;
            foreach (var currentCoordinate in path)
            {
                Console.ForegroundColor = ConsoleColor.Green;
                Console.SetCursorPosition(previousCoordinate.Col * 2 + MarginLeftSize,
                    previousCoordinate.Row + MarginTopSize);
                Console.Write(Texture);

                previousCoordinate = currentCoordinate;
                Console.ForegroundColor = ConsoleColor.Red;

                Console.SetCursorPosition(currentCoordinate.Col * 2 + MarginLeftSize,
                    currentCoordinate.Row + MarginTopSize);
                Console.Write(Texture);

                Thread.Sleep(60);
            }

            Console.ForegroundColor = copyOfStandardColor;
            Console.SetCursorPosition(MarginLeftSize, this._height + MarginTopSize);
            Console.WriteLine($"\n{MarginLeft}PASSED SUCCESSFULLY !");
        }

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

            this._startCoordinate.Row += sbyte.Parse(lines[^2].Split(' ')[0]);
            this._startCoordinate.Col += sbyte.Parse(lines[^2].Split(' ')[1]);
            this._finishCoordinate.Row += sbyte.Parse(lines[^1].Split(' ')[0]);
            this._finishCoordinate.Col += sbyte.Parse(lines[^1].Split(' ')[1]);
        }

        public void PassByComputer()
        {
            var visitedPositions = new int[this._height, this._width];
            for (sbyte row = 0; row < this._height; ++row)
            for (sbyte col = 0; col < this._width; ++col)
                visitedPositions[row, col] = (_field[row][col] ? 0 : -1);

            visitedPositions[this._startCoordinate.Row, this._startCoordinate.Col] = 0;

            var bfs = new Queue<Position>();
            var foundPath = false;

            this.SearchInLabirint(ref foundPath, ref bfs, ref visitedPositions);

            if (foundPath)
            {
                var path = this.GetPath(ref visitedPositions);
                path.Reverse();
                this.ShowPassage(ref path);
            }
            else
            {
                this.PrintField();
                Console.WriteLine("Path was not found");
            }
        }
    }
}